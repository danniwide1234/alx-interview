#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const filmUrl = 'https://swapi-api.hbtn.io/api/films/' + filmId;
let characterUrls = [];
const characterNames = [];

const fetchCharacterUrls = async () => {
  await new Promise(resolve => request(filmUrl, (error, response, body) => {
    if (error || response.statusCode !== 200) {
      console.error('Error: ', error, '| StatusCode: ', response.statusCode);
    } else {
      const data = JSON.parse(body);
      characterUrls = data.characters;
      resolve();
    }
  }));
};

const fetchCharacterNames = async () => {
  if (characterUrls.length > 0) {
    for (const url of characterUrls) {
      await new Promise(resolve => request(url, (error, response, body) => {
        if (error || response.statusCode !== 200) {
          console.error('Error: ', error, '| StatusCode: ', response.statusCode);
        } else {
          const data = JSON.parse(body);
          characterNames.push(data.name);
          resolve();
        }
      }));
    }
  } else {
    console.error('Error: Got no Characters for some reason');
  }
};

const displayCharacterNames = async () => {
  await fetchCharacterUrls();
  await fetchCharacterNames();

  for (const name of characterNames) {
    if (name === characterNames[characterNames.length - 1]) {
      process.stdout.write(name);
    } else {
      process.stdout.write(name + '\n');
    }
  }
};

displayCharacterNames();
