#!/usr/bin/node

// Import the request module
const request = require('request');

// Get the Movie ID from the first positional argument
const movieID = process.argv[2];

// Base URL for the Star Wars API
const apiUrl = `https://swapi.dev/api/films/${movieID}/`;

// Make an HTTP GET request to the Star Wars API to fetch the movie data
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Parse the JSON response body
  const data = JSON.parse(body);

  // Ensure the movie data exists
  if (!data.characters) {
    console.error('Invalid Movie ID');
    return;
  }

  // Iterate through the character URLs
  data.characters.forEach((characterUrl) => {
    // Make an HTTP GET request to fetch each character's data
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error:', charError);
        return;
      }

      // Parse the character data and print the name
      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
    });
  });
});
