###async tcp

import asyncio
import socket
import sys

async def call(dest, port, message):
	
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	async def answer(size):
		return client.recv(size)

	client.settimeout(5)
	client.connect((dest, port))
	client.send(message)
	try:
		print(f"Scaning host: {dest} port: {port}")
		recv = await answer(4096)
		print(recv.decode())
		client.close()
	except TimeoutError:
		print("TimeoutError")
		client.close()	

async def main():
	print("Coroutines was started!")
	task1 = asyncio.create_task(call("kzts.ru", 23, b"Message"))
	task2 = asyncio.create_task(call("kzts.ru", 80, b"Message"))
	task3 = asyncio.create_task(call("kzts.ru", 21, b"Message"))

	await task3
	await task2
	await task1

if __name__ == '__main__':
	asyncio.run(main())