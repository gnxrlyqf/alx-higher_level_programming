#!/usr/bin/node
function add_me(number, theFunction) {
  theFunction(++number);
};
exports.addMeMaybe = add_me;
