# yn = input('Continue(y/n)? ')
#
# while yn != 'n':
#     print('working...')
#     yn = input('Continue(y/n)? ')
#
# DRY: Don't Repeat Yourself
# Pythonic
#
while True:
    yn = input('Continue(y/n)? ')
    if yn == 'n':
        break    # 结束循环，循环后续代码也不执行
    print('working...')
