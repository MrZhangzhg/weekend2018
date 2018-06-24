import sys

try:
    num = int(input('number: '))
    result = 100 / num
except ValueError:
    print('必须输入数字')
except ZeroDivisionError:
    print('不能是0')
except (KeyboardInterrupt, EOFError):
    print('\nBye-bye')
    sys.exit(1)
else:   # 不发生异常才执行
    print(result)
finally:  # 不管是否发生异常，都会执行
    print('Done')

# try-except/try-finally 是常见用法
