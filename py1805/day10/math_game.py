from random import randint, choice

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def exam():
    cmds = {'+': add, '-': sub}
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)
    op = choice('+-')
    result = cmds[op](*nums)
    prompt = "%s %s %s = " % (nums[0], op, nums[1])
    tries = 0

    while tries < 3:
        try:
            answer = int(input(prompt))
        except:
            print()
            continue
        if answer == result:
            print('right')
            break
        print('Wrong answer. Try again.')
        tries += 1
    else:
        print('%s%s' % (prompt, result))


def main():
    while True:
        exam()
        try:
            yn = input('Continue(y/n)? ').strip()[0]
        except IndexError:
            continue
        except (KeyboardInterrupt, EOFError):
            print('\nBye-bye')
            yn = 'n'

        if yn in 'nN':
            break

if __name__ == '__main__':
    main()
