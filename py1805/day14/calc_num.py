import time

def func():
    result = 0
    for i in range(50000000):
        result += i
    print(result)

if __name__ == '__main__':
    start = time.time()
    func()
    func()
    end = time.time()
    print(end - start)
