#!/usr/bin/node

// Write a script that writes a string to a file

const fs = require('fs');

const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Write files using Js
fs.writeFile(filePath, stringToWrite, 'utf8', (err) => {
  if (err) {
   return console.log(err);{
  }
});
