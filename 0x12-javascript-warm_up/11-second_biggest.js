#!/usr/bin/node
const argv = process.argv.slice(2).map(Number);
if (argv.length < 2) {
  console.log(0);
} else {
  const arr = argv.sort();
  console.log(arr[arr.length - 2]);
}
