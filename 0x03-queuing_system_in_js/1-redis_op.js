import redis from 'redis';

const client = redis.createClient();

client.on('connect', (_) => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) =>
  console.log(
    `Redis client not connected to the server: Error: Redis connection to ${err.address}:${err.port} failed - ${err.message}`
  )
);

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (_, reply) => {
    console.log(reply);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
