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
    use std::collections::HashMap;

    fn make_req(method: &str, path: &str) -> HttpRequest {
        HttpRequest {
            method: method.to_string(),
            path: path.to_string(),
            headers: HashMap::new(),
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
