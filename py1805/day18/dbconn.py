# mysqladmin password tedu.cn
# mysql -uroot -ptedu.cn
# MariaDB [(none)]> CREATE DATABASE tarena DEFAULT CHAR SET 'utf8';

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'mysql+pymysql://root:tedu.cn@localhost/tarena?charset=utf8',
    encoding='utf8',
    echo=True
)
Session = sessionmaker(bind=engine)
Base = declarative_base()  # 创建ORM映射的基类

class Departments(Base):
    __tablename__ = 'departments'  # 数据库中表的名字
    dep_id = Column(Integer, primary_key=True) # dep_id是字段名
    dep_name = Column(String(20), unique=True)

    def __str__(self):
        return "<部门：%s>" % self.dep_name

class Employees(Base):
    __tablename__ = 'employees'
    emp_id = Column(Integer, primary_key=True)
    emp_name = Column(String(20))
    gender = Column(String(10))
    birth_date = Column(Date)
    phone = Column(String(11))
    email = Column(String(50))
    dep_id = Column(Integer, ForeignKey('departments.dep_id'))

    def __str__(self):
        return '员工：<%s: %s>' % (self.emp_id, self.emp_name)

class Salary(Base):
    __tablename__ = 'salary'
    auto_id = Column(Integer, primary_key=True)
    date = Column(Date)
    emp_id = Column(Integer, ForeignKey('employees.emp_id'))
    basic = Column(Integer)
    awards = Column(Integer)

    def __str__(self):
        return "%s: salary<%s: %s>" % \
               (self.date, self.emp_id, self.basic + self.awards)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
