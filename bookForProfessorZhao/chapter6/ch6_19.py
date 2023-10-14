string = "    Python.学习手册.上  ";    # 声明一个字符串
print(string);                        # 打印原始字符串
print("字符串大写  "+string.upper());
print("字符串小写  "+string.lower());
print("首字母大写"+"     aaaaaa".title());
print("删除左侧端字符串空白:"+string.lstrip());
print("没有删除右端字符串空白  "+string+"a");
print("删除右端字符串空白  "+string.rstrip()+"a");
print("删除两端端字符串空白  :"+string.strip()+"a");
print("打印原字符串"+string);            # 以上方法没有改变原始字符串
print("字符串长度%d"%len(string));
print("字符串字符的最大值:"+max(string));
print("字符串字符的最小值:"+min(string));
for x in string:
    print(ord(x),end ='-');