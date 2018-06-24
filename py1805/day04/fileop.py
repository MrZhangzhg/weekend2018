import shutil

sf = open('/etc/hosts', 'rb')
df = open('/etc/zj', 'wb')
shutil.copyfileobj(sf, df)  # copy文件对象
sf.close()
df.close()
##############################
shutil.copyfile('/etc/hosts', '/tmp/zj2')  # 通过文件名拷贝
# 把zj2的权限设置为和/usr/bin/touch一样
shutil.copymode('/usr/bin/touch', '/tmp/zj2')
# 将zj2的stat信息设备置为与/usr/bin/touch一样
shutil.copystat('/usr/bin/touch', '/tmp/zj2')
# 将hosts文件拷贝到/tmp目录
shutil.copy('/etc/hosts', '/tmp')
# 相当于是cp -p /etc/hosts /tmp
shutil.copy2('/etc/hosts', '/tmp')
# 将security目录拷贝到/tmp下，并改名为anquan
shutil.copytree('/etc/security', '/tmp/anquan')
shutil.rmtree('/tmp/anquan')  # 删除目录
# shutil模块没有删除单个文件的方法，删除单个文件
# 需要使用os模块：os.remove('/tmp/zj2')
shutil.move('/tmp/zj', '/var/tmp')  # 剪切、移动
# 系统命令useradd user1 可以创建用户
# 改变文件的拥有者
shutil.chown('/var/tmp/zj', 'user1')
