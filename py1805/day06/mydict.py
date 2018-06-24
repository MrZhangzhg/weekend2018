adict = {'name': 'bob', 'age': 25}
bdict = dict(['ab', 'cd']) # 列表中两个字符串，每个串中第一个字符是key，第二个是val
cdict = dict([('name', 'bob'), ('age', 25)])  # 列表中的元组有两项，分别是key和val
ddict = {}.fromkeys(('zhangsan', 'lisi'), 7)  # fromkeys第一个参数的元组中，每一项是key，7是val
len(adict)
'bob' in adict  # 判断bob是不是字典的key
'name' in adict  # 返回True
adict['name']  # 通过key取出val
adict['name'] = 'tom'  # 修改值
adict['phone'] = '13511223344'  # 增加值
adict.keys()  # 返回所有key
adict.values()  # 返回所有val
adict.items()  # 返回[(key, val), (key, val)]
adict.popitem()  # 随机弹出一项
adict.pop('age')
# adict['age']  # 报错，字典中已无age
print(adict.get('age'))  # 不报错，返回None
print(adict.get('age', 'not found'))  # 返回not found
print(adict.get('name', 'not found'))  # 返回tom
adict['name'] = 'jerry'  # name的值改为jerry
adict.setdefault('name', 'john')  # name值仍为jerry
adict.setdefault('age', 23)  # age值为23
