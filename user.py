import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
while True:
    a=str(input("Введите строку: "))
    if a == 'exit':
        break
    else:
        sock.send(a.encode())
        print(sock.recv(1024).decode())
sock.close()
