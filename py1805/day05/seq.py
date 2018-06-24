# 以下内容在交互解释器上输写
from random import randint
alist = ['bob', 'alice', 'tom', 10, 20, [1, 2, 3]]
alist[-1]
alist[-1][-1]
[1, 2, 3][-1]
a = alist[-1]
a
alist[-1] = 100
alist[3:5] = [1000, 2000, 3000, 4000]
alist[1:1]
alist[1:1] = ['zhangsan', 'lisi']
'*' * 20
alist + [200]
'bob' in alist
100000 not in alist
alist = [randint(1, 100) for i in range(10)]
