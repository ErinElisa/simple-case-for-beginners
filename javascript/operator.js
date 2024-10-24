// 1. Assignment Operators
let a = 5;   // Assign 5 to a
let b = 10;  // Assign 10 to b

// Compound assignment
a += 2;      // a = a + 2 -> a is now 7
b *= 2;      // b = b * 2 -> b is now 20
a -= 3;      // a = a - 3 -> a is now 4
b /= 4;      // b = b / 4 -> b is now 5
a %= 3;      // a = a % 3 -> a is now 1 (remainder of 4/3)

// 2. Arithmetic Operators
let x = 8;
let y = 2;

let add = x + y;   // Addition -> 10
let sub = x - y;   // Subtraction -> 6
let mul = x * y;   // Multiplication -> 16
let div = x / y;   // Division -> 4
let mod = x % y;   // Modulus (remainder) -> 0
let exp = x ** y;  // Exponentiation -> 64 (8^2)

console.log("Arithmetic Operators:");
console.log("Addition: " + add);
console.log("Subtraction: " + sub);
console.log("Multiplication: " + mul);
console.log("Division: " + div);
console.log("Modulus: " + mod);
console.log("Exponentiation: " + exp);

// 3. Comparison Operators
let isEqual = a == b;      // Equal -> false
let isNotEqual = a != b;   // Not equal -> true
let isGreater = a > b;     // Greater than -> false
let isLess = a < b;        // Less than -> true
let isGreaterOrEqual = a >= 5;  // Greater than or equal to -> true
let isLessOrEqual = b <= 8;     // Less than or equal to -> true

let strictEqual = a === 5;  // Strict equality (checks type too) -> true
let strictNotEqual = b !== "8";  // Strict inequality (checks type too) -> true

console.log("Comparison Operators:");
console.log("Equal: " + isEqual);
console.log("Not Equal: " + isNotEqual);
console.log("Greater than: " + isGreater);
console.log("Less than: " + isLess);
console.log("Greater or Equal: " + isGreaterOrEqual);
console.log("Less or Equal: " + isLessOrEqual);
console.log("Strict Equal: " + strictEqual);
console.log("Strict Not Equal: " + strictNotEqual);

// 4. Logical Operators
let bool1 = true;
let bool2 = false;

let andResult = bool1 && bool2;  // Logical AND -> false (true && false)
let orResult = bool1 || bool2;   // Logical OR -> true (true || false)
let notResult = !bool1;          // Logical NOT -> false (!true)

console.log("Logical Operators:");
console.log("Logical AND: " + andResult);
console.log("Logical OR: " + orResult);
console.log("Logical NOT: " + notResult);

// 5. Increment/Decrement Operators
let count = 5;

count++;  // Increment -> 6
count--;  // Decrement -> 5

// Pre-increment and Post-increment
let preInc = ++count;  // Pre-increment -> count is now 6
let postInc = count++; // Post-increment -> postInc is 6, count is now 7

console.log("Increment/Decrement Operators:");
console.log("Pre-Increment: " + preInc);
console.log("Post-Increment: " + postInc);

// 6. Ternary (Conditional) Operator
let age = 18;
let canVote = (age >= 18) ? "Yes, you can vote!" : "No, too young.";  
console.log("Ternary Operator (Can Vote): " + canVote);

// 7. Bitwise Operators
let bitA = 5;  // 0101 in binary
let bitB = 3;  // 0011 in binary

let bitAnd = bitA & bitB;  // Bitwise AND -> 1 (0001)
let bitOr = bitA | bitB;   // Bitwise OR -> 7 (0111)
let bitXor = bitA ^ bitB;  // Bitwise XOR -> 6 (0110)
let bitNot = ~bitA;        // Bitwise NOT -> -6
let leftShift = bitA << 1; // Left shift -> 10 (1010)
let rightShift = bitA >> 1;// Right shift -> 2 (0010)

console.log("Bitwise Operators:");
console.log("Bitwise AND: " + bitAnd);
console.log("Bitwise OR: " + bitOr);
console.log("Bitwise XOR: " + bitXor);
console.log("Bitwise NOT: " + bitNot);
console.log("Left Shift: " + leftShift);
console.log("Right Shift: " + rightShift);

// 8. Typeof Operator
let num = 42;
let text = "Hello";
let isNull = null;

console.log("Typeof Operator:");
console.log("Type of num: " + typeof num);    // "number"
console.log("Type of text: " + typeof text);  // "string"
console.log("Type of isNull: " + typeof isNull); // "object" (due to legacy reasons in JavaScript)

// 9. Instanceof Operator
let today = new Date();
console.log("Instanceof Operator:");
console.log("today instanceof Date: " + (today instanceof Date));  // true

// 10. Spread Operator
let arr1 = [1, 2, 3];
let arr2 = [...arr1, 4, 5];  // Combine arrays -> [1, 2, 3, 4, 5]

let obj1 = {a: 1, b: 2};
let obj2 = {...obj1, c: 3};  // Combine objects -> {a: 1, b: 2, c: 3}

console.log("Spread Operator:");
console.log("Combined Array: " + arr2);
console.log("Combined Object:", obj2);
