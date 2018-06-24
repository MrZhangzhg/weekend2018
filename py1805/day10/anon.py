def add(x, y):
    return x + y

a = lambda x, y: x + y
b = add
print(id(add))
print(id(b))

print(a(10, 20))
print(b(100, 200))
