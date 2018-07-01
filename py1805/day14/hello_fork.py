import os

print('Hello World!')
os.fork()   # 生成子进程，后续代码在父子进程中都会执行
print('How are you?')
