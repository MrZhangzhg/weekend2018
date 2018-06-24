def get_age(name, age):
    print('%s is %s years old.' % (name, age))

get_age('zs', 25)
get_age(25, 'zs')  # 逻辑不对
get_age(age=25, name='zs')
# get_age(age=25, 'zs')  # 语法错误，应该key=val在后，非关键字参数在前
# get_age(25, name='zs')  # Error: name被赋值两次
get_age('zs', age=25)
# get_age('zs', 25, 100)  # 函数调用时，实参个数要与形参个数相同


