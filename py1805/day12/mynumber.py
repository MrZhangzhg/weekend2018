class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return self.n + other

    def __radd__(self, other):
        return self.n + other

    def __sub__(self, other):
        return self.n - other

    def __rsub__(self, other):
        return other - self.n

    def __gt__(self, other):
        return self.n > other


if __name__ == '__main__':
    a = Number(10)
    print(a + 5)
    print(5 + a)
    print(a - 5)
    print(5 - a)
    print(a > 5)

