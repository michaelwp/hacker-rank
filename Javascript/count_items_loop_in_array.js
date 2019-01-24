function numDuplicates(arr) {
    res = {};
    d = 0;
    arr.forEach(ye => {
        arr.forEach(xe => {
            if (xe === ye){
                d++;
            }
        });
        res[ye]=d;
        d=0;
    });
    return res;
}

n = ['ball','ball','mango','coconut','mango','mango'];
console.log(numDuplicates(n));