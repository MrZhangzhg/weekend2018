import time

for i in range(1, 11):
    print("\r%d" % i, end='')   # \r表示回车，但不换行
    time.sleep(1)
