// In Go, there is only one looping construct: the `for` loop.
// However, it can be used in various ways to achieve different looping behaviors.

package main

import (
	"fmt"
)

func main() {

	// Basic `for` loop
	for i := 0; i < 5; i++ {
		// This loop will run 5 times, with `i` taking values from 0 to 4
		fmt.Println(i)
	}

	// `for` loop as a while loop
	n := 0
	for n < 5 {
		// This loop will run as long as `n` is less than 5
		fmt.Println(n)
		n++
	}

	// Infinite `for` loop
	for {
		// This loop will run forever unless a `break` statement is encountered
		fmt.Println("Infinite loop")
		break // This will break the loop and prevent it from running infinitely
	}

	// `for` loop with `range` to iterate over a slice
	numbers := []int{1, 2, 3, 4, 5}
	for index, value := range numbers {
		// This loop will iterate over each element in the slice `numbers`
		// `index` is the index of the element, and `value` is the value of the element
		fmt.Printf("Index: %d, Value: %d\n", index, value)
	}

	// `for` loop with `range` to iterate over a map
	personAge := map[string]int{"Alice": 25, "Bob": 30}
	for key, value := range personAge {
		// This loop will iterate over each key-value pair in the map `personAge`
		// `key` is the key of the map, and `value` is the value associated with the key
		fmt.Printf("Key: %s, Value: %d\n", key, value)
	}

	// `for` loop with `range` to iterate over a string
	str := "hello"
	for index, char := range str {
		// This loop will iterate over each character in the string `str`
		// `index` is the index of the character, and `char` is the character itself
		fmt.Printf("Index: %d, Character: %c\n", index, char)
	}
}
