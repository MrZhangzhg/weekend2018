# for i in range(4):  # [0, 1, 2, 3]
#     for j in range(i + 1):  # [0, 1, 2, 3]
#         print('hello', end=' ')
#     print()
#
#######################################
# 1 X 1 = 1
for i in range(1, 10):
    for j in range(1, i + 1):
        # print(j, 'X', i, '=', i * j, end=' ')
        print('%sX%s=%s' % (j, i, i*j), end=' ')
    print()
