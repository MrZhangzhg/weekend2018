import socket
import sys

class TcpClient:
    def __init__(self):
        self.client = socket.socket()

    def connect(self, host, port):
        addr = (host, port)
        self.client.connect(addr)

    def communicate(self):
        while True:
            data = input('> ') + '\r\n'
            data = data.encode('utf8')
            self.client.send(data)
            if data.strip() == b'quit':
                break
            print(self.client.recv(1024).decode('utf8'), end='')

    def close(self):
        self.client.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('%s host port' % sys.argv[0])
        sys.exit(1)
    c = TcpClient()
    ip = sys.argv[1]
    port = int(sys.argv[2])
    c.connect(ip, port)
    c.communicate()
    c.close()
