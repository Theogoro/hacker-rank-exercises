// https://www.hackerrank.com/challenges/strange-advertising/problem
'use strict';

import { WriteStream, createWriteStream } from "fs";
process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString: string = '';
let inputLines: string[] = [];
let currentLine: number = 0;

process.stdin.on('data', function(inputStdin: string): void {
    inputString += inputStdin;
});

process.stdin.on('end', function(): void {
    inputLines = inputString.split('\n');
    inputString = '';

    main();
});

function readLine(): string {
    return inputLines[currentLine++];
}

/*
 * Complete the 'viralAdvertising' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER n as parameter.
 */

function viralAdvertising(n: number): number {
    let acc = 0;
    let recipients = 5;
    const SHARES_EACH_RECIPENT = 3
    
    for (let i = 1; i <= n; i++) {
        console.log({
            day: i,
            liked: likes(recipients),
            recipients
        })
        acc += likes(recipients);
        
        recipients = likes(recipients) * SHARES_EACH_RECIPENT;
    }
    
    return acc;
}

function likes(recipients: number): number {
    return Math.floor(recipients / 2);
}

function main() {
    const ws: WriteStream = createWriteStream(process.env['OUTPUT_PATH']);

    const n: number = parseInt(readLine().trim(), 10);

    const result: number = viralAdvertising(n);

    ws.write(result + '\n');

    ws.end();
}
