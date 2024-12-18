import { channel } from 'diagnostics_channel';
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

client.subscribe('holberton school channel');

client.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    client.unsubscribe();
    client.quit();
  }
});
