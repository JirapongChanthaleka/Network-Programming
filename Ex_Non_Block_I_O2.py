#cilent
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 1234))
sock.setblocking(0)

data = 'foober\n' * 10 * 1024 * 1024
sent = sock.send(data.encode())
assert sent == len(data), '%s != %s' % (sent, len(data))

