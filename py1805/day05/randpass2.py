#!/usr/bin/env python3

import string
from random import choice

all_chs = string.ascii_letters + string.digits


def gen_pass(length=8):
    result = ''

    for i in range(length):
        ch = choice(all_chs)
        result += ch

    return result


if __name__ == '__main__':
    print(gen_pass())
    print(gen_pass(6))
