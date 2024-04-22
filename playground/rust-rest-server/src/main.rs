use actix_web::{get, post, web, App, HttpResponse, HttpServer, Responder};
use serde::{Deserialize, Serialize};
use std::sync::Mutex; // New import for thread-safe data sharing
use std::{fs, io};

#[derive(Deserialize, Serialize, Clone)]
struct User {
    name: String,
    age: u8,
}

#[get("/")]
async fn index() -> impl Responder {
    HttpResponse::Ok().body("Hello world!")
}

#[get("/users")]
async fn get_users(data: web::Data<Mutex<Vec<User>>>) -> impl Responder {
    let users = data.lock().unwrap();
    web::Json(users.clone()) // Clone the data to send as JSON
}
#[post("/users")]
async fn create_user(user: web::Json<User>, data: web::Data<Mutex<Vec<User>>>) -> impl Responder {
    let mut users = data.lock().unwrap();
    users.push(user.into_inner()); // Add the new user to the shared user list
    // Save updated users back to a file
    save_users_to_file(&users).expect("Failed to save users");
    HttpResponse::Ok().body("User created")
}

#[actix_web::main]
async fn main() -> io::Result<()> {
    let users = load_users_from_file().expect("Failed to load users");

    let users_data = web::Data::new(Mutex::new(users)); // Share users across threads
    HttpServer::new(move || {
        App::new()
            .app_data(users_data.clone()) // Clone `Data` so each worker gets a reference
           .service(index)
           .service(get_users)
           .service(create_user)
    })
   .bind("127.0.0.1:8080")?
   .run()
   .await
}

fn load_users_from_file() -> Result<Vec<User>, io::Error> {
    let data = fs::read_to_string("users.json").unwrap_or_else(|_| "[]".to_string());
    let users: Vec<User> = serde_json::from_str(&data)?;
    Ok(users)
}

fn save_users_to_file(users: &Vec<User>) -> Result<(), io::Error> {
    let data = serde_json::to_string(users)?;
    fs::write("users.json", data)?;
    Ok(())
}