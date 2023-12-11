#!/usr/bin/node
const argv = process.argv;
if (argv[2]) {
  console.log(factorial(parseFloat(argv[2])));
} else {
  console.log(factorial(0));
}

function factorial (input) {
  if (input === 1 || input === 0) {
    return (1);
  }
  return (input * factorial(input - 1));
}
