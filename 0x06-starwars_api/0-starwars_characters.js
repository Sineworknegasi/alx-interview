#!/usr/bin/node

const request = require("request");

request(
  "https://swapi-api.hbtn.io/api/films/" + process.argv[2],
  function (err, res, body) {
    if (err) throw err;
    const actors = JSON.parse(body).characters;
    exactord(actors, 0);
  }
);
const exactord = (actors, x) => {
  if (x === actors.length) return;
  request(actors[x], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    exactord(actors, x + 1);
  });
};
