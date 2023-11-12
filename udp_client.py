#udp client
import socket
import sys

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(b"Message", (sys.argv[1], int(sys.argv[2])))

data, addr = client.recvfrom(4096)

print(data.decode())

client.close()