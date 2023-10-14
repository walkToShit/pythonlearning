def function1(num1,num2):
    '''返回加减乘数据'''
    add = num1+num2;
    sub = num1-num2;
    mul = num1*num2;
    return add,sub,mul;

param1,param2,param3 = function1(3,4);  #使用对应数量的变量接收返回
para4,*para5 = function1(5,6);          #使用封包的方式接收返回
print(param1,param2,param3,para4,para5);