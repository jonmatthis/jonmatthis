use utoipa::OpenApi;
use utoipa_swagger_ui::SwaggerUi;

use crate::routes::{rest, ws};

/// The root OpenAPI document.
///
/// `#[openapi]` scans all the `#[utoipa::path]` attributes on our handlers
/// and compiles them into a single OpenAPI 3.0 spec at compile time.
/// `components(schemas(...))` registers our request/response types so they
/// show up in the Schemas section of Swagger UI.
#[derive(OpenApi)]
#[openapi(
    paths(
        rest::root,
        rest::health,
        rest::echo,
        ws::ws_handler,
    ),
    components(
        schemas(
            crate::models::MessageResponse,
            crate::models::HealthResponse,
            crate::models::EchoRequest,
            crate::models::EchoResponse,
        )
    ),
    tags(
        (name = "rest", description = "REST endpoints"),
        (name = "websocket", description = "WebSocket endpoint")
    ),
    info(
        title = "Axum Demo Server",
        version = "0.1.0",
        description = "Production-style HTTP + WebSocket server built with Axum.\n\n\
            Replaces the hand-rolled TCP/HTTP/WS server with industry-standard crates.\n\n\
            ## Endpoints\n\
            - `GET /` — welcome message\n\
            - `GET /health` — health check\n\
            - `POST /echo` — echo posted JSON\n\
            - `GET /ws` — WebSocket echo"
    )
)]
pub struct ApiDoc;

/// Build the Swagger UI + OpenAPI JSON routes for Axum.
///
/// This creates two routes:
/// - `GET /docs` → Swagger UI (interactive HTML page)
/// - `GET /api-docs/openapi.json` → raw OpenAPI JSON spec
pub fn swagger_ui() -> SwaggerUi {
    SwaggerUi::new("/docs")
        .url("/api-docs/openapi.json", ApiDoc::openapi())
}
