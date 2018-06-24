def func1(*args):   # * 表示args是个元组
    print(args)

def func2(**kw_args):  # **表示kw_args是个字典
    print(kw_args)

func1()
func1('zs')
func1('zs', 25)
func1('zs', 25, 'male')
func2()
func2(name='zs')
func2(name='zs', age=25)
