use axum::extract::ws::{Message, WebSocket, WebSocketUpgrade};
use axum::response::IntoResponse;

/// GET /ws — WebSocket upgrade endpoint.
///
/// `WebSocketUpgrade` is an Axum extractor that checks for the
/// required WebSocket headers. If present, it returns a 101 Switching Protocols.
/// If absent, Axum responds with 426 Upgrade Required (optional, via `on_failed_upgrade`).
#[utoipa::path(
    get,
    path = "/ws",
    responses(
        (status = 101, description = "WebSocket upgrade successful"),
        (status = 426, description = "Not a WebSocket request")
    )
)]
pub async fn ws_handler(ws: WebSocketUpgrade) -> impl IntoResponse {
    ws.on_upgrade(move |socket| handle_ws(socket))
}

/// The actual WebSocket connection loop — runs on the connection's task.
///
/// Each WebSocket connection gets its own tokio task (lightweight green thread).
/// This is the async equivalent of our hand-rolled thread pool from the
/// from-scratch server — but tokio multiplexes thousands of these tasks
/// onto a small number of OS threads.
async fn handle_ws(mut socket: WebSocket) {
    tracing::info!("WebSocket connected");

    loop {
        match socket.recv().await {
            Some(Ok(Message::Text(text))) => {
                tracing::debug!("WS received: {}", text);
                let reply = format!("Echo: {}", text);
                if socket.send(Message::Text(reply.into())).await.is_err() {
                    break; // client disconnected
                }
            }
            Some(Ok(Message::Ping(data))) => {
                // Axum can auto-pong, but handling it ourselves is explicit
                if socket.send(Message::Pong(data)).await.is_err() {
                    break;
                }
            }
            Some(Ok(Message::Pong(_))) => {
                // Received pong — client responded to our ping, nothing to do
            }
            Some(Ok(Message::Close(_))) => {
                tracing::info!("WS close frame — shutting down");
                let _ = socket.send(Message::Close(None)).await;
                break;
            }
            Some(Ok(Message::Binary(data))) => {
                let _ = socket
                    .send(Message::Text(
                        format!("Binary echo ({} bytes)", data.len()).into(),
                    ))
                    .await;
            }
            Some(Err(e)) => {
                tracing::error!("WS protocol error: {}", e);
                break;
            }
            None => {
                tracing::info!("WS stream ended");
                break;
            }
        }
    }

    tracing::info!("WebSocket disconnected");
}
