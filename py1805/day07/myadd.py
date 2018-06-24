import time

sum = 0
start = time.time()
for i in range(10000000):
    sum += i

end = time.time()
print(sum, end - start)
