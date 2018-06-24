from mktxtfile import get_content

width = 50
content = get_content()  # ['hello world', 'how are you?']

print('*' * width)
for line in content:
    print('*%s*' % line.center(width-2))
print('*' * width)
