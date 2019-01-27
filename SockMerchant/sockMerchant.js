'use strict';
function sockMerchant(n, ar) {
    let c = {};
    let d = 0;
    ar.forEach(e => {
        ar.forEach(f => {
            if (e == f) {
                d++;
            }
        });

        if (d > 1) {
            if ((d % 2) != 0) {
                d -= 1;
            }
            d /= 2;
            c[e] = d;
        }
        d = 0;
    });

    let r = 0;
    let _;
    for (_ in c) {
        r += c[_];
    }
    return r;
}

//test case
let n = 9
let arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]
//arr = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]

console.log(sockMerchant(n, arr));