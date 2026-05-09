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
        let status_line = format!(
            "HTTP/1.1 {} {}\r\n",
            self.status_code, self.status_text
        );
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
