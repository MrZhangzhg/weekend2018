import socket

host = ''   # 表示本机的所有地址
port = 12345  # 端口号，应该大于1024
addr = (host, port)

# 创建一个TCP的网络套接字
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置服务器在停止之后，可以立即启动。地址默认保留60s
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)  # 为套接字绑定地址
s.listen(1)  # 启动服务监听
cli_sock, cli_addr = s.accept()  # accept返回客户端套接字和地址
print('Client connected from:', cli_addr)
print(cli_sock.recv(1024))  # 接收客户端发来的数据，最多接收1024字节
cli_sock.send(b'How are you?\r\n')  # 向客户端发送数据
cli_sock.close()  # 客户端安装telnet执行yum install -y telnet
s.close()         # telnet 127.0.0.1 12345  访问服务器1234问端口
