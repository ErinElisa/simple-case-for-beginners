// if (condition) {
     //  block of code to be executed if the condition is true
// }

let number = 20;
let teks;
if (number > 10) {
    teks = "More than 10";
}
console.log(teks)

// if (condition) {
    //  block of code to be executed if the condition is true
// } else {
    //  block of code to be executed if the condition is false
// }

let number2 = 20;
let teks2;
if (number2 < 10) {
    teks2 = "More than 10";
} else {
    teks2 = "Less than 10";
}
console.log(teks2)


// if (condition1) {
    //  block of code to be executed if condition1 is true
// } else if (condition2) {
    //  block of code to be executed if the condition1 is false and condition2 is true
// } else {
    //  block of code to be executed if the condition1 is false and condition2 is false
// }

let number3 = 10;
let teks3;
if (number3 < 10) {
    teks3 = "More than 10";
} else if (number3 < 20) {
    teks3 = "Less than 10";
} else {
    teks3 = "Hello World";
}
console.log(teks3)