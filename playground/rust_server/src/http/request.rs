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
