import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind((UDP_IP, UDP_PORT))
while True:
    data, addr = socket.recvfrom(1024)
    print("received message: %s" % data)