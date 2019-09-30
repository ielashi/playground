extern crate rand;
use rand::Rng;
use std::io;

fn main() {
  println!("Guess the number!");

  let secret_number = rand::thread_rng().gen_range(1, 101);

  loop {
    println!("Please input your guess.");

    let mut guess = String::new();
    io::stdin()
      .read_line(&mut guess)
      .expect("Failed to read line.");

    let guess: i32 = match guess.trim().parse() {
      Ok(num) => num,
      Err(_) => continue,
    };

    if guess == secret_number {
      println!("You win!");
      break;
    } else if guess > secret_number {
      println!("Lower");
    } else {
      println!("Higher");
    }
  }
}
