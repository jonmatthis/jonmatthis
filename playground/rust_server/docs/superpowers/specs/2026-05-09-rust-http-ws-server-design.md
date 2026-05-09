# Design: Step-by-Step Rust HTTP + WebSocket Server (From Scratch)

## Goal

Build a multi-threaded HTTP + WebSocket server using only the Rust standard library,
following the Rust Book Chapter 21 pedagogy. Each stage is a working milestone.

## Architecture

```
main.rs ──► server.rs ──► thread_pool.rs
                │
                ├──► http/request.rs
                ├──► http/response.rs
                ├──► http/router.rs
                └──► ws/
                       ├── handshake.rs
                       └── frame.rs
```

## Build Stages

1. **TCP Echo Server** — `TcpListener`, accept loop, read/write
2. **HTTP Request Parser** — parse method, path, headers, body from raw bytes
3. **HTTP Response + Router** — status codes, response builder, route matching
4. **Single-Threaded WebSocket Upgrade** — Upgrade handshake, SHA-1, frame masking
5. **Thread Pool** — `ThreadPool`, `Worker`, `Job` (`Arc<Mutex<mpsc::Receiver>>`)
6. **Multi-Threaded WebSocket Server** — wire pool in, shared WS client state

## Dependencies

Zero external crates. Standard library only.

## Errors

Panic on fatal errors (port bind failure). Log and continue on per-connection errors.
