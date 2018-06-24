from time import sleep, time

def deco(func):
    def timeit():    # func -> loop
        start = time()
        result = func()   # loop()
        end = time()
        return result, end - start
    return timeit

@deco
def loop():
    alist = []
    for i in range(1, 11):
        alist.append(i)
        sleep(0.2)
    return alist

if __name__ == '__main__':
    # loop = deco(loop)   # 新的loop是timeit
    print(loop())
