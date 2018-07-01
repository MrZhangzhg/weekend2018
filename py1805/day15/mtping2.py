import threading
import subprocess

class Ping:
    def __init__(self, host):
        self.host = host

    def __call__(self):
        retval = subprocess.call(
            'ping -c2 %s &> /dev/null' % self.host,
            shell=True
        )
        if retval == 0:
            print('%s: up' % self.host)
        else:
            print('%s: down' % self.host)

if __name__ == '__main__':
    ip_list = ['172.40.51.%s' % i for i in range(1, 255)]
    for ip in ip_list:
        t = threading.Thread(target=Ping(ip))
        t.start()
