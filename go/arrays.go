// Arrays in Go
// An array is a fixed-size sequence of elements of the same type.
// The size of an array is part of its type, which means that arrays cannot be resized.

package main

import (
	"fmt"
)

func main() {
	// Define an array with specific size and default values (zero values)
	var arr1 [5]int
	fmt.Println("arr1:", arr1) // Output: [0 0 0 0 0]

	// Define an array with specific size and initial values
	var arr2 = [5]int{1, 2, 3, 4, 5}
	fmt.Println("arr2:", arr2) // Output: [1 2 3 4 5]

	// Define an array without specifying the size (size inferred from the number of initial values)
	var arr3 = [...]int{1, 2, 3}
	fmt.Println("arr3:", arr3) // Output: [1 2 3]

	// Define an array with specific size and partial initial values (remaining elements are zero values)
	var arr4 = [5]int{1, 2}
	fmt.Println("arr4:", arr4) // Output: [1 2 0 0 0]

	// Define an array using a short variable declaration
	arr5 := [3]string{"Go", "Python", "Java"}
	fmt.Println("arr5:", arr5) // Output: [Go Python Java]

	// Define an array with specific size and initial values using index
	arr6 := [5]int{0: 10, 4: 20}
	fmt.Println("arr6:", arr6) // Output: [10 0 0 0 20]
}
