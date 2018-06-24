src_fname = '/bin/ls'
dst_fname = '/tmp/list'

src_fobj = open(src_fname, 'rb')
dst_fobj = open(dst_fname, 'wb')

while True:
    data = src_fobj.read(4096)
    # if data == b'':   # 读到结尾后，再读就是空
    # if len(data) == 0:   # 读到结尾后，data值为0
    if not data:    # 空对象是False，取反为True
        break
    else:
        dst_fobj.write(data)

src_fobj.close()
dst_fobj.close()
