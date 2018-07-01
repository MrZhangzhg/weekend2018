import threading
import subprocess

def ping(host):
    retval = subprocess.call(
        'ping -c2 %s &> /dev/null' % host,
        shell=True
    )
    if retval == 0:
        print('%s: up' % host)
    else:
        print('%s: down' % host)

if __name__ == '__main__':
    ip_list = ['172.40.51.%s' % i for i in range(1, 255)]
    for ip in ip_list:
        t = threading.Thread(target=ping, args=(ip,))
        t.start()



