import getpass
import paramiko
import sys
import os
import threading

def remote_comm(host, user, pwd, comm):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, username=user, password=pwd, allow_agent=False)
    stdin, stdout, stderr = ssh.exec_command(comm)
    out = stdout.read().decode('utf8')
    error = stderr.read().decode('utf8')
    if out:
        print('[OUT] %s:\n%s' % (host, out), end='')
    if error:
        print('[ERROR] %s:\n%s' % (host, error), end='')
    ssh.close()

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: %s ipfile username "command"' % sys.argv[0])
        sys.exit(1)
    if not os.path.isfile(sys.argv[1]):
        print('No such file:', sys.argv[1])
        sys.exit(2)
    ipfile = sys.argv[1]
    user = sys.argv[2]
    comm = sys.argv[3]
    pwd = getpass.getpass("password: ")
    with open(ipfile) as fobj:
        for line in fobj:
            ip = line.strip()
            t = threading.Thread(target=remote_comm, args=(ip, user, pwd, comm))
            t.start()
