class P1:
    def foo(self):
        print('p1-foo')
class P2:
    def foo(self):
        print('p2-foo')
    def bar(self):
        print('p2-bar')
class C1(P1, P2):
    pass
class C2(P1, P2):
    def bar(self):
        print('C2-bar')
class D(C1, C2):
    pass
#mro 返回的多继承调用的顺序
print(D.mro())   #mro Return a type's method resolution order.
print(D.__mro__)
d = D()
d.foo()
d.bar()
