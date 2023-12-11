#!/usr/bin/node
const argv = process.argv;
if (parseFloat(argv[2])) {
  console.log('My number: ' + argv[2]);
} else {
  console.log('Not a number');
}
