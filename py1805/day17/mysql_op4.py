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
cursor.scroll(3, mode='absolute')
result = cursor.fetchone()
print(result)
print('-' * 30)
cursor.scroll(-2, mode='relative')
result = cursor.fetchone()
print(result)

cursor.close()
conn.close()
