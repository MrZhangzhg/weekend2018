import random

number = random.randint(1, 100)
tries = 0
print(number)

while tries < 3:
    answer = int(input('guess: '))
    if answer > number:
        print('猜大了')
    elif answer < number:
        print('猜小了')
    else:
        print('猜对了')
        break           # 结束循环
    tries += 1
else:     # 它是while-else结构，循环被break不执行，否则执行
    print('the number is:', number)
