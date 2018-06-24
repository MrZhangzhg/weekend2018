alist = ['zhangsan', 'lisi', 'wangwu', 'zhaoliu']
for name in alist:
    print(name)

for ind in range(len(alist)):  # [0, 1, 2, 3]
    print(ind, alist[ind])

for item in enumerate(alist):
    print(item[0], item[1])

for ind, val in enumerate(alist):
    print(ind, val)

list(reversed(alist))   # 翻转
sorted(alist)  # 排序
