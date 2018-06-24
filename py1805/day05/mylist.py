# 列表解析
[10]
[10 + 5]  # 将表达式计算结果存入列表
[10 + 5 for i in range(5)] # 表达式计算5次，结果存入列表
[10 + i for i in range(1, 6)] # 将循环内的变量传给表达式
[10 + i for i in range(1, 11)]
[10 + i for i in range(1, 11) if i % 2]  # 满足if条件的变量才参与运算
[10 + i for i in range(1, 11) if i % 2 == 1]
content = ['hello world!', 'how are you?']
content = ['%s\n' % line for line in content]
