import os
import pickle
import time

def save_money(record, wallet):
    try:
        amount = int(input('amount: '))
        comment = input('comment: ')
    except:
        print()
        return
    date = time.strftime('%Y-%m-%d')

    with open(wallet, 'rb') as fobj:
        balance = pickle.load(fobj) + amount
    line = '%-12s%-8s%-8s%-10s%-20s\n' % (date, '', amount, balance, comment)
    with open(record, 'a') as fobj:
        fobj.write(line)
    with open(wallet, 'wb') as fobj:
        pickle.dump(balance, fobj)

def cost_money(record, wallet):
    try:
        amount = int(input('amount: '))
        comment = input('comment: ')
    except:
        print()
        return
    date = time.strftime('%Y-%m-%d')

    with open(wallet, 'rb') as fobj:
        balance = pickle.load(fobj) - amount
    line = '%-12s%-8s%-8s%-10s%-20s\n' % (date, amount, '', balance, comment)
    with open(record, 'a') as fobj:
        fobj.write(line)
    with open(wallet, 'wb') as fobj:
        pickle.dump(balance, fobj)

def view_money(record, wallet):
    with open(wallet, 'rb') as fobj:
        balance = pickle.load(fobj)
    print('\033[32;1m%-12s%-8s%-8s%-10s%-20s\033[0m' % ('date', 'cost', 'save', 'balance', 'comment'))
    with open(record) as fobj:
        for line in fobj:
            print(line, end='')
    print('\033[31;1mLatest Balance: %d\033[0m' % balance)

def show_menu():
    record = 'record.txt'
    wallet = 'wallet.data'
    if not os.path.exists(record):
        os.mknod(record)
    if not os.path.exists(wallet):
        with open(wallet, 'wb') as fobj:
            pickle.dump(10000, fobj)
    cmds = {'0': save_money, '1': cost_money, '2': view_money}
    prompt = """(0) save money
(1) cost money
(2) view money
(3) quit
Please input your choice(0/1/2/3): """
    while True:
        try:
            choice = input(prompt).strip()[0]
        except IndexError:
            continue
        except (KeyboardInterrupt, EOFError):
            print()
            choice = '3'

        if choice not in '0123':
            print('Invalid input. Try again.')
            continue

        if choice == '3':
            break

        cmds[choice](record, wallet)


if __name__ == '__main__':
    show_menu()
