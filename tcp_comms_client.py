import socket

HOST = "192.168.0.106"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Helllo, world")
    data=s.recv(1024)

print(f"Received {data!r}")