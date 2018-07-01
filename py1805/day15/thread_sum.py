import time
import threading

def add():
    result = 0
    for i in range(50000000):
        result += i
    print(result)

if __name__ == '__main__':
    start = time.time()
    t1 = threading.Thread(target=add)
    t1.start()
    t2 = threading.Thread(target=add)
    t2.start()
    t1.join()
    t2.join()
    end = time.time()
    print(end - start)

# GIL: 全局解释器锁。python在某一时刻只能把一个线程发给CPU处理
# 分时操作，时分复用，时间片
# 因为GIL，python多线程不适合计算密集型应用
# python多线程适合IO密集型应用
