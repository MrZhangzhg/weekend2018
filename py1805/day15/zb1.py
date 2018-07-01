import os
import time

print('Starting...')
pid = os.fork()
if pid:
    print('Hello from parent')
    time.sleep(30)
    print('parent done')
else:
    print('Hello from child')
    time.sleep(10)
    print('child done')

#执行系统命令 watch -n1 ps a后，再从另一终端执行此脚本
