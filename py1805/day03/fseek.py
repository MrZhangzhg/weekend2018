f = open('/tmp/mima')
f.read(5)  # 读取５字节，文件指针相应的向后移动５字节
f.tell()   # 返回当前文件指针位置
f.seek(0, 0)  # 返回文件开头，第一个０表示偏移量，第二个０表示相对位置
              # 相对位置０表示开头，１表示当前位置，２表示结尾
f.read(5)  # 重新读取开头的５字节
f.close()