//simple array
const array = [1, 2, 3]

//using map for get the all value
array.map( a =>{
    //print all value in console
    console.log(a)
})

//array 2 dimension
const array2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

//using map for get the all value array 2 dimension
array2d.map(row => {
    //map again for access next array
    row.map(element => {
        //print all value in console
        console.log(element);
    });
});