from random import randint

def qsort(data):
    if len(data) < 2:
        return data
    middle = data[0]
    smaller = []
    larger = []
    for item in data[1:]:
        if item < middle:
            smaller.append(item)
        else:
            larger.append(item)

    return qsort(smaller) + [middle] + qsort(larger)

if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)
    print(qsort(nums))
