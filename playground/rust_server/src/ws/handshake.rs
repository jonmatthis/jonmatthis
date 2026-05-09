use std::collections::HashMap;

/// The magic GUID defined by RFC 6455 section 4.2.2.
/// This fixed string prevents cross-protocol attacks — a malicious
/// HTTP cache or proxy can't replay a WebSocket handshake because
/// the accept key depends on this server-only secret.
const WS_GUID: &str = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11";

pub struct WsHandshake {
    /// The bytes to send back to the client to complete the handshake
    pub response: Vec<u8>,
}

/// Attempt a WebSocket upgrade handshake.
/// Returns Some(handshake) if the request headers contain a valid
/// WebSocket upgrade request, None otherwise.
pub fn try_upgrade(headers: &HashMap<String, String>) -> Option<WsHandshake> {
    let upgrade = headers.get("upgrade")?;
    let connection = headers.get("connection")?;
    let key = headers.get("sec-websocket-key")?;

    if !upgrade.eq_ignore_ascii_case("websocket") {
        return None;
    }
    if !connection.to_lowercase().contains("upgrade") {
        return None;
    }

    // Step 1: Concatenate client key + magic GUID
    let mut concat = String::with_capacity(key.len() + WS_GUID.len());
    concat.push_str(key);
    concat.push_str(WS_GUID);

    // Step 2: SHA-1 hash the concatenated string → 20 bytes
    let sha1_hash = sha1(concat.as_bytes());

    // Step 3: Base64 encode those 20 bytes → 28-character accept key
    let accept_key = base64_encode(&sha1_hash);

    // Step 4: Build the HTTP 101 Switching Protocols response
    let response = format!(
        "HTTP/1.1 101 Switching Protocols\r\n\
         Upgrade: websocket\r\n\
         Connection: Upgrade\r\n\
         Sec-WebSocket-Accept: {}\r\n\
         \r\n",
        accept_key
    );

    Some(WsHandshake {
        response: response.into_bytes(),
    })
}

// ═══════════════════════════════════════════════════════
// SHA-1 — we implement this ourselves because std has no
// cryptographic hash functions. The WebSocket spec (RFC 6455)
// mandates SHA-1 for the accept key computation.
// ═══════════════════════════════════════════════════════

fn sha1(data: &[u8]) -> [u8; 20] {
    // Step 1: Padding.
    // SHA-1 processes data in 64-byte (512-bit) chunks.
    // We append bytes so the total length is a multiple of 64.
    // The last 8 bytes of the padding are the original message
    // length in bits, stored as a 64-bit big-endian integer.
    let bit_len = (data.len() as u64) * 8;
    let mut msg = data.to_vec();
    msg.push(0x80); // a single 1 bit (0x80 = 10000000 in binary)
    while (msg.len() % 64) != 56 {
        msg.push(0x00);
    }
    msg.extend_from_slice(&bit_len.to_be_bytes());

    // Step 2: Initialize hash state (h0-h4).
    // These are the standard SHA-1 initial values from FIPS 180-4.
    let mut h: [u32; 5] = [
        0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0,
    ];

    // Step 3: Process each 64-byte chunk
    for chunk in msg.chunks(64) {
        // Expand 16 u32 words into 80 u32 words via XOR + rotate
        let mut w = [0u32; 80];
        for i in 0..16 {
            w[i] = u32::from_be_bytes([
                chunk[i * 4],
                chunk[i * 4 + 1],
                chunk[i * 4 + 2],
                chunk[i * 4 + 3],
            ]);
        }
        for i in 16..80 {
            w[i] = (w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16]).rotate_left(1);
        }

        let [mut a, mut b, mut c, mut d, mut e] = h;

        // Step 4: 80 rounds of the compression function
        for i in 0..80 {
            let (f, k): (u32, u32) = match i {
                0..=19 => ((b & c) | ((!b) & d), 0x5A827999),
                20..=39 => (b ^ c ^ d, 0x6ED9EBA1),
                40..=59 => ((b & c) | (b & d) | (c & d), 0x8F1BBCDC),
                _ => (b ^ c ^ d, 0xCA62C1D6),
            };
            let temp = a
                .rotate_left(5)
                .wrapping_add(f)
                .wrapping_add(e)
                .wrapping_add(k)
                .wrapping_add(w[i]);
            e = d;
            d = c;
            c = b.rotate_left(30);
            b = a;
            a = temp;
        }

        h[0] = h[0].wrapping_add(a);
        h[1] = h[1].wrapping_add(b);
        h[2] = h[2].wrapping_add(c);
        h[3] = h[3].wrapping_add(d);
        h[4] = h[4].wrapping_add(e);
    }

    // Step 5: Convert 5 u32 values into 20 u8 bytes
    let mut result = [0u8; 20];
    for i in 0..5 {
        let bytes = h[i].to_be_bytes();
        result[i * 4..(i + 1) * 4].copy_from_slice(&bytes);
    }
    result
}

// ═══════════════════════════════════════════════════════
// Base64 encoder — also no std implementation.
// Base64 maps each group of 3 bytes (24 bits) into 4
// ASCII characters from a 64-character alphabet.
// ═══════════════════════════════════════════════════════

const B64: &[u8; 64] =
    b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

fn base64_encode(data: &[u8]) -> String {
    let mut out = String::with_capacity(((data.len() + 2) / 3) * 4);
    for chunk in data.chunks(3) {
        let b0 = chunk[0] as u32;
        let b1 = if chunk.len() > 1 { chunk[1] as u32 } else { 0 };
        let b2 = if chunk.len() > 2 { chunk[2] as u32 } else { 0 };
        let triple = (b0 << 16) | (b1 << 8) | b2;

        out.push(B64[((triple >> 18) & 0x3F) as usize] as char);
        out.push(B64[((triple >> 12) & 0x3F) as usize] as char);
        out.push(if chunk.len() > 1 {
            B64[((triple >> 6) & 0x3F) as usize] as char
        } else {
            b'=' as char
        });
        out.push(if chunk.len() > 2 {
            B64[(triple & 0x3F) as usize] as char
        } else {
            b'=' as char
        });
    }
    out
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn sha1_abc() {
        // Known test vector: SHA-1("abc") = a9993e36...
        let hash = sha1(b"abc");
        let hex: String = hash.iter().map(|b| format!("{:02x}", b)).collect();
        assert_eq!(hex, "a9993e364706816aba3e25717850c26c9cd0d89d");
    }

    #[test]
    fn ws_accept_key_from_rfc() {
        // From RFC 6455 section 4.2.2, numbered step 7
        let mut headers = HashMap::new();
        headers.insert("upgrade".into(), "websocket".into());
        headers.insert("connection".into(), "Upgrade".into());
        headers.insert(
            "sec-websocket-key".into(),
            "dGhlIHNhbXBsZSBub25jZQ==".into(),
        );

        let hs = try_upgrade(&headers).unwrap();
        let resp = String::from_utf8(hs.response).unwrap();
        // The expected accept key from the RFC example
        assert!(resp.contains("s3pPLMBiTxaQ9kYGzzhZRbK+xOo="));
        assert!(resp.starts_with("HTTP/1.1 101"));
    }

    #[test]
    fn non_websocket_returns_none() {
        let headers = HashMap::new();
        assert!(try_upgrade(&headers).is_none());
    }
}
