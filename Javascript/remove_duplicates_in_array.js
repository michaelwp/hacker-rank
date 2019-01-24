function remDuplicates(arr) {
    r = [];

    arr.forEach(element => {
        r[element]=0;
    });

    y = [];
    for (i in r){
        y.push(i);
    }
    
    return y;
}

arr = ['ball','ball','mango','coconut','mango','mango'];
console.log(remDuplicates(arr));