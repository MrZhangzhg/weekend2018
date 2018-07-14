from dbconn import Departments, Session

session = Session()
# sqlalchemy的主键默认设置为自动增长
# dev = Departments(dep_name="development")
# print(dev.dep_name)
# print(dev.dep_id)
# hr = Departments(dep_id=2, dep_name='人事部')
# session.add(hr)
ops = Departments(dep_name='运维部')
finance = Departments(dep_name='财务部')
session.add_all([ops, finance])
session.commit()
session.close()
