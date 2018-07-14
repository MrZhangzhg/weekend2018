# mysqladmin password tedu.cn
# mysql -uroot -ptedu.cn
# MariaDB [(none)]> CREATE DATABASE tarena DEFAULT CHAR SET 'utf8';

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine(
    'mysql+pymysql://root:tedu.cn@localhost/tarena',
    encoding='utf8',
    echo=True
)
Base = declarative_base()  # 创建ORM映射的基类

class Departments(Base):
    __tablename__ = 'departments'  # 数据库中表的名字
    dep_id = Column(Integer, primary_key=True) # dep_id是字段名
    dep_name = Column(String(20), unique=True)

    def __str__(self):
        return "<部门：%s>" % self.dep_name

if __name__ == '__main__':
    Base.metadata.create_all(engine)
