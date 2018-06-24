from functools import partial

def add(x, y, z):
    return x + y + z

if __name__ == '__main__':
    print(add(10, 20, 5))
    print(add(10, 20, 15))
    print(add(10, 20, 8))
    new_add = partial(add, y=10, z=20)
    print(new_add(3))
