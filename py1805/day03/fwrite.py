f = open('abc.txt', 'w')  # 文件不存在则创建，已存在则清空
f.write('hello world!')
f.flush()   # 立即将数据同步到硬盘文件，否则先写入到缓冲区
f.write('hello china!\n')
f.writelines(['how are you?\n', 'nice to meet you!\n'])
f.close()
