use serde::{Deserialize, Serialize};
use utoipa::ToSchema;

/// Generic message response — used by nearly every endpoint.
/// The `#[schema]` derive generates the OpenAPI schema for Swagger.
#[derive(Debug, Serialize, ToSchema)]
pub struct MessageResponse {
    /// Human-readable status or greeting
    pub message: &'static str,
}

/// Structured health status, matching the common FastAPI pattern.
#[derive(Debug, Serialize, ToSchema)]
pub struct HealthResponse {
    pub status: &'static str,
    pub version: &'static str,
}

/// Request body accepted by POST /echo.
/// The `Deserialize` derive lets Axum auto-parse JSON bodies,
/// exactly like Pydantic's `BaseModel` in FastAPI.
#[derive(Debug, Deserialize, ToSchema)]
pub struct EchoRequest {
    /// Any string payload — we echo it back
    pub content: String,
}

/// Response body for POST /echo, including a server timestamp.
#[derive(Debug, Serialize, ToSchema)]
pub struct EchoResponse {
    /// The original content, echoed back
    pub echo: String,
    /// Byte length of the original content
    pub length: usize,
    /// Server-side timestamp (seconds since Unix epoch)
    pub received_at: u64,
}
