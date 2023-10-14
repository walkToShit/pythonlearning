'''

步骤： 1.定义一个函数，  函数中使用yield 关键字
      2.调用函数，接受调用结果
      3.得到的结果就是生成器
      4.借助于 next() 或者 __next() 来得到元素

'''


def func():
    n = 0
    while True:
        n += 1
        yield n  # 相当于return + 暂停


g = func()
print(g)
for i in range(4):
    print(g.__next__())
print('------------------分割-----------------------------------')


def fib(length):
    a, b = 0, 1
    n = 0
    while n < length:
        yield b  # 相当于return + 暂停
        a, b = b, a + b
        n += 1
    return '没有更过元素了'  # return就是得到StopIteration 提示信息


t = fib(8)
#print(t.send(None))
#print(t.send(3))
try:
    for i in range(9):
        print(next(t))
except StopIteration as e:
    print('发生错误的文件：', e.__traceback__.tb_frame.f_globals['__file__'])
    print('错误所在的行号：', e.__traceback__.tb_lineno)
    print('错误信息', e)
