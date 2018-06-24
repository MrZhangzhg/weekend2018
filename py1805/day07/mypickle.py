"""只接使用文件，只能把字符类的数据写入。
pickle可以将任意数据对象写入存储器。以后还可以无损的读取出来
"""
import pickle
shopping_list = ['apple', 'pear', 'banana']
with open('shopping.data', 'wb') as fobj:
    pickle.dump(shopping_list, fobj)
#
# with open('shopping.data', 'rb') as fobj:
#     data = pickle.load(fobj)
#
# print(type(data))
# print(data[1:])
