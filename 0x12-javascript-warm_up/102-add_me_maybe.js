#!/usr/bin/node
function addMe (number, theFunction) {
  theFunction(++number);
}
exports.addMeMaybe = addMe;
