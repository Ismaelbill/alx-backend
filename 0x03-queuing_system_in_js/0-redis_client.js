#!/usr/bin/node
import { createClient } from 'redis';

const client = createClient();

client.on('connect', (_) => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) =>
  console.log(
    `Redis client not connected to the server: Error: Redis connection to ${err.address}:${err.port} failed - ${err.message}`
  )
);
