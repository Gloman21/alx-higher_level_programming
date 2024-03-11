#!/usr/bin/node

function factorial (b) {
  if (b < 0) {
    return (-1);
  }
  if (b  === 0 || isNaN(b)) {
    return (1);
  }
  return (b * factorial(b - 1));
}

console.log(factorial(Number(process.argv[2])));
