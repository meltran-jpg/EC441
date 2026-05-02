import socket

domain = "google.com"
ip = socket.gethostbyname(domain)

print(f"{domain} resolves to {ip}")
