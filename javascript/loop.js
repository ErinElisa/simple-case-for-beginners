//simple array
const array = [1, 2, 3]

//loop using for
for (const a of array) {
    //print in the console
    console.log(a)
}

//loop using foreach
array.forEach(a => {
    //print in the console
    console.log(a)
});

//for array 2 dimension
const array2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

//loop using for
for (const a of array2d) {
    //loop again for access next array
    for (const b of a) {
        //print in the console
        console.log(b)
    }
}

//loop using foreach
array2d.forEach(a => {
    //loop again for access next array
    a.forEach(b => {
        //print in the console
        console.log(b)
    });
});


