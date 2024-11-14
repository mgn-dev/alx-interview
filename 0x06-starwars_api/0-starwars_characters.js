#!/usr/bin/node

// Import the request module for making HTTP requests
const request = require('request');

// Make a request to the Star Wars API to fetch movie details using the movie ID from command line arguments
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, body) {
  // Handle any request errors
  if (err) throw err;

  // Parse the response body to extract the characters' URLs
  const actors = JSON.parse(body).characters;

  // Call the exactOrder function to print character names in the order they appear
  exactOrder(actors, 0);
});

// Function to recursively fetch and print character names in order
const exactOrder = (actors, x) => {
  // Base case: if the index 'x' equals the length of the actors array, exit the function
  if (x === actors.length) return;

  // Make a request to fetch details of the character at the current index
  request(actors[x], function (err, res, body) {
    // Handle any request errors
    if (err) throw err;

    // Parse the response body to get the character details and print the character's name
    console.log(JSON.parse(body).name);

    // Recursively call the exactOrder function for the next character
    exactOrder(actors, x + 1);
  });
};
