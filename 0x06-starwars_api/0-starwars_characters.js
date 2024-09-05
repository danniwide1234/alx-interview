#!/usr/bin/node
const request = require('request');
const filmId = process.argv[2];
const requestOptions = {
  url: 'https://swapi-api.hbtn.io/api/films/' + filmId,
  method: 'GET'
};

request(requestOptions, function (err, res, data) {
  if (!err) {
    const characterUrls = JSON.parse(data).characters;
    displayCharacterNames(characterUrls, 0);
  }
});

function displayCharacterNames (urls, idx) {
  request(urls[idx], function (err, res, data) {
    if (!err) {
      console.log(JSON.parse(data).name);
      if (idx + 1 < urls.length) {
        displayCharacterNames(urls, idx + 1);
      }
    }
  });
}
