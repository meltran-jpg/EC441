# simple tcp client

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 8080))

client.send("hello server".encode())

data = client.recv(1024)
print("server says:", data.decode())

client.close()
