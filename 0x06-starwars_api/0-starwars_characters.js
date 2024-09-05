#!/usr/bin/node
/* Prints all Casts of Star Wars movie
Read the README.md file for more info
*/

const request = require('request');
const apiBaseUrl = 'https://swapi-api.alx-tools.com/api/';
const filmsEndpoint = 'films/';
const filmId = process.argv[2].toString();

request(apiBaseUrl + filmsEndpoint + filmId, function (err, _, responseBody) {
  if (err) console.error(err);
  const filmData = JSON.parse(responseBody);
  const characters = filmData.characters;
  displayCharacterNames(characters);
});

/* Recursively and synchronously request each character
and print out the character names */
function displayCharacterNames (characterUrls, index = 0) {
  request(characterUrls[index], function (err, _, responseBody) {
    if (err) console.error(err);
    console.log(JSON.parse(responseBody).name);
    if (++index < characterUrls.length) {
      displayCharacterNames(characterUrls, index);
    }
  });
}
