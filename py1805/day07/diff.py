# cp /etc/passwd mima1
# cp /etc/passwd mima2
# gedit mima2   # 编辑文件，使得两个文件有些不同行

old_fname = 'mima1'
new_fname = 'mima2'
dst_fname = 'result.txt'

with open(old_fname) as fobj:
    data1 = set(fobj)

with open(new_fname) as fobj:
    data2 = set(fobj)

with open(dst_fname, 'w') as fobj:
    fobj.writelines(data2 - data1)
