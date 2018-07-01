import os

print('Starting...')

pid = os.fork()  # fork()返回两次，针对父进程返回子进程PID，子进程返回0
if pid:
    print('Hello from parent...')
else:
    print('Hello from child...')

print('Hello from both')
