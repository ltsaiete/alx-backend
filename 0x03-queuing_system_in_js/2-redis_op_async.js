import redis, { createClient } from 'redis';
import util from 'util';

const client = createClient()
	.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`))
	.on('ready', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value) {
	client.set(schoolName, value, redis.print);
}

// const get = promisify(client.get);

async function displaySchoolValue(schoolName) {
	const get = util.promisify(client.get).bind(client);
	const value = await get(schoolName).then((response) => response);
	console.log(value);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
