# simple tcp server

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 8080))
server.listen(1)

print("server is listening...")

conn, addr = server.accept()
print("connected to", addr)

data = conn.recv(1024)
print("client says:", data.decode())

conn.send("hello from server".encode())

conn.close()
