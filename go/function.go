// In Go, a function is a block of code that performs a specific task.
// Functions are defined using the `func` keyword, followed by the function name,
// a list of parameters enclosed in parentheses, and the return type(s).

package main

import (
	"fmt"
)

// Define a function named `add` that takes two integers as parameters and returns an integer.
func add(a int, b int) int {
	// The function body where the logic is implemented.
	// Here, we simply return the sum of the two parameters.
	return a + b
}

// Define the main function, which is the entry point of a Go program.
func main() {
	// Call the `add` function with arguments 3 and 5.
	result := add(3, 5)

	// Print the result to the console.
	fmt.Println("The sum is:", result)
}
