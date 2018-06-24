# with语句结束，文件自动关闭，不需要再执行close()语句
with open('/tmp/mima') as f:   # 相当于f = open('/tmp/mima')
    print(f.readline())
