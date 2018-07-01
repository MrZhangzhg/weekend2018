import paramiko

def remote_comm(host, user, pwd, comm):
    ssh = paramiko.SSHClient()
    # 以下这行相当于是在ssh时问(yes/no)?回答yes
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ssh.connect(hostname=host, username=user, password=pwd)
    # 如果上面代码执行有异常发生，那么使用下面这个
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
    remote_comm('192.168.4.1', 'root', '123456', 'ls /root')
    remote_comm('192.168.4.1', 'root', '123456', 'id zhangsan')
