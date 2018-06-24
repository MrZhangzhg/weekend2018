import socket
import sys

class UdpClient:
    def __init__(self):
        self.client = socket.socket(type=socket.SOCK_DGRAM)

    def communicate(self, host, port):
        addr = (host, port)
        while True:
            data = input('> ') + '\r\n'
            data = data.encode('utf8')
            if data.strip() == b'quit':
                break
            self.client.sendto(data, addr)
            print(self.client.recvfrom(1024)[0].decode('utf8'), end='')

    def close(self):
        self.client.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('%s host port' % sys.argv[0])
        sys.exit(1)
    ip = sys.argv[1]
    port = int(sys.argv[2])
    c = UdpClient()
    c.communicate(ip, port)
    c.close()
