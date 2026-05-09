# Rust HTTP + WebSocket Server Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a multi-threaded HTTP + WebSocket server from scratch using only the Rust standard library, following the Rust Book Chapter 21 pedagogical approach.

**Architecture:** 6 sequential stages, each a working milestone. Start with a TCP echo server, layer on HTTP parsing, then routing, then WebSocket upgrade, then a thread pool, and finally wire it all together. Zero external crates.

**Tech Stack:** Rust standard library only. `std::net::TcpListener`, `std::thread`, `std::sync::mpsc`, `std::sync::{Arc, Mutex}`, `std::io::{Read, Write}`.

---

### Task 1: Cargo project and TCP echo server (Stage 1)

**Files:**
- Create: `Cargo.toml`
- Create: `src/main.rs`

- [ ] **Step 1: Initialize Cargo project**

Create `Cargo.toml`:

```toml
[package]
name = "rust_server"
version = "0.1.0"
edition = "2021"
```

- [ ] **Step 2: Write TCP echo server — listen and accept loop**

Write `src/main.rs`:

```rust
use std::io::{Read, Write};
use std::net::{TcpListener, TcpStream};

fn main() {
    // Bind to port 7878 — the Book's canonical port
    let listener = TcpListener::bind("127.0.0.1:7878")
        .expect("Failed to bind to 127.0.0.1:7878");
    println!("Server listening on 127.0.0.1:7878");

    // accept() blocks until a client connects, then returns a TcpStream
    for stream in listener.incoming() {
        match stream {
            Ok(stream) => {
                println!("Connection from {}", stream.peer_addr().unwrap());
                handle_connection(stream);
            }
            Err(e) => eprintln!("Connection failed: {}", e),
        }
    }
}

fn handle_connection(mut stream: TcpStream) {
    // Read what the client sent into a buffer
    let mut buffer = [0u8; 1024];
    match stream.read(&mut buffer) {
        Ok(n) if n > 0 => {
            // Echo it right back
            stream.write_all(&buffer[..n]).unwrap();
            stream.flush().unwrap();
        }
        _ => {}
    }
}
```

- [ ] **Step 3: Build and test with a real TCP client**

Run: `cargo build`

Then in one terminal:
```
cargo run
```

In another terminal:
```
echo "hello from telnet-ish" | nc 127.0.0.1 7878
```

Expected: the server prints the connection and echoes "hello from telnet-ish" back.

