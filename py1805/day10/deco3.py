def colors(c):
    def set_color(func):
        def red(*word):
            return '\033[31;1m%s\033[0m' % func(*word)
        def green(*word):
            return '\033[32;1m%s\033[0m' % func(*word)
        adict = {'red': red, 'green': green}
        return adict[c]
    return set_color

@colors('red')
def hello():
    return 'Hello world!'

@colors('green')
def welcome(word):
    return 'Hello %s' % word

if __name__ == '__main__':
    print(hello())   # -> hello = set_color(hello)
    print(welcome('China'))
