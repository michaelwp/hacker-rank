/*
 * Complete the 'rotateLeft' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER d
 *  2. INTEGER_ARRAY arr
 */

function rotateLeft(d, arr) {
    // Write your code here
    const newPos = [];

    for (let i=0; i < arr.length; i++) {
        let n = i - d;

        if (n < 0) {
            n += arr.length
        }

        newPos[n] = arr[i];
    }

    return newPos;
}

const d = 4;
const arr = [1, 2, 3, 4, 5];

console.log(rotateLeft(d, arr));