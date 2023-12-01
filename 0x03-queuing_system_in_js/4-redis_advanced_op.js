import redis, { createClient } from 'redis';

const client = createClient()
	.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`))
	.on('ready', () => console.log('Redis client connected to the server'));

function hset(key, field, value) {
	client.hset(key, field, value, redis.print);
}

hset('HolbertonSchools', 'Portland', 50);
hset('HolbertonSchools', 'Seattle', 80);
hset('HolbertonSchools', 'New York', 20);
hset('HolbertonSchools', 'Bogota', 20);
hset('HolbertonSchools', 'Cali', 40);
hset('HolbertonSchools', 'Paris', 2);

client.hgetall('HolbertonSchools', (error, value) => console.log(value));
