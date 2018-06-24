f = open('/tmp/mima')
for line in f:    # 将文件的每一行赋值给变量line
    print(line, end='')  # 文件行尾本身有\n，加上end=''抑制print自带的\n
f.close()
