import socket,time,threading
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
s.listen(5)

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf8')).encode('utf8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

while True:
    sock, addr = s.accept()
    t = threading.star(target=tcplink, args=(sock,addr))
    t.start()