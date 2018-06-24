import getpass   # 导入系统模块getpass

username = input('username: ')
password = getpass.getpass('password: ')

# 注意：123456是字符串，要放到引号中，判断是否相等是双等号
if username == 'bob' and password == '123456':
    print('Login Successful')
else:
    print('Login incorrect')
