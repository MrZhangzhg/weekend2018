def counter(start=0):
    count = start
    def incr():
        nonlocal count
        count += 1
        return count
    return incr   # 返回值是一个函数

if __name__ == '__main__':
    a = counter()
    b = counter(10)
    print(a())
    print(b())
    print(a())
    print(b())
