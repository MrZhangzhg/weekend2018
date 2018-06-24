from getpass import getpass

userdb = {}

def register():
    username = input('用户名: ').strip()
    if username in userdb:
        print('\033[31;1m用户已存在\033[0m')
    else:
        password = input('密码: ')
        userdb[username] = password
        print('\033[32;1m创建成功\033[0m')

def login():
    username = input('用户名: ')
    password = getpass('密码: ')
    # if (username not in userdb) or (userdb[username] != password):
    if userdb.get(username) != password:
        print('登陆失败')
    else:
        print('登陆成功')

def show_menu():
    cmds = {'0': register, '1': login}
    prompt = """(0) 注册
(1) 登陆
(2) 退出
请选择(0/1/2): """
    while True:
        choice = input(prompt).strip()[0]
        if choice not in '012':
            print('无效输入，请重试')
            continue
        if choice == '2':
            break
        cmds[choice]()

if __name__ == '__main__':
    show_menu()
