/********************************************************
 *              DO NOT TOUCH AREA: START                *
 ********************************************************/

function main() {
    let ln;
    while((ln = readln()).indexOf(' ') >= 0) {
        const [s, ...ws] = ln.split(' ');
        const addS = add_suffix(s);
        ws.forEach(w => writeln(addS(w)));
    }
}

/********************************************************
 *                DO NOT TOUCH AREA: END                *
 ********************************************************/

{{code}}
