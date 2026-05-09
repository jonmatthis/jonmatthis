/// WebSocket opcodes (RFC 6455 section 5.2)
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
    pub fn text(data: &str) -> Self {
        WsFrame {
            opcode: OP_TEXT,
            payload: data.as_bytes().to_vec(),
            is_final: true,
        }
    }

    pub fn close() -> Self {
        WsFrame {
            opcode: OP_CLOSE,
            payload: vec![],
            is_final: true,
        }
    }

    /// Encode this frame into bytes to send over TCP.
    /// Server → client frames are NOT masked (RFC 6455 section 5.3).
    pub fn encode(&self) -> Vec<u8> {
        let mut bytes = Vec::new();

        // Byte 0: FIN bit (0x80) + 4-bit opcode
        let fin = if self.is_final { 0x80 } else { 0x00 };
        bytes.push(fin | (self.opcode & 0x0F));

        // Byte 1+: payload length. Server sends unmasked.
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

    /// Try to decode a WebSocket frame from raw bytes.
    /// Returns Some((frame, bytes_consumed)) on success,
    /// None if we don't have a complete frame yet.
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
            if raw.len() < 4 {
                return None;
            }
            len = u16::from_be_bytes([raw[2], raw[3]]) as usize;
            pos = 4;
        } else if len == 127 {
            if raw.len() < 10 {
                return None;
            }
            len = u64::from_be_bytes([
                raw[2], raw[3], raw[4], raw[5], raw[6], raw[7], raw[8], raw[9],
            ]) as usize;
            pos = 10;
        }

        // Client → server frames MUST be masked (4-byte masking key)
        let mask = if masked {
            if raw.len() < pos + 4 {
                return None;
            }
            let m = [raw[pos], raw[pos + 1], raw[pos + 2], raw[pos + 3]];
            pos += 4;
            Some(m)
        } else {
            None
        };

        if raw.len() < pos + len {
            return None;
        }

        let mut payload = raw[pos..pos + len].to_vec();

        // Unmask: XOR each byte with the corresponding mask byte
        if let Some(m) = mask {
            for i in 0..payload.len() {
                payload[i] ^= m[i % 4];
            }
        }

        Some((WsFrame { opcode, payload, is_final: fin }, pos + len))
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn decode_masked_text_frame() {
        // Hand-crafted: FIN=1, opcode=1 (text), MASK=1, len=5
        // mask = [0x37, 0xFA, 0x21, 0x3D]
        // "Hello" XORed with mask = [0x7F, 0x9F, 0x4D, 0x51, 0x58]
        let frame = vec![
            0x81, 0x85, 0x37, 0xFA, 0x21, 0x3D, 0x7F, 0x9F, 0x4D, 0x51, 0x58,
        ];
        let (decoded, consumed) = WsFrame::decode(&frame).unwrap();
        assert_eq!(decoded.opcode, OP_TEXT);
        assert_eq!(decoded.payload, b"Hello");
        assert!(decoded.is_final);
        assert_eq!(consumed, frame.len());
    }

    #[test]
    fn encode_unmasked_text() {
        let frame = WsFrame::text("Hi");
        let bytes = frame.encode();
        // 0x81 = FIN + text opcode, 0x02 = len, then "Hi"
        assert_eq!(bytes, vec![0x81, 0x02, b'H', b'i']);
    }

    #[test]
    fn roundtrip_unmasked() {
        let original = WsFrame::text("roundtrip");
        let encoded = original.encode();
        let (decoded, _) = WsFrame::decode(&encoded).unwrap();
        assert_eq!(decoded.payload, b"roundtrip");
    }
}
