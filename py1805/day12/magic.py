class Book:
    def __init__(self, title, author):  # 实例化时自动执行
        self.title = title
        self.author = author

    def __str__(self):  # 返回字符串
        return '《%s》' % self.title

    def __call__(self):
        print('《%s》 is written by %s' % (self.title, self.author))


if __name__ == '__main__':
    pybook = Book('Core Python', 'Wesley')   # 调用__init__方法
    print(pybook)   # 调用__str__方法
    pybook()   # 调用__call__方法
