#类中的方法
#种类：普通方法  类方法  静态方法  魔术方法

#python 中的属性 分为对象属性和 类属性 java中没有这种说法
'''
普通方法格式:
    def 方法名(self[,参数。。。。])
'''
class Phone:
    brand = 'xiaomi'  #类属性
    price =4999
    type = 'xiaomi10'

    def call(self):
        print(self)
        print('正在打电话。。。')
        print('留言：', self.note)
        print('正在访问通讯录。。。')
        for phone in self.phonebook:
            for key,value in phone.items():
                print(key,value)

phone1 = Phone()
#对象专有属性
phone1.note = 'woshi11111111111111'
phone1.phonebook = [{'156486':'sss'},{'15687846':'gged'}]
print(phone1,'----------1------')
phone1.call()
print('*'*30)
phone2 = Phone()
phone2.note = 'woshi222222222222222'
print(phone2,'----------2------')
phone2.call()

