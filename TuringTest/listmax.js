
function listMax(n, operations){
    //Please write your code here.
    let x = [];
    for (i=0; i<n; i++){
        x.push(0);
    }

    for (j=0; j<operations.length; j++){
        jx = operations[j].length;
        for (q=0; q<(jx-1); q++){
            jn = operations[j][jx-1];
            x[(operations[j][q])-1] += jn;
        }
    }
    
    let max_num = 0;
    for (r=0; r<(x.length-1); r++){
        if (x[r] > max_num){
            max_num = x[r];
        };
    }
    return(max_num);
}

let n = 5;
let operations = [[1, 2, 100],[2, 5, 100], [3, 4, 100]];
console.log(listMax(n, operations));