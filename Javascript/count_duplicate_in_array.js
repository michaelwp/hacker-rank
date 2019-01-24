function numDuplicates(names, prices, weights) {
    x = [];
    
    for (i in names){
        x.push(names[i]+String(prices[i])+String(weights[i]));
    }

    res = [];
    d = 0;
    r = 0;
    x.forEach(ye => {
        x.forEach(xe => {
            if (xe === ye){
                d++;
            }
        });
        
        if (d > 1){
            res[ye]=d;
        }
        d=0;
    });

    for (e in res){
        r = r + (res[e]);
    }

    return r;
}

n = ['ball','ball','mango','coconut','mango','mango'];
p = [1,1,2,3,2,2];
w = [1,1,3,2,3,3];
console.log(numDuplicates(n, p, w));