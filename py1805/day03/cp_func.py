import sys

def copy(src_fname, dst_fname):
    src_fobj = open(src_fname, 'rb')
    dst_fobj = open(dst_fname, 'wb')

    while True:
        data = src_fobj.read(4096)
        if not data:
            break
        else:
            dst_fobj.write(data)

    src_fobj.close()
    dst_fobj.close()

copy(sys.argv[1], sys.argv[2])
# python3 cp_func.py /bin/touch /tmp/ttt
