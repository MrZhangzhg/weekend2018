"{} is {} years old".format('zhangsan', 25)
"{} is {} years old".format(25, 'zhangsan')
"{1} is {0} years old".format(25, 'zhangsan')
adict = {'name': 'zhangsan', 'age': 25}
"{0[name]} is {0[age]} years old".format(adict)
alist = ['zhangsan', 25]
"{0[0]} is {0[1]} years old".format(alist)
"{:>20}".format('name')  # 右对齐，20宽度
"{:<20}".format('name')  # 左对齐，20宽度
"{:^20}".format('name')  # 居中，20宽度
"{:#>20}".format('name') # 右对齐，20宽度，左侧填充#
