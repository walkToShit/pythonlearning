# 递归函数

def sum1(n):
    '''

    :param n:
    :return:
    '''
    sum =1
    if n == 1:
        return sum
    else:
        sum = n + sum1(n - 1)
    return sum


sum1 = sum1(10)
print(sum1)
