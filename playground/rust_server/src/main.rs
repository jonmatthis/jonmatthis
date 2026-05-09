use std::io::{Read, Write};
use std::net::{TcpListener, TcpStream};

mod http;
mod ws;
mod thread_pool;

fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878")
        .expect("Failed to bind to 127.0.0.1:7878");

    let pool = thread_pool::ThreadPool::new(4);
    println!("Server listening on 127.0.0.1:7878 (4 workers)");

    for stream in listener.incoming() {
        match stream {
            Ok(stream) => {
                println!("Connection from {}", stream.peer_addr().unwrap());
                pool.execute(move || {
                    handle_connection(stream);
                });
            }
            Err(e) => eprintln!("Connection failed: {}", e),
        }
    }
}

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
    use ws::frame::{WsFrame, OP_CLOSE, OP_PING, OP_PONG, OP_TEXT};

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

                // Try to decode complete frames from the accumulated buffer
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
                            println!("WS close frame received");
                            return;
                        }
                        _ => {}
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
