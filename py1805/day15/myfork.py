import os

for i in range(7):
    pid = os.fork()
    if pid == 0:
        print('Hello World!')
        exit()

print('Done')

# [0, 1, 2]
#  c1 -> hello world
#     c1-1-> hello world
#        c1-1-1: hello world
#     c1-2 -> hello world
# [0, 1, 2]
#     c2 -> hello world
#     c2-1 -> hello world
# [0, 1, 2]
#        c3->hello world
