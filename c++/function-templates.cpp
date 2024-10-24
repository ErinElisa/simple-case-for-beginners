/*
    The simple idea is to pass the data type as a parameter so that 
    we don’t need to write the same code for different data types. 
    For example, a software company may need to sort() for different data types. 
    Rather than writing and maintaining multiple codes, 
    we can write one sort() and pass the datatype as a parameter.
*/

// Include the standard library for c++ iostream
#include <iostream>

// Add this line to include all the identifiers from the `std` namespace to the global namespace
using namespace std;

/*
Example:
*/

// Function template definition
template <typename T>
T add(T a, T b) {
    // Return the sum of a and b
    return a + b;
}

// Testing out our function template with different data types
int main() {
    // Test the function template with int
    int intResult = add(3, 4);
    cout << "Sum of integers: " << intResult << endl;

    // Test the function template with double
    double doubleResult = add(3.5, 4.5);
    cout << "Sum of doubles: " << doubleResult << endl;

    return 0;
}