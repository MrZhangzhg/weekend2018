def gen_fib(l=10):
    fib = [0, 1]

    for i in range(l-2):
        fib.append(fib[-1] + fib[-2])

    return fib  # 不返回变量fib，而是返回变量的值，如[0, 1, 1, 2, 3]

length = int(input("length: "))
a = gen_fib(length)  # 传参不是把length变量传进去，而是它的值，如5
print(a)
# for i in a:
#     print(i+3)

print(gen_fib())
