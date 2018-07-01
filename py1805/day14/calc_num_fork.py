import time
import os

def func():
    result = 0
    for i in range(50000000):
        result += i
    print(result)

if __name__ == '__main__':
    start = time.time()
    for i in range(2):
        pid = os.fork()
        if not pid:
            func()
            exit(1)
    os.waitpid(-1, 0)
    os.waitpid(-1, 0)
    end = time.time()
    print(end - start)
