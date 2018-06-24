def add(x, y):
    print(x + y)

add(10, 20)
nums = [100, 200]
add(nums[0], nums[1])
add(*nums)   # *nums，表示把nums拆开
ndict = {'x': 1000, 'y': 2000}
add(**ndict)  # **拆成x=1000, y=2000
