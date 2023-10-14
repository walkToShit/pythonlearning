def function1(num1,num2):
    '''返回加减乘数据'''
    add = num1+num2;
    sub = num1-num2;
    mul = num1*num2;
    return add,sub,mul;

rmg = function1(1,2);
print(rmg)