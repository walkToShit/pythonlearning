# 语法错误和异常

'''
格式：
try:
    可能出现异常的代码
except:
    如果出现异常则运行的代码
finally:
     无论是否存在异常都会被执行的代码

'''


def cacaulate(a, b, symbol):
    try:
        a = int(a)
        b = int(b)
        if symbol == '+':
            print(a + b)
        elif symbol == '-':
            print(a - b)
        elif symbol == '*':
            print(a * b)
        elif symbol == '/':
            print(a / b)
        with open(r'E:\pythonLearining\file_learn\test.txt', 'r') as rstream:
            print(rstream.read())


    except ValueError as e:
        print('输入字符请', e)  # ,e.__annotations__
    except ZeroDivisionError:
        print('除法分母不能为零')
    except Exception as e:
        print('发生错误的文件：', e.__traceback__.tb_frame.f_globals['__file__'])
        print('错误所在的行号：', e.__traceback__.tb_lineno)
        print('错误信息', e)


cacaulate('1', '1', '/')
cacaulate('1', '1', '/')

print('----------------------')


def testfinally():
    stream = None
    try:
        stream = open(r'E:\pythonLearining\file_learn\aa.txt', 'r')  #a.txt 可以正常走下去
        print(stream.read())
        return 1
    except Exception as e:
        print('发生错误的文件：', e.__traceback__.tb_frame.f_globals['__file__'])
        print('错误所在的行号：', e.__traceback__.tb_lineno)
        print('错误信息', e)
        return 2
    finally:
        if  stream:
           stream.close()
        #return 3

print(testfinally())