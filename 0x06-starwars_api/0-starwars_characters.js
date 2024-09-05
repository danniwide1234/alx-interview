#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const filmUrl = 'https://swapi-api.hbtn.io/api/films/' + filmId;
let characterUrls = [];
const characterNames = [];

const fetchCharacterUrls = async () => {
  return new Promise((resolve, reject) => {
    request(filmUrl, (error, response, body) => {
      if (error || response.statusCode !== 200) {
        console.error('Error: ', error, '| StatusCode: ', response.statusCode);
        reject();
      } else {
        const data = JSON.parse(body);
        characterUrls = data.characters;
        resolve();
      }
    });
  });
};

const fetchCharacterNames = async () => {
  if (characterUrls.length > 0) {
    for (const url of characterUrls) {
      await new Promise((resolve, reject) => {
        request(url, (error, response, body) => {
          if (error || response.statusCode !== 200) {
            console.error('Error: ', error, '| StatusCode: ', response.statusCode);
            reject();
          } else {
            const data = JSON.parse(body);
            characterNames.push(data.name);
            resolve();
          }
        });
      });
    }
  } else {
    console.error('Error: Got no Characters for some reason');
  }
};

const displayCharacterNames = async () => {
  await fetchCharacterUrls();
  await fetchCharacterNames();

  // Print each name on a new line
  for (const name of characterNames) {
    console.log(name);
  }
};

displayCharacterNames();
