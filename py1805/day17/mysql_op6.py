import pymysql
import time

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

insert_emp = "INSERT INTO employees VALUES(%s, %s, %s, %s, %s, %s)"
insert_sal = "INSERT INTO salary(date, emp_id, basic, awards) VALUES(%s, %s, %s, %s)"
emp_data = (6, '张三', 'male', '15088992233', 'zs@tedu.cn', 3)
sal_data = (time.strftime('%Y-%m-%d'), 3, 13000, 3000)
cursor.execute(insert_emp, emp_data)
cursor.execute(insert_sal, sal_data)
conn.commit()

cursor.close()
conn.close()
