#!/usr/bin/node
const argv = process.argv;
if (parseFloat(argv[2])) {
  for (let i = 0; i < argv[2]; i++) {
    console.log('X'.repeat(argv[2]));
  }
} else {
  console.log('Missing size');
}
