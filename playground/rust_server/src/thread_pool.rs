use std::sync::{mpsc, Arc, Mutex};
use std::thread;

/// A closure that can be sent across threads and executed once.
/// `Box` puts it on the heap (closures have unknown sizes, so we
/// can't store them directly — we need a pointer).
/// `dyn FnOnce()` means "a type that implements FnOnce()" (dynamic dispatch).
/// `Send` means "safe to transfer ownership between threads."
/// `'static` means "doesn't borrow any short-lived data."
type Job = Box<dyn FnOnce() + Send + 'static>;

pub struct ThreadPool {
    workers: Vec<Worker>,
    sender: Option<mpsc::Sender<Job>>,
}

struct Worker {
    id: usize,
    thread: Option<thread::JoinHandle<()>>,
}

impl ThreadPool {
    /// Create a new ThreadPool.
    ///
    /// `size` is the number of worker threads. Must be > 0.
    ///
    /// # Panics
    /// Panics if `size` is 0.
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0, "ThreadPool size must be greater than 0");

        // Create the channel: sender stays with the pool,
        // receiver is shared among workers via Arc<Mutex<>>
        let (sender, receiver) = mpsc::channel();
        let receiver = Arc::new(Mutex::new(receiver));

        let mut workers = Vec::with_capacity(size);
        for id in 0..size {
            // Arc::clone increments the reference count (atomic operation)
            // but doesn't clone the underlying Receiver — all workers
            // share the same Receiver behind the same Mutex.
            workers.push(Worker::new(id, Arc::clone(&receiver)));
        }

        ThreadPool {
            workers,
            sender: Some(sender),
        }
    }

    /// Send a closure to be executed by a worker thread.
    pub fn execute<F>(&self, f: F)
    where
        F: FnOnce() + Send + 'static,
    {
        let job = Box::new(f);
        // send() can only fail if the receiver has been dropped.
        // We only drop the receiver in Drop, so this is safe.
        self.sender.as_ref().unwrap().send(job).unwrap();
    }
}

impl Drop for ThreadPool {
    fn drop(&mut self) {
        // Drop the sender. When all senders are gone, the channel closes,
        // and workers' recv() calls return Err, causing them to exit their loop.
        drop(self.sender.take());

        for worker in &mut self.workers {
            println!("Shutting down worker {}", worker.id);
            // take() replaces thread with None, giving us ownership of the JoinHandle
            if let Some(thread) = worker.thread.take() {
                thread.join().unwrap();
            }
        }
    }
}

impl Worker {
    fn new(id: usize, receiver: Arc<Mutex<mpsc::Receiver<Job>>>) -> Worker {
        // move || captures receiver by moving ownership into the closure.
        // Without 'move', the closure would borrow receiver, but the borrow
        // can't outlive the Worker::new function. 'move' gives the closure
        // its own Arc<Mutex<Receiver>> that lives as long as the thread.
        let thread = thread::spawn(move || {
            loop {
                // Lock the mutex, then call recv().
                // The mutex is held only during the lock+recv call —
                // it's dropped at the end of this let statement.
                // If recv() blocks (no jobs available), the mutex is NOT held
                // while waiting, so other workers can receive jobs.
                let job = {
                    let receiver = receiver.lock().unwrap();
                    receiver.recv()
                };

                match job {
                    Ok(job) => {
                        println!("Worker {id} executing a job.");
                        job();
                    }
                    Err(_) => {
                        // Channel closed (sender dropped) — time to shut down
                        println!("Worker {id} shutting down.");
                        break;
                    }
                }
            }
        });

        Worker {
            id,
            thread: Some(thread),
        }
    }
}