(If `nc` isn't available on Windows, use PowerShell: `Test-NetConnection 127.0.0.1 -Port 7878` to verify the port is open, or install netcat.)

---

### Task 2: HTTP request parser (Stage 2)

**Files:**
- Create: `src/http/mod.rs`
- Create: `src/http/request.rs`
- Modify: `src/main.rs`

- [ ] **Step 1: Create `src/http/mod.rs`**

```rust
pub mod request;
```

- [ ] **Step 2: Write HTTP request parser**

Write `src/http/request.rs`:

```rust
use std::collections::HashMap;

#[derive(Debug)]
pub struct HttpRequest {
    pub method: String,
    pub path: String,
    pub headers: HashMap<String, String>,
    pub body: Vec<u8>,
}

impl HttpRequest {
    /// Parse raw bytes from a TCP stream into an HTTP request.
    /// Returns None if the request is incomplete or malformed.
    pub fn parse(raw: &[u8]) -> Option<Self> {
        let text = std::str::from_utf8(raw).ok()?;

        // HTTP is split into headers and body by a blank line: \r\n\r\n
        let mut parts = text.split("\r\n\r\n");
        let header_text = parts.next()?;
        let body_text = parts.next().unwrap_or("");

        let mut lines = header_text.lines();

        // First line: GET /path HTTP/1.1
        let request_line = lines.next()?;
        let mut request_parts = request_line.split_whitespace();
        let method = request_parts.next()?.to_string();
        let path = request_parts.next()?.to_string();

        // Remaining lines before blank line are headers: Key: Value
        let mut headers = HashMap::new();
        for line in lines {
            if let Some((key, value)) = line.split_once(": ") {
                headers.insert(key.to_lowercase(), value.to_string());
            }
        }

        Some(HttpRequest {
            method,
            path,
            headers,
            body: body_text.as_bytes().to_vec(),
        })
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn parse_simple_get() {
        let raw = b"GET /hello HTTP/1.1\r\nHost: localhost\r\n\r\n";
        let req = HttpRequest::parse(raw).unwrap();
        assert_eq!(req.method, "GET");
        assert_eq!(req.path, "/hello");
        assert_eq!(req.headers.get("host").unwrap(), "localhost");
        assert!(req.body.is_empty());
    }
}
```

- [ ] **Step 3: Update `src/main.rs` to use the parser**

At the top of `src/main.rs`, add:
```rust
mod http;
```

Replace the `handle_connection` function:
```rust
fn handle_connection(mut stream: TcpStream) {
    let mut buffer = [0u8; 1024];
    let n = stream.read(&mut buffer).unwrap();
    if n == 0 {
        return;
    }

    match http::request::HttpRequest::parse(&buffer[..n]) {
        Some(req) => println!("Parsed: {} {}", req.method, req.path),
        None => eprintln!("Failed to parse request"),
    }
}
```

- [ ] **Step 4: Run tests**

Run: `cargo test`
Expected: 1 test passes (parse_simple_get)

- [ ] **Step 5: Test with a real HTTP client**

Start the server with `cargo run`, then in another terminal:
```
curl http://127.0.0.1:7878/hello
```

Expected: Server prints `Parsed: GET /hello`. Curl will hang (no response yet — that's Stage 3).

---

### Task 3: HTTP response builder + router (Stage 3)

**Files:**
- Create: `src/http/response.rs`
- Create: `src/http/router.rs`
- Modify: `src/http/mod.rs`
- Modify: `src/http/request.rs` (add tests)
- Modify: `src/main.rs`

- [ ] **Step 1: Update `src/http/mod.rs`**

```rust
pub mod request;
pub mod response;
pub mod router;
```

- [ ] **Step 2: Write HTTP response builder**

Write `src/http/response.rs`:

```rust
pub struct HttpResponse {
    pub status_code: u16,
    pub status_text: String,
    pub headers: Vec<(String, String)>,
    pub body: Vec<u8>,
}

impl HttpResponse {
    pub fn new(status_code: u16, body: &str) -> Self {
        let status_text = status_text(status_code).to_string();
        HttpResponse {
            status_code,
            status_text,
            headers: vec![
                ("Content-Length".into(), body.len().to_string()),
                ("Content-Type".into(), "text/html; charset=utf-8".into()),
            ],
            body: body.as_bytes().to_vec(),
        }
    }

    /// Serialize into raw bytes ready to write to a TCP socket
    pub fn to_bytes(&self) -> Vec<u8> {
        let status_line = format!("HTTP/1.1 {} {}\r\n", self.status_code, self.status_text);
        let headers: String = self
            .headers
            .iter()
            .map(|(k, v)| format!("{}: {}\r\n", k, v))
            .collect();
        let blank = "\r\n";

        let mut bytes = Vec::new();
        bytes.extend_from_slice(status_line.as_bytes());
        bytes.extend_from_slice(headers.as_bytes());
        bytes.extend_from_slice(blank.as_bytes());
        bytes.extend_from_slice(&self.body);
        bytes
    }
}

fn status_text(code: u16) -> &'static str {
    match code {
        200 => "OK",
        404 => "Not Found",
        _ => "Unknown",
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn response_200_contains_status_line() {
        let resp = HttpResponse::new(200, "Hello");
        let bytes = resp.to_bytes();
        let text = String::from_utf8(bytes).unwrap();
        assert!(text.starts_with("HTTP/1.1 200 OK\r\n"));
        assert!(text.contains("Content-Length: 5\r\n"));
        assert!(text.ends_with("Hello"));
    }
}
```

- [ ] **Step 3: Write router**

Write `src/http/router.rs`:

```rust
use crate::http::request::HttpRequest;
use crate::http::response::HttpResponse;

pub fn route(req: &HttpRequest) -> HttpResponse {
    match (req.method.as_str(), req.path.as_str()) {
        ("GET", "/") => HttpResponse::new(200, "<h1>Hello from Rust!</h1>"),
        ("GET", "/health") => HttpResponse::new(200, "OK"),
        _ => HttpResponse::new(404, "<h1>404 Not Found</h1>"),
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn make_req(method: &str, path: &str) -> HttpRequest {
        HttpRequest {
            method: method.to_string(),
            path: path.to_string(),
            headers: std::collections::HashMap::new(),
            body: vec![],
        }
    }

    #[test]
    fn root_returns_200() {
        let req = make_req("GET", "/");
        let resp = route(&req);
        assert_eq!(resp.status_code, 200);
    }

    #[test]
    fn unknown_returns_404() {
        let req = make_req("GET", "/nonexistent");
        let resp = route(&req);
        assert_eq!(resp.status_code, 404);
    }
}
```

- [ ] **Step 4: Update `src/main.rs` `handle_connection` to send responses**

Replace the current `handle_connection`:
```rust
fn handle_connection(mut stream: TcpStream) {
    let mut buffer = [0u8; 4096];
    let n = stream.read(&mut buffer).unwrap();
    if n == 0 {
        return;
    }

    if let Some(req) = http::request::HttpRequest::parse(&buffer[..n]) {
        println!("{} {}", req.method, req.path);
        let response = http::router::route(&req);
        stream.write_all(&response.to_bytes()).unwrap();
        stream.flush().unwrap();
    }
}
```

- [ ] **Step 5: Run all tests**

Run: `cargo test`
Expected: 4 tests pass (1 request + 1 response + 2 router)

- [ ] **Step 6: Test with curl**

Start server with `cargo run`, then:
```
curl http://127.0.0.1:7878/
curl http://127.0.0.1:7878/health
curl http://127.0.0.1:7878/nope
```

Expected: HTML for `/`, "OK" for `/health`, 404 for `/nope`.

---

### Task 4: WebSocket upgrade handshake (Stage 4)

**Files:**
- Create: `src/ws/mod.rs`
- Create: `src/ws/handshake.rs`
- Modify: `src/main.rs`

- [ ] **Step 1: Create `src/ws/mod.rs`**

```rust
pub mod handshake;
```

- [ ] **Step 2: Write WebSocket handshake (with SHA-1)**

Write `src/ws/handshake.rs`:

```rust
use std::collections::HashMap;

/// The magic GUID defined by RFC 6455
const WS_GUID: &str = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11";

/// Result of a successful WebSocket upgrade handshake
pub struct WsHandshake {
    pub response: Vec<u8>,   // bytes to send back to complete handshake
}

pub fn try_upgrade(headers: &HashMap<String, String>) -> Option<WsHandshake> {
    // Check required headers
    let upgrade = headers.get("upgrade")?;
    let connection = headers.get("connection")?;
    let key = headers.get("sec-websocket-key")?;

    if !upgrade.eq_ignore_ascii_case("websocket") {
        return None;
    }
    if !connection.to_lowercase().contains("upgrade") {
        return None;
    }

    // Step 1: Concatenate client key + magic GUID (pen on paper: write them end to end)
    let mut input = String::with_capacity(key.len() + WS_GUID.len());
    input.push_str(key);
    input.push_str(WS_GUID);

    // Step 2: SHA-1 hash the concatenated string
    let sha1_hash = sha1(input.as_bytes());

    // Step 3: Base64 encode the 20-byte hash
    let accept_key = base64_encode(&sha1_hash);

    // Step 4: Build the 101 Switching Protocols response
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

// ═══════════════════════════════════════════════════════════
// SHA-1 implementation (no external crates)
// ═══════════════════════════════════════════════════════════

fn sha1(data: &[u8]) -> [u8; 20] {
    // Padding: append a 1 bit, then zeros, then 64-bit length in big-endian
    let mut msg = data.to_vec();
    let bit_len = (msg.len() as u64) * 8;

    msg.push(0x80); // append 1 bit (as 0x80 byte)
    while (msg.len() % 64) != 56 {
        msg.push(0x00);
    }
    msg.extend_from_slice(&bit_len.to_be_bytes());

    // Initial hash values (h0-h4)
    let mut h: [u32; 5] = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0];

    // Process each 64-byte chunk
    for chunk in msg.chunks(64) {
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

    let mut result = [0u8; 20];
    for i in 0..5 {
        let bytes = h[i].to_be_bytes();
        result[i * 4..(i + 1) * 4].copy_from_slice(&bytes);
    }
    result
}

// ═══════════════════════════════════════════════════════════
// Base64 encoder (no external crates)
// ═══════════════════════════════════════════════════════════

const BASE64_TABLE: &[u8; 64] = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

fn base64_encode(data: &[u8]) -> String {
    let mut result = String::with_capacity(((data.len() + 2) / 3) * 4);
    for chunk in data.chunks(3) {
        let b0 = chunk[0];
        let b1 = if chunk.len() > 1 { chunk[1] } else { 0 };
        let b2 = if chunk.len() > 2 { chunk[2] } else { 0 };
        let triple = (b0 as u32) << 16 | (b1 as u32) << 8 | b2 as u32;

        result.push(BASE64_TABLE[((triple >> 18) & 0x3F) as usize] as char);
        result.push(BASE64_TABLE[((triple >> 12) & 0x3F) as usize] as char);
        if chunk.len() > 1 {
            result.push(BASE64_TABLE[((triple >> 6) & 0x3F) as usize] as char);
        } else {
            result.push('=');
        }
        if chunk.len() > 2 {
            result.push(BASE64_TABLE[(triple & 0x3F) as usize] as char);
        } else {
            result.push('=');
        }
    }
    result
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_sha1_known_value() {
        // SHA-1("abc") = a9993e36...
        let hash = sha1(b"abc");
        let hex: String = hash.iter().map(|b| format!("{:02x}", b)).collect();
        assert_eq!(hex, "a9993e364706816aba3e25717850c26c9cd0d89d");
    }

    #[test]
    fn test_ws_accept_key() {
        // From RFC 6455 section 4.2.2
        let mut headers = HashMap::new();
        headers.insert("upgrade".into(), "websocket".into());
        headers.insert("connection".into(), "Upgrade".into());
        headers.insert("sec-websocket-key".into(), "dGhlIHNhbXBsZSBub25jZQ==".into());

        let handshake = try_upgrade(&headers).unwrap();
        let response = String::from_utf8(handshake.response).unwrap();
        assert!(response.contains("s3pPLMBiTxaQ9kYGzzhZRbK+xOo="));
    }
}
```

- [ ] **Step 3: Update `src/main.rs` to handle WebSocket upgrade**

Add the module declaration at the top:
```rust
mod ws;
```

Update `handle_connection`:
```rust
fn handle_connection(mut stream: TcpStream) {
    let mut buffer = [0u8; 4096];
    let n = stream.read(&mut buffer).unwrap();
    if n == 0 {
        return;
    }

    if let Some(req) = http::request::HttpRequest::parse(&buffer[..n]) {
        println!("{} {}", req.method, req.path);

        // Check if this is a WebSocket upgrade request
        if let Some(handshake) = ws::handshake::try_upgrade(&req.headers) {
            stream.write_all(&handshake.response).unwrap();
            stream.flush().unwrap();
            println!("WebSocket upgraded");
            // For now, just close the connection after upgrade
            return;
        }

        let response = http::router::route(&req);
        stream.write_all(&response.to_bytes()).unwrap();
        stream.flush().unwrap();
    }
}
```

- [ ] **Step 4: Run all tests**

Run: `cargo test`
Expected: 6 tests pass (1 request + 1 response + 2 router + 2 handshake)

---

### Task 5: WebSocket frame reading + writing (Stage 4 continued)

**Files:**
- Create: `src/ws/frame.rs`
- Modify: `src/ws/mod.rs`

- [ ] **Step 1: Update `src/ws/mod.rs`**

```rust
pub mod handshake;
pub mod frame;
```

- [ ] **Step 2: Write WebSocket frame encoder/decoder**

Write `src/ws/frame.rs`:

```rust
/// WebSocket opcodes
pub const OP_TEXT: u8 = 0x1;
pub const OP_CLOSE: u8 = 0x8;
pub const OP_PING: u8 = 0x9;
pub const OP_PONG: u8 = 0xA;

#[derive(Debug)]
pub struct WsFrame {
    pub opcode: u8,
    pub payload: Vec<u8>,
    pub is_final: bool,
}

impl WsFrame {
    /// Create a text frame
    pub fn text(data: &str) -> Self {
        WsFrame {
            opcode: OP_TEXT,
            payload: data.as_bytes().to_vec(),
            is_final: true,
        }
    }

    /// Create a close frame
    pub fn close() -> Self {
        WsFrame {
            opcode: OP_CLOSE,
            payload: vec![],
            is_final: true,
        }
    }

    /// Encode this frame into bytes to send over TCP
    /// Server→client frames are NOT masked per RFC 6455
    pub fn encode(&self) -> Vec<u8> {
        let mut bytes = Vec::new();

        // Byte 1: FIN (bit 7) + opcode (bits 0-3)
        let fin_bit = if self.is_final { 0x80 } else { 0x00 };
        bytes.push(fin_bit | (self.opcode & 0x0F));

        // Byte 2+: payload length + optional mask (server sends unmasked)
        let len = self.payload.len();
        if len < 126 {
            bytes.push(len as u8);
        } else if len <= 65535 {
            bytes.push(126);
            bytes.extend_from_slice(&(len as u16).to_be_bytes());
        } else {
            bytes.push(127);
            bytes.extend_from_slice(&(len as u64).to_be_bytes());
        }

        bytes.extend_from_slice(&self.payload);
        bytes
    }

    /// Try to decode a frame from bytes read from TCP
    /// Returns None if we don't have a complete frame yet
    pub fn decode(raw: &[u8]) -> Option<(WsFrame, usize)> {
        if raw.len() < 2 {
            return None;
        }

        let fin = (raw[0] & 0x80) != 0;
        let opcode = raw[0] & 0x0F;
        let masked = (raw[1] & 0x80) != 0;
        let mut len = (raw[1] & 0x7F) as usize;

        let mut pos = 2;

        // Extended payload length
        if len == 126 {
            if raw.len() < 4 { return None; }
            len = u16::from_be_bytes([raw[2], raw[3]]) as usize;
            pos = 4;
        } else if len == 127 {
            if raw.len() < 10 { return None; }
            len = u64::from_be_bytes([
                raw[2], raw[3], raw[4], raw[5], raw[6], raw[7], raw[8], raw[9],
            ]) as usize;
            pos = 10;
        }

        // Masking key (4 bytes, only present in client→server frames)
        let mask = if masked {
            if raw.len() < pos + 4 { return None; }
            let m = [raw[pos], raw[pos + 1], raw[pos + 2], raw[pos + 3]];
            pos += 4;
            Some(m)
        } else {
            None
        };

        // Payload
        if raw.len() < pos + len {
            return None;
        }
        let mut payload = raw[pos..pos + len].to_vec();

        // Unmask if needed
        if let Some(m) = mask {
            for i in 0..payload.len() {
                payload[i] ^= m[i % 4];
            }
        }

        Some((
            WsFrame {
                opcode,
                payload,
                is_final: fin,
            },
            pos + len,
        ))
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn decode_masked_text_frame() {
        // A real masked frame: FIN=1, opcode=1 (text), mask=0x37FA213D, payload="Hello"
        let frame = vec![
            0x81, 0x85, // FIN+text, MASK+len=5
            0x37, 0xFA, 0x21, 0x3D, // mask
            0x7F, 0x9F, 0x4D, 0x51, 0x58, // masked "Hello"
        ];
        let (decoded, consumed) = WsFrame::decode(&frame).unwrap();
        assert_eq!(decoded.opcode, OP_TEXT);
        assert_eq!(decoded.payload, b"Hello");
        assert!(decoded.is_final);
        assert_eq!(consumed, frame.len());
    }

    #[test]
    fn encode_text_frame_no_mask() {
        let frame = WsFrame::text("Hi");
        let bytes = frame.encode();
        // Server frames are unmasked: FIN=0x80|0x1=0x81, len=2, "Hi"
        assert_eq!(bytes, vec![0x81, 0x02, b'H', b'i']);
    }

    #[test]
    fn roundtrip_unmasked() {
        let original = WsFrame::text("roundtrip test");
        let encoded = original.encode();
        let (decoded, _) = WsFrame::decode(&encoded).unwrap();
        assert_eq!(decoded.payload, b"roundtrip test");
    }
}
```

- [ ] **Step 3: Run all tests**

Run: `cargo test`
Expected: 9 tests pass (1 request + 1 response + 2 router + 2 handshake + 3 frame)

---

### Task 6: Single-threaded WebSocket echo server (Stage 4 complete)

**Files:**
- Modify: `src/main.rs`

- [ ] **Step 1: Replace `handle_connection` and add WebSocket echo loop**

Replace the entire `handle_connection` in `src/main.rs` and add the `handle_ws_connection` function:

```rust
fn handle_connection(mut stream: TcpStream) {
    let mut buffer = [0u8; 4096];
    let n = stream.read(&mut buffer).unwrap();
    if n == 0 {
        return;
    }

    if let Some(req) = http::request::HttpRequest::parse(&buffer[..n]) {
        println!("{} {}", req.method, req.path);

        // WebSocket upgrade path
        if let Some(handshake) = ws::handshake::try_upgrade(&req.headers) {
            stream.write_all(&handshake.response).unwrap();
            stream.flush().unwrap();
            println!("WS connected: {}", stream.peer_addr().unwrap());
            handle_ws_connection(stream);
            return;
        }

        // Normal HTTP path
        let response = http::router::route(&req);
        stream.write_all(&response.to_bytes()).unwrap();
        stream.flush().unwrap();
    }
}

fn handle_ws_connection(mut stream: TcpStream) {
    use crate::ws::frame::{WsFrame, OP_CLOSE, OP_PING, OP_PONG, OP_TEXT};

    let mut accumulated = Vec::new();
    let mut read_buf = vec![0u8; 4096];

    loop {
        match stream.read(&mut read_buf) {
            Ok(0) => {
                println!("WS disconnected");
                break;
            }
            Ok(n) => {
                accumulated.extend_from_slice(&read_buf[..n]);

                // Try to decode frames from the accumulated buffer
                while let Some((frame, consumed)) = WsFrame::decode(&accumulated) {
                    // Remove consumed bytes
                    accumulated.drain(..consumed);

                    match frame.opcode {
                        OP_TEXT => {
                            let msg = String::from_utf8_lossy(&frame.payload);
                            println!("WS received: {}", msg);
                            // Echo back
                            let response = WsFrame::text(&format!("Echo: {}", msg));
                            stream.write_all(&response.encode()).unwrap();
                            stream.flush().unwrap();
                        }
                        OP_PING => {
                            let mut pong = WsFrame {
                                opcode: OP_PONG,
                                payload: frame.payload,
                                is_final: true,
                            };
                            stream.write_all(&pong.encode()).unwrap();
                            stream.flush().unwrap();
                        }
                        OP_CLOSE => {
                            let close = WsFrame::close();
                            stream.write_all(&close.encode()).unwrap();
                            stream.flush().unwrap();
                            println!("WS close frame received");
                            return;
                        }
                        _ => {
                            println!("WS unknown opcode: {}", frame.opcode);
                        }
                    }
                }
            }
            Err(e) => {
                eprintln!("WS read error: {}", e);
                break;
            }
        }
    }
}
```

- [ ] **Step 2: Build and test**

Run: `cargo build`

To test WebSocket, you can use a browser's console or a tool like `websocat`. In Chrome DevTools console:
```javascript
const ws = new WebSocket("ws://127.0.0.1:7878/");
ws.onmessage = (e) => console.log("Received:", e.data);
ws.onopen = () => ws.send("Hello from browser!");
```

Expected: Server prints "WS received: Hello from browser!" and browser console shows "Received: Echo: Hello from browser!"

---

### Task 7: Thread pool (Stage 5)

**Files:**
- Create: `src/thread_pool.rs`
- Modify: `src/main.rs`

- [ ] **Step 1: Write the ThreadPool**

Write `src/thread_pool.rs`:

```rust
use std::sync::{mpsc, Arc, Mutex};
use std::thread;

type Job = Box<dyn FnOnce() + Send + 'static>;

pub struct ThreadPool {
    workers: Vec<Worker>,
    sender: Option<mpsc::Sender<Job>>,
}

struct Worker {
    id: usize,
    thread: Option<thread::JoinHandle<()>>,
}

impl ThreadPool {
    /// Create a new ThreadPool with `size` worker threads.
    ///
    /// # Panics
    /// Panics if size is 0.
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0, "ThreadPool size must be greater than 0");

        let (sender, receiver) = mpsc::channel();
        let receiver = Arc::new(Mutex::new(receiver));

        let mut workers = Vec::with_capacity(size);
        for id in 0..size {
            workers.push(Worker::new(id, Arc::clone(&receiver)));
        }

        ThreadPool {
            workers,
            sender: Some(sender),
        }
    }

    /// Send a closure to be executed by a worker thread.
    pub fn execute<F>(&self, f: F)
    where
        F: FnOnce() + Send + 'static,
    {
        let job = Box::new(f);
        self.sender.as_ref().unwrap().send(job).unwrap();
    }
}

impl Drop for ThreadPool {
    fn drop(&mut self) {
        // Drop the sender — workers will see the channel is closed and exit
        drop(self.sender.take());

        for worker in &mut self.workers {
            println!("Shutting down worker {}", worker.id);
            if let Some(thread) = worker.thread.take() {
                thread.join().unwrap();
            }
        }
    }
}

impl Worker {
    fn new(id: usize, receiver: Arc<Mutex<mpsc::Receiver<Job>>>) -> Worker {
        let thread = thread::spawn(move || {
            loop {
                // Lock the mutex, receive a job
                let job = {
                    let receiver = receiver.lock().unwrap();
                    receiver.recv()
                };

                match job {
                    Ok(job) => {
                        println!("Worker {id} got a job; executing.");
                        job();
                    }
                    Err(_) => {
                        println!("Worker {id} disconnected; shutting down.");
                        break;
                    }
                }
            }
        });

        Worker {
            id,
            thread: Some(thread),
        }
    }
}
```

- [ ] **Step 2: Update `src/main.rs` to use ThreadPool**

Add the module declaration:
```rust
mod thread_pool;
```

Replace `main()`:
```rust
fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878")
        .expect("Failed to bind to 127.0.0.1:7878");

    let pool = thread_pool::ThreadPool::new(4);
    println!("Server listening on 127.0.0.1:7878 (4 workers)");

    for stream in listener.incoming() {
        match stream {
            Ok(stream) => {
                pool.execute(|| {
                    handle_connection(stream);
                });
            }
            Err(e) => eprintln!("Connection failed: {}", e),
        }
    }
}
```

- [ ] **Step 3: Build and test**

Run: `cargo build`

Start the server and connect from multiple terminals simultaneously:
```
curl http://127.0.0.1:7878/ &
curl http://127.0.0.1:7878/ &
curl http://127.0.0.1:7878/ &
```

Expected: All three respond correctly. Server log shows different workers handling different connections.

---

### Task 8: Multi-threaded WebSocket server with shared state (Stage 6)

**Files:**
- Create: `src/server.rs`
- Modify: `src/main.rs`

- [ ] **Step 1: Extract server logic into `src/server.rs`**

Write `src/server.rs`:

```rust
use std::io::{Read, Write};
use std::net::{TcpListener, TcpStream};
use std::sync::{Arc, Mutex};
use std::collections::HashSet;

use crate::http;
use crate::ws;
use crate::ws::frame::{WsFrame, OP_TEXT, OP_CLOSE, OP_PING, OP_PONG};
use crate::thread_pool::ThreadPool;

/// Shared state visible to all worker threads
pub struct ServerState {
    /// Number of active WebSocket connections
    pub ws_connections: Mutex<usize>,
}

pub struct Server {
    state: Arc<ServerState>,
}

impl Server {
    pub fn new() -> Self {
        Server {
            state: Arc::new(ServerState {
                ws_connections: Mutex::new(0),
            }),
        }
    }

    pub fn run(&self, addr: &str, pool_size: usize) {
        let listener = TcpListener::bind(addr)
            .expect(&format!("Failed to bind to {}", addr));

        let pool = ThreadPool::new(pool_size);
        println!("Server listening on {} ({} workers)", addr, pool_size);

        let state = Arc::clone(&self.state);

        for stream in listener.incoming() {
            match stream {
                Ok(stream) => {
                    let state = Arc::clone(&state);
                    pool.execute(move || {
                        handle_connection(stream, &state);
                    });
                }
                Err(e) => eprintln!("Connection failed: {}", e),
            }
        }
    }
}

fn handle_connection(mut stream: TcpStream, state: &ServerState) {
    let mut buffer = [0u8; 4096];
    let n = match stream.read(&mut buffer) {
        Ok(n) => n,
        Err(_) => return,
    };
    if n == 0 {
        return;
    }

    if let Some(req) = http::request::HttpRequest::parse(&buffer[..n]) {
        println!("{} {}", req.method, req.path);

        if let Some(handshake) = ws::handshake::try_upgrade(&req.headers) {
            stream.write_all(&handshake.response).unwrap();
            stream.flush().unwrap();

            {
                let mut count = state.ws_connections.lock().unwrap();
                *count += 1;
                println!("WS connected ({} active)", *count);
            }

            handle_ws(stream);

            {
                let mut count = state.ws_connections.lock().unwrap();
                *count -= 1;
                println!("WS disconnected ({} active)", *count);
            }
            return;
        }

        let response = http::router::route(&req);
        stream.write_all(&response.to_bytes()).unwrap();
        stream.flush().unwrap();
    }
}

fn handle_ws(mut stream: TcpStream) {
    let mut accumulated = Vec::new();
    let mut read_buf = vec![0u8; 4096];

    loop {
        match stream.read(&mut read_buf) {
            Ok(0) => break,
            Ok(n) => {
                accumulated.extend_from_slice(&read_buf[..n]);

                while let Some((frame, consumed)) = WsFrame::decode(&accumulated) {
                    accumulated.drain(..consumed);

                    match frame.opcode {
                        OP_TEXT => {
                            let msg = String::from_utf8_lossy(&frame.payload);
                            println!("WS: {}", msg);
                            let resp = WsFrame::text(&format!("Echo: {}", msg));
                            let _ = stream.write_all(&resp.encode());
                            let _ = stream.flush();
                        }
                        OP_PING => {
                            let pong = WsFrame {
                                opcode: OP_PONG,
                                payload: frame.payload,
                                is_final: true,
                            };
                            let _ = stream.write_all(&pong.encode());
                            let _ = stream.flush();
                        }
                        OP_CLOSE => {
                            let close = WsFrame::close();
                            let _ = stream.write_all(&close.encode());
                            let _ = stream.flush();
                            return;
                        }
                        _ => {}
                    }
                }
            }
            Err(_) => break,
        }
    }
}
```

- [ ] **Step 2: Simplify `src/main.rs` to just the entry point**

Replace `src/main.rs` entirely:

```rust
mod http;
mod ws;
mod thread_pool;
mod server;

fn main() {
    let server = server::Server::new();
    server.run("127.0.0.1:7878", 4);
}
```

- [ ] **Step 3: Build and test everything**

Run: `cargo build && cargo test`

Expected: All tests pass, server builds cleanly.

Test HTTP:
```
curl http://127.0.0.1:7878/
curl http://127.0.0.1:7878/health
```

Test WebSocket (browser console or websocat):
```javascript
const ws = new WebSocket("ws://127.0.0.1:7878/");
ws.onmessage = (e) => console.log(e.data);
ws.onopen = () => ws.send("Hello from multi-threaded server!");
```

Expected: Server tracks connection count, echo works across multiple concurrent WebSocket clients.

---

### Task 9: Final review and cleanup

- [ ] **Step 1: Run full test suite**

```
cargo test
```

Expected: All tests pass.

- [ ] **Step 2: Run `cargo clippy` if available, or `cargo build` with no warnings**

```
cargo build
```

Expected: No warnings.

- [ ] **Step 3: Verify file structure**

```
src/
  main.rs
  server.rs
  thread_pool.rs
  http/
    mod.rs
    request.rs
    response.rs
    router.rs
  ws/
    mod.rs
    handshake.rs
    frame.rs
```
