# Echo server Program
import socket

HOST = ''                 # Symbolic name meaning all available interface
PORT = 50007              # Arbitracy non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data: break
            conn.sendall(data)

# Echo client program
import socket

HOST = 'daring.ewi.nl'    # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT)) 
    s.sendall(b'Hello, world')
    data = s.recv(1024)
    data = s.recv(1024)
print('Received', repr(data))