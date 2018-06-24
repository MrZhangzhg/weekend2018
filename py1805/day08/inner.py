def foo():
    def bar():
        print('in foo-bar')
    print('in foo')
    bar()

if __name__ == '__main__':
    foo()
