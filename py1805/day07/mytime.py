import time
from datetime import datetime, timedelta

time.localtime()  # 返回struct_time
time.localtime(0)  # 0是秒数，以本地时区为准
time.gmtime(0)  # 按格林威治所在时区算
time.time()  # 返回1970-1-1-8:00:00到执行此命令之间的秒数
# 将struct_time转换成时间戳
time.mktime((2018, 5, 27, 14, 0, 0, 0, 0, 0))
time.sleep(3)
time.asctime()  # 返回当前UTC时间
time.ctime()  # 返回当前UTC时间
time.ctime(0)  # 参数是时间戳
time.asctime(time.localtime())  # 参数是struct_time
time.strftime('%Y-%m-%d')  # 2018-05-27
time.strftime('%Y-%m-%d %H:%M:%S')  # 2018-05-27 13:54:47
# 将字符串转换成struct_time，与strftime正好相反
time.strptime('2018/5/27 14:30:00', '%Y/%m/%d %H:%M:%S')
##############################################################
datetime.today()
datetime.now()
# 与time模块中的strptime类似
datetime.strptime('2018/5/27 14:30:00', '%Y/%m/%d %H:%M:%S')
t = datetime.now()
datetime.strftime(t, '%Y/%m/%d %H:%M:%S')
datetime.ctime(t)
# 以下计算100天零3小时之后是什么时候
t = datetime.today()
t1 = timedelta(days=100, hours=3)  # from datetime import timedelta
t2 = t + t1
t2
t2.year
t2.month
t2.day
t2.hour
t2.minute
t2.second
