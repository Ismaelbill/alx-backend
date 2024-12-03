// import redis from 'redis';

// const client = redis.createClient();

// client.on('connect', (_) => {
//   console.log('Redis client connected to the server');
// });

// client.on('error', (err) =>
//   console.log(
//     `Redis client not connected to the server: Error: Redis connection to ${err.address}:${err.port} failed - ${err.message}`
//   )
// );

// // client.connect();

// function setNewSchool(schoolName, value) {
//   client.set(schoolName, value, redis.print)
// }

// function displaySchoolValue(schoolName) {
//   client.get(schoolName, (_, reply) => {
//     console.log(reply)
//   })
// }

// displaySchoolValue('Holberton');
// setNewSchool('HolbertonSanFrancisco', '100');
// displaySchoolValue('HolbertonSanFrancisco');


import { print, createClient } from 'redis';

const redisClient = createClient();

redisClient.on('error', (error) => {
  console.log(`Redis client not connected to server: ${error.message}`);
  redisClient.quit();
});
redisClient.on('connect', () =>
  console.log('Redis client connected to the server')
);

console.log(redisClient.connected);
/**
 * Set a key-value pair in redis
 * @param {string} schoolName - key
 * @param {string} value      - value
 */
function setNewSchool(schoolName, value) {
  redisClient.set(schoolName, value, print);
}

/**
 * Gets and display the value associated with given key
 * in redis store.
 * @param {string} schoolName - key to search in redis
 */
function displaySchoolValue(schoolName) {
  redisClient.get(schoolName, (_error, value) => {
    if (value) console.log(value);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');