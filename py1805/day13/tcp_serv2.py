import socket
from time import strftime

host = ''
port = 12345
addr = (host, port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)  # 为套接字绑定地址
s.listen(1)  # 启动服务监听
while True:
    cli_sock, cli_addr = s.accept()  # accept返回客户端套接字和地址
    print('Client connected from:', cli_addr)
    while True:
        data = cli_sock.recv(1024)
        if data.strip() == b'quit':
            break
        data = '[%s] %s' % \
               (strftime('%Y-%m-%d %H:%M:%S'), data.decode('utf8'))
        data = data.encode('utf8')
        cli_sock.send(data)
    cli_sock.close()
s.close()
