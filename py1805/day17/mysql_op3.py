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

query1 = "SELECT * FROM departments ORDER BY dep_id"
result = cursor.execute(query1)
print(result)
print('-' * 30)
data1 = cursor.fetchone()
print(data1)
print('-' * 30)
data2 = cursor.fetchmany(2)
print(data2)
print('-' * 30)
data3 = cursor.fetchall()
print(data3)

cursor.close()
conn.close()
