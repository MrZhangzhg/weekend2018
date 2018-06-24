import star
from random import randint, choice  # 从模块中只导入某些属性
import getpass as gp  # 导入模块的同时，为其改名

star.pstar()
print(randint(1, 100))
print(choice('abcd'))
password = gp.getpass('password: ')  # gp就是getpass模块
