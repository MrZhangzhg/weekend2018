py_str = 'Python'
len(py_str)
py_str[0]   # 下标从０开始
# py_str[6]   # Error
py_str[-1]  # 从右向左取
py_str[2:4] # th 切片起始下标对应的字符包含，结束下标不包含
py_str[2:]  # 从下标２开始，取到结尾
py_str[:2]
py_str[:]   # 从开头取到结尾
py_str[::2] # 从开头取到结尾，步长为２
py_str[1::2]
py_str[::-1] # 步长值为负，表示从右向左取
py_str + ' is cool'  # 字符串拼接
'*' * 50   # 将*重复50遍
't' in py_str  # 成员关系判断
'th' in py_str
'to' in py_str  # False
'to' not in py_str
#############################################################
alist = [1, 5, 10, 'bob', 'alice', [1, 2, 3]]
alist[-3:-1]  # 取切片
alist[-1] = 100  # 修改列表元素
10 in alist
alist.append(50)  # 向列表尾部追加数据
#############################################################
# 元组可以认为是不可变的列表
atuple = (10, 20, 30, 'bob', 'alice')
len(atuple)
atuple[:3]
