import os
import time

print('Starting...')
pid = os.fork()
if pid:
    # print(os.waitpid(-1, 0))  # 挂起父进程，waitpid返回子进程pid
    time.sleep(7)
    print(os.waitpid(-1, 1))  # 第二个参数是1，表示不挂起父进程
else:
    print('in child')
    time.sleep(5)
    print('child done')
