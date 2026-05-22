use axum::Json;

use crate::models::{EchoRequest, EchoResponse, HealthResponse, MessageResponse};

/// GET / — Welcome endpoint.
///
/// The simplest possible Axum handler: returns a JSON body.
/// `Json(...)` tells Axum to serialize the struct to JSON and set
/// `Content-Type: application/json` on the response.
#[utoipa::path(
    get,
    path = "/",
    responses(
        (status = 200, description = "Welcome message", body = MessageResponse)
    )
)]
pub async fn root() -> Json<MessageResponse> {
    Json(MessageResponse {
        message: "Hello from Axum!",
    })
}

/// GET /health — Standard health check, same pattern as FastAPI.
#[utoipa::path(
    get,
    path = "/health",
    responses(
        (status = 200, description = "Health status", body = HealthResponse)
    )
)]
pub async fn health() -> Json<HealthResponse> {
    Json(HealthResponse {
        status: "ok",
        version: env!("CARGO_PKG_VERSION"),
    })
}

/// POST /echo — Echo posted JSON with a server timestamp.
///
/// `Json(req)` extracts and deserializes the request body into an `EchoRequest`.
/// If the JSON is malformed or missing fields, Axum automatically returns a 422
/// with a helpful error — no manual validation needed.
#[utoipa::path(
    post,
    path = "/echo",
    request_body = EchoRequest,
    responses(
        (status = 200, description = "Echo response", body = EchoResponse),
        (status = 422, description = "Invalid JSON body")
    )
)]
pub async fn echo(Json(req): Json<EchoRequest>) -> Json<EchoResponse> {
    let now = std::time::SystemTime::now()
        .duration_since(std::time::UNIX_EPOCH)
        .unwrap_or_default()
        .as_secs();

    Json(EchoResponse {
        length: req.content.len(),
        echo: req.content,
        received_at: now,
    })
}
