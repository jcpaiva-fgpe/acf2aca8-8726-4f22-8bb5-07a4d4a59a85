/********************************************************
 *              DO NOT TOUCH AREA: START                *
 ********************************************************/

function main() {
    const arr = [];
    let n;
    do {
        n = parseInt(readln(), 10);
        if (n >= 0) {
            arr.push(n);
        }
    } while(n >= 0);
    const [min, max] = minMax(arr);
    writeln(min);
    writeln(max);
}

/********************************************************
 *                DO NOT TOUCH AREA: END                *
 ********************************************************/

{{code}}
