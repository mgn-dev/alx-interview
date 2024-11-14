#!/usr/bin/node

const request = require('request');

// Get the Movie ID from command line arguments
const movieId = process.argv[2];

if (!movieId || isNaN(movieId) || movieId < 1 || movieId > 6) {
  console.log('Please provide a valid Movie ID (1-6).');
  process.exit(1);
}

// Function to fetch characters from the specified movie
const fetchCharacters = (id) => {
  // Construct the URL for the films endpoint
  const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

  // Make a request to the Star Wars API for the movie
  request(url, { json: true }, (err, res, body) => {
    if (err) {
      console.error('Error fetching movie data:', err.message);
      return;
    }

    // Check if the movie has characters
    if (body && body.characters) {
      // Fetch each character
      body.characters.forEach(characterUrl => {
        request(characterUrl, { json: true }, (err, res, characterBody) => {
          if (err) {
            console.error('Error fetching character data:', err.message);
            return;
          }
          console.log(characterBody.name);
        });
      });
    } else {
      console.log('No characters available for this movie.');
    }
  });
};

// Call the function to fetch characters
fetchCharacters(movieId);
