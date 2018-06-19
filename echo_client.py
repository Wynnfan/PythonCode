import socket,time,threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 9999))

print(s.recv(1024).decode('utf8'))
while True:
    data = input()
    data_byte = data.encode(encoding="utf8")
    s.send(data_byte)
    print(s.recv(1024).decode('utf8'))
s.send(b'exit')
s.close()