import random

number = random.randint(1, 100)
print(number)

while True:
    answer = int(input('guess: '))
    if answer > number:
        print('猜大了')
    elif answer < number:
        print('猜小了')
    else:
        print('猜对了')
        break           # 结束循环

