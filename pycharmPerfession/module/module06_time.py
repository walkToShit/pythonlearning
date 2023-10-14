import datetime
import time

t = time.time()  #获得的是时间戳
print(t)
time.sleep(3)
t1 = time.time()
print(t1)

#将时间戳转换为字符串
s = time.ctime(t)
print(s)
#时间戳转元组
s2 = time.localtime(t)
print(s2)
print(type(s2)) #<class 'time.struct_time'>
print('{}年{}月{}日{}时{}分{}秒'.format(s2.tm_year,s2.tm_mon,s2.tm_mday,s2.tm_hour,s2.tm_min,s2.tm_sec))
s1 = time.gmtime()  #utc 0时区的函数
print(s1)

#元组转时间戳
tt = time.mktime(s2)  #转换后时区小数点后精度
print(tt)


rightnow = time.strftime('%Y-%m-%d %H:%M:%S')  #按格式转换时间
print(rightnow)
print(time.strptime(rightnow,'%Y-%m-%d %H:%M:%S'))#按格式转换时间
'''
time模块：
  重点：
  time()
  sleep()
  strftime(格式)
'''

print(datetime.time.hour)

print(datetime.date.today())
print(datetime.datetime.now())
# 时间差
timeinterval = datetime.timedelta(days=3)
print(timeinterval)