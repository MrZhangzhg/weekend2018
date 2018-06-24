py_str = 'hello world!'
py_str.capitalize()  # 首字符大写
py_str.center(20, '#')  # 居中，用#填充空白部分
py_str.ljust(30)  # 左对齐
py_str.rjust(30)  # 右对齐
py_str.count('l')  # 统计字符串出现的次数
py_str.count('ll')
py_str.endswith('!')  # 判断字符串是否以!结尾
py_str.endswith('d!')
py_str.startswith('a')  # 判断字符串是否以a开头
py_str.title()  # 每个单词单字母大写
py_str.islower()  # 字符串中所有字母都是小写返回True
'Hao123'.isupper()  # 字符串中所有字母都是大写返回True
'Hao123'.isdigit()  # 所有字符全部是数字才为True
'Hao'.isalpha()  # 所有字符全部是字母才为True
'Hao123'.isalnum()  # 所有字符全部是字母或数字才为True
py_str.upper()  # 转成大写字母
py_str.lower()  # 转成小写字母
py_str.split()  # 切分字符串
'hello.tar.gz'.split('.')
'  hello  \n'.strip()  # 去除两端空白字符
'  hello  \n'.lstrip()
'  hello  \n'.rstrip()
