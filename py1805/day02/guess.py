import random

running = True
number = random.randint(1, 100)

while running:
    answer = int(input('guess: '))
    if answer > number:
        print('猜大了')
    elif answer < number:
        print('猜小了')
    else:
        print('猜对了')
        running = False
