#tcp_server.py

import sys
import socket

def tcp_server(ip, port):
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((ip, port))
	server.listen(5)
	print(f'Listening on {ip}:{port}')

	while True:
		client, address = server.accept()
		print(f'Accepted connection from {address[0]}:{address[1]}')
		client_request = client.recv(1024)
		print(f'[*] Received: {client_request.decode("utf-8")}')
		client.send(b'ACK')

if __name__ == '__main__':
	tcp_server("127.0.0.1", 8080)