import sys

def unix2dos(fname):
    new_fname = 'new_' + fname
    with open(fname, 'rb') as src_fobj:
        with open(new_fname, 'wb') as dst_fobj:
            for line in src_fobj:
                line = line.rstrip(b'\r\n') + b'\r\n'
                dst_fobj.write(line)


if __name__ == '__main__':
    unix2dos(sys.argv[1])
