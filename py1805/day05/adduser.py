import sys
import subprocess
from randpass2 import gen_pass

def adduser(username, fname):
    password = gen_pass()
    data = """user info:
username: %s
password: %s
"""
    subprocess.call('useradd %s' % username, shell=True)
    subprocess.call(
        'echo %s | passwd --stdin %s &> /dev/null' % (password, username),
        shell=True
    )
    with open(fname, 'a') as fobj:
        fobj.write(data % (username, password))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: %s uername fname" % sys.argv[0])
        sys.exit(1)
    adduser(sys.argv[1], sys.argv[2])
