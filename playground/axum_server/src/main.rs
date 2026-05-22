mod api_docs;
mod models;
mod routes;

use axum::{routing::get, Router};
use tower_http::cors::{Any, CorsLayer};

#[tokio::main]
async fn main() {
    // Initialize structured logging
    tracing_subscriber::fmt::init();

    // CORS: allow any origin (for local dev / testing)
    let cors = CorsLayer::new()
        .allow_origin(Any)
        .allow_methods(Any)
        .allow_headers(Any);

    // Build the router — equivalent to FastAPI's `app.include_router()`
    let app = Router::new()
        .route("/", get(routes::rest::root))
        .route("/health", get(routes::rest::health))
        .route("/echo", axum::routing::post(routes::rest::echo))
        .route("/ws", get(routes::ws::ws_handler))
        .merge(api_docs::swagger_ui())
        .layer(cors);

    let addr = "127.0.0.1:7878";
    println!("========================================");
    println!("  Axum Server");
    println!("  REST API:   http://{}/", addr);
    println!("  Swagger UI: http://{}/docs", addr);
    println!("  OpenAPI:    http://{}/api-docs/openapi.json", addr);
    println!("  WebSocket:  ws://{}/ws", addr);
    println!("========================================");

    let listener = tokio::net::TcpListener::bind(addr).await.unwrap();
    axum::serve(listener, app).await.unwrap();
}
