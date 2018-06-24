# 集合相当于是无值的字典，所以也采用{}表示
s1 = set('abcd')
frozenset('abcd')  # 不可变集合
len(s1)
'a' in s1
for ch in s1:
    print(ch)
s2 = set('cde')
s1 & s2  # 取交集
s1 | s2  # 取并集
s1 - s2  # 差补，即只存在s1中的元素
s1.add('new')
s1.update('new')
s1.update(['hello', 'world'])
s1.pop()
s1.remove('e')

s1 = set('abcde')
s2 = set('bcd')
s2.issubset(s1)   # s2是s1的子集
s1.issuperset(s2)  # s1是s2的超集
s1.union(s2)  # s1 | s2
s1.intersection(s2)  # s1 & s2
s1.difference(s2)  # s1 - s2
