#!/usr/bin/node
const argv = process.argv;
console.log(factorial(parseFloat(argv[2])));

function factorial (input) {
  if (input === 1 || input === 0) {
    return (1);
  }
  return (input * factorial(input - 1));
}
