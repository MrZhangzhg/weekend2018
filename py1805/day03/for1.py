# for ch in 'abcd':
#     print(ch)
#
# for i in [1, 2, 3, 4]:
#     print(i)

# range采用延迟计算，需要用到数字，临时生成，不需要时也不占内存
# for i in range(10):
#     print(i)

# result = 0
# for i in range(10000001):
#     result += i
# print(result)

print(list(range(6, 11)))
print(list(range(1, 10, 2)))
print(list(range(10, 0, -1)))
