import os
os.listdir('/tmp')  # 列出目录内容
os.mkdir('/tmp/mydemo')  # 创建目录
os.chdir('/tmp/mydemo')  # 切换目录
os.listdir()  # 列出当前目录下的内容
os.getcwd()   # 显示当前工作路径
os.symlink('/etc/hosts', 'zhuji')  # 创建快捷方式
os.mknod('mytest.txt')  # 创建空文件
os.path.abspath('mytest.txt')  # 返回文件的绝对路径
os.chmod('mytest.txt', 0o600)  # 修改文件权限
os.path.isdir('/etc')  # 判断是否为目录
os.path.isfile('zhuji')  # 判断是否为文件
os.path.islink('zhuji')  # 判断是否为快捷方式
os.path.exists('abc.txt')  # 判断是否存在
os.path.split('/home/zhangsan/zs.txt')
os.path.dirname('/home/zhangsan/zs.txt')
os.path.basename('/home/zhangsan/zs.txt')
os.path.join('/home/zhangsan', 'zs.txt')
