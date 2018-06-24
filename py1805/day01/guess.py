# if-elif-else是多分支，一旦某一条件满足就会执行相应子语句，其他不再执行
# if
#
# elif
#
# elif
#
# else:

import random

num = random.randint(1, 10)
# print(num)
answer = int(input("number: "))

if answer > num:
    print('猜大了')
elif answer < num:
    print('猜小了')
else:
    print('猜对了')
