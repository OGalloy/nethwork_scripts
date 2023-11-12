#tcp client
import sys
import socket

class TCP_Client(socket.socket):
    def __init__(self, dest = "127.0.0.1", port = "80", message = "empty"):
        self.dest = dest
        self. port = port
        self.message = message
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)

    def set_timeout(self, value):
        super().settimeout(value)    
    
    def call(self):
        super().connect((self.dest, self.port))
        super().send(str.encode(self.message))
        response = super().recv(4096)
        super().close()
        return response

        

#print(f"Host: {sys.argv[1]} Port: {sys.argv[2]}")

#client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#client.settimeout(10)

#client.connect((sys.argv[1], int(sys.argv[2])))

#client.send(str.encode(sys.argv[3]))

#response = client.recv(4096)

#print(response.decode())

#client.close()

if __name__ == '__main__':
    client = TCP_Client('127.0.0.1', 8080, "ACK")
    data = client.call()
    print(data)