// function name(parameter1, parameter2, parameter3) {
//     // code to be executed
// }



// Not using paramenter
// Function is called, the return value will end up in namePerson
let namePerson = name();

function name(){
// Function returns the name Chriss
    return 'Chriss';
}

console.log(namePerson)

// Using paramenter
// Function is called, the return value will end up in x
let x = myFunction(10, 5);

function myFunction(a, b) {
// Function returns the product of a and b
  return a * b;
}

console.log(x)