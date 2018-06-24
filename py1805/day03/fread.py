# cp /etc/passwd /tmp/mima
# 文件操作的步骤：打开 -> 读写 -> 关闭
f = open('/tmp/mima')   # 默认以r方式打开
data = f.read()   # 默认读取全部内容
f.close()
print(data)
###################
f = open('/tmp/mima')
print(f.read(5))  # 读5字节
print(f.readline()) # 读文本文件的一行
print(f.readlines())   # 读文本文件的所有行，放到列表中
f.close()
#####################
f = open('/usr/bin/ls', 'rb')  # 如果是非文本文件需要加上b，表示bytes
print(f.read(5))
f.close()
