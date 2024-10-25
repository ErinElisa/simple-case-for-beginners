/*
A function in C++ is a block of code that performs a specific task. It is defined with a name and can be called (invoked) from other parts of the program. Functions help in organizing code, making it reusable, and improving readability.

Terms to know:
    - function data type
    - parameters & arguements
    - return type

In C++ functions can be defined in 2 ways:
1. Function prototyping
2. Function definition

Below is an example of a simple function in C++ that adds two integers and returns the result.
*/

#include <iostream>
// Add this line to include all the identifiers from the `std` namespace to the global namespace
using namespace std;

/*   ==============   */

/*
Example 1: Function Prototyping
First a declaration for the function is made (line 28) and then it is defined (line 46)
*/


// Function declaration (prototype)
int add(int a, int b);

// Main function where the program execution begins
int main() {
    int num1 = 5;
    int num2 = 3;

    // Calling the add function and storing the result in sum
    int sum = add(num1, num2);

    // Printing the result
    cout << "The sum is: " << sum << endl;

    return 0;
}

// Function definition
// This function takes two integers as parameters and returns their sum
int add(int a, int b) {
    return a + b;
}

/*   ==============   */

/*
Example 2: Function Definition
Function is directly defined in the first place. You need to make sure that the function is defined before the main function
so that it is usable.
*/

int add(int a, int b) {
    return a + b;
}

int main() {
    int num1 = 5;
    int num2 = 3;

    // Calling the add function and storing the result in sum
    int sum = add(num1, num2);

    // Printing the result
    cout << "The sum is: " << sum << endl;

    return 0;
}
