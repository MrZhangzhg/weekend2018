from random import randint

def func1(x):
    return x % 2

def func2(x):
    return (x - 10) * 2

if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)
    # for i in filter(func1, nums):
    #     print(i)
    # for j in filter(lambda x: x % 2, nums):
    #     print(j)
    print(list(map(func2, nums)))
    print(list(map(lambda x: (x - 10) * 2, nums)))
