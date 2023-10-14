'''
生成器方法：
  __next__(): 获取下一个元素
  send(value):向每次生成器调用中传值
  Resumes the generator and "sends" a value that becomes the result of the current yield-expression.

'''
def gen():
    i = 0
    while i < 5:
        temp = yield i
        print('temp', temp)
        i += 1
        if temp:
            for x in temp:
                print(x)
    return '没有更多的数据了'


g = gen();
print(next(g))
n1 = g.send('呵呵')
print('n1:', n1)
n2 = g.send('哈哈')
print('n2:', n2)

for i in range(10):
    print(g.__next__())


