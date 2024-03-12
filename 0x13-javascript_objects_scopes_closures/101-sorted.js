#!/usr/bin/node
const diction = require('./101-data').dict;
const newDict = {};

Object.keys(diction).map(function (key, index) {
  if (newDict[diction[key]] === undefined) {
    newDict[diction[key]] = [];
  }
  newDict[diction[key]].push(key);
});

console.log(newDict);
