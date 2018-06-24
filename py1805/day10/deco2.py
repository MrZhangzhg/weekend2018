def set_color(func):
    def red(*word):
        return '\033[31;1m%s\033[0m' % func(*word)
    return red

@set_color
def hello():
    return 'Hello world!'

@set_color
def welcome(word):
    return 'Hello %s' % word

if __name__ == '__main__':
    print(hello())   # -> hello = set_color(hello)
    print(welcome('China'))
