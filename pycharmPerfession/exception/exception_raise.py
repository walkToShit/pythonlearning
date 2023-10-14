#抛出异常

#注册 用户没那个必须六位

def register():
    username = input('输入用户名')
    if len(username)<6:
        raise Exception('用户名必须六位以上')
    else:
        print('输入的用户名是{}'.format(username))

try:
    register()
except Exception as e:
    print(e.__traceback__.tb_frame)
    print('注册失败00')
else:
    print("注册成功")
