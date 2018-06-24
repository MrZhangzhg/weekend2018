def foo():
    print('in foo')
    bar()

# foo()   # NameError

def bar():
    print('in bar')

if __name__ == '__main__':
    foo()   # 没问题，因为调用foo时，bar已经存在
