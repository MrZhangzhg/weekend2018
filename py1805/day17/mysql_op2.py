import pymysql

# 创建连接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='tedu.cn',
    db='tarena',
    charset='utf8'
)
# 返回游标
cursor = conn.cursor()

insert1 = "INSERT INTO departments VALUES(%s, %s)"
deps = [(7, '行政部'), (6, '财务部')]
cursor.executemany(insert1, deps)

conn.commit()
cursor.close()
conn.close()
