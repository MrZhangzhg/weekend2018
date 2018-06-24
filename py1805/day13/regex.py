import re

print(re.match('foo', 'food'))  # match从开头匹配
print(re.match('foo', 'seafood'))
m = re.match('f..', 'food')
print(m.group())   # m.group()取出匹配内容

m = re.search('f..', 'seafood')  # search可以在任意位置匹配
print(m.group())
print(re.findall('f..', 'seafood is food'))  # 返回所有匹配的列表

result = re.finditer('f..', 'seafood is food')
for m in result:
    print(m.group())

# 如果有大量内容需要匹配，为了执行效率，可以先把模式进行编译
cpatt = re.compile('f..')
m = cpatt.search('seafood')
print(m.group())

# 用-和.作为分隔符切割，注意.表示任意字符，所以要转义
print(re.split('-|\.', 'hello-world.tar.gz'))

# 查找替换，把X替换成MrZzg
print(re.sub('X', 'MrZzg', 'Hi X. Nice to meet you, X!'))
