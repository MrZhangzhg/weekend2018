from random import randint, shuffle
alist = [10, 20]
alist.append(30)
alist.insert(0, 1)
alist.count(10)  # 统计10出现的次数
alist.extend('new')
alist.extend(['new', 'old'])
alist.index('new')  # 获得new的下标
alist.reverse()  # 将列表反转
alist.sort()  # 排序，如果列表中的对象不是同一类型则报错
alist.pop()  # 弹出列表中的最后一项
alist.pop(1)  # 弹出下标为1的项
alist.remove('new')  # 移除列表中的第一个new
clist = alist.copy()  # 只是将alist的值赋值给clist
clist.clear()  # 清空列表
alist = [randint(1, 100) for i in range(10)]
alist.sort()
shuffle(alist)  # 打乱列表
