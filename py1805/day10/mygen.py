import time

def mygen():
    yield 10
    a = 10 + 20
    yield a
    yield 'hello world'

if __name__ == '__main__':
    aaa = mygen()
    for item in aaa:
        print(item)
        time.sleep(0.5)
