// The break statement "jumps out" of a loop.

let text;
for (let i = 0; i < 10; i++) {
    if (i === 5) { 
        break; 
    }
    text += "The number is " + i + "\n";
}
console.log(text)

// The continue statement "jumps over" one iteration in the loop.

let text2;
for (let i = 0; i < 10; i++) {
    if (i === 5) { 
        continue; 
    }
    text2 += "The number is " + i + "\n";
}
console.log(text2)