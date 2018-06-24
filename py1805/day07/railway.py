import time
import sys

# l = 19
# print('#' * 20, end='')
# sys.stdout.flush()   # 标准输出有缓冲区，flush可以立即输出到屏幕
#
# for i in range(20):
#     time.sleep(0.5)
#     print('\r%s@%s' % ('#' * i, '#' * (l - i)), end='')
##############################################
l = 19
print('#' * 20, end='')
sys.stdout.flush()
i = 0

while True:
    try:
        time.sleep(0.3)
    except KeyboardInterrupt:
        print('\nBye-bye')
        break
    print('\r%s@%s' % ('#' * i, '#' * (l - i)), end='')
    if i == l:
        i = 0
    i += 1
