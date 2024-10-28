// Functions in Rust
// Functions are a way to encapsulate code into reusable blocks. They can take parameters and return values.
// Functions are defined using the `fn` keyword followed by the function name and a set of parentheses.

fn main() {
    // The main function is the entry point of a Rust program.
    println!("Hello, world!");

    // Calling a function without parameters and without return value
    greet();

    // Calling a function with parameters
    let sum = add(5, 10);
    println!("Sum: {}", sum);

    // Calling a function with a return value
    let square = square(4);
    println!("Square: {}", square);

    // Calling a function with a mutable reference
    let mut number = 5;
    increment(&mut number);
    println!("Incremented number: {}", number);
}

// A simple function that prints a greeting message
fn greet() {
    println!("Hello from the greet function!");
}

// A function that takes two integers as parameters and returns their sum
fn add(a: i32, b: i32) -> i32 {
    a + b
}

// A function that takes an integer and returns its square
fn square(x: i32) -> i32 {
    x * x
}

// A function that takes a mutable reference to an integer and increments it
fn increment(num: &mut i32) {
    *num += 1;
}