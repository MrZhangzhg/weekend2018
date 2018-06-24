import keyword
import string

first_chs = string.ascii_letters + '_'
all_chs = first_chs + string.digits

def check_idt(idt):
    if keyword.iskeyword(idt):
        return '%s is keyword' % idt

    if idt[0] not in first_chs:
        return '1st char invalid'

    for ind, val in enumerate(idt[1:]):
        if val not in all_chs:
            return 'char in position #%s invalid' % (ind + 2)

    return '%s is valid' % idt

if __name__ == '__main__':
    print(check_idt('hello'))
    idt = input('identifier to check: ')
    print(check_idt(idt))
