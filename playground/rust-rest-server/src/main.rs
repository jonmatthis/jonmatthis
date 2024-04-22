use actix_web::{get, post, web ,App, HttpResponse, HttpServer, Responder};
use::serde::{Deserialize, Serialize};

#[derive(Deserialize, Serialize)]
struct User {
    name: String,
    age: u8,
}

#[get("/")]
async fn index() -> impl Responder {
    HttpResponse::Ok().body("Hello world!")
}

#[get("/users")]
async fn get_users() -> impl Responder {
    let users = vec![
        User {
            name: "John".to_string(),
            age: 20,
        },
        User {
            name: "Jane".to_string(),
            age: 21,
            },
    ];

    web::Json(users)
}

#[post("/users")]
async fn create_user(user: web::Json<User>) -> impl Responder {
    HttpResponse::Ok().body(format!("User {} created", user.name))
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    