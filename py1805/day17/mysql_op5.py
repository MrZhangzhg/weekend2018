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

query1 = "UPDATE departments SET dep_name=%s WHERE dep_id=%s"
result = cursor.execute(query1, ('人事部', 1))
query2 = "DELETE FROM departments WHERE dep_name=%s"
result2 = cursor.execute(query2, ('qa2',))

conn.commit()
cursor.close()
conn.close()
