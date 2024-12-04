import redis from 'redis';
import { promisify } from 'util';

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

const promisifyGet = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
  try {
    const reply = await promisifyGet(schoolName);
    console.log(reply);
  } catch (err) {
    throw new Error(err);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
