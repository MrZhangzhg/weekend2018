f1 = open('/bin/ls', 'rb')
f2 = open('/tmp/list', 'wb')

data = f1.read()
f2.write(data)

f1.close()
f2.close()
# md5sum /tmp/list /bin/ls   # 系统命令，查看文件md5值
