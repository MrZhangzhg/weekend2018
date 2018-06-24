if 3 > 0:
    print('yes')

# 判断语句是分支语句，if和else只能执行一个
if 3 > 10:
    print('yes')
else:
    print('no')

if -0.0: print('ok')   # 不打印，任何值为０的数字都是False
if 10: print('10 ok')   # 打印
if ' ': print('space ok')  # 任何非空对象都是True，空对象是False
if '': print('ooooo')   # 不打印
if [10, 20]: print('list ok')   # 打印
