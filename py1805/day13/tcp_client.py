import socket

host = '127.0.0.1'  # 客户端要连接的服务器地址
port = 12345  # 客户端要连接的服务器的端口号
addr = (host, port)

c = socket.socket()
c.connect(addr)
while True:
    data = input('> ') + '\r\n'
    data = data.encode('utf8')
    c.send(data)
    if data.strip() == b'quit':
        break
    print(c.recv(1024).decode('utf8'), end='')

c.close()
