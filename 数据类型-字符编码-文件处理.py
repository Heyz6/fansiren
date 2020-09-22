#coding=utf-8
name="*egon**"
#只能删除存在于字符串两端的符号或者字符
name_1="dassdda a"
print(name.strip("*"))
print(name.lstrip("*"))
print(name.rstrip("*"))
print(name_1.strip("a"))
print(name_1.lstrip("d"))
print(name_1.rstrip("d a"))

name="wangchao"
print(name.lower()) #小写
print(name.upper()) #大写

name='wangchao_sb'
print(name.endswith("sb")) #判断字符串结尾处内容是否存在，存在即True
print(name.startswith("wangcha")) #判断字符串开头处指定内容是否存在，存在即True

print("{} {} {}".format('wangchao',18,'sb'))
print("{1} {0} {1} {2}".format("wangchao",18,"sb"))
print("{name} {age} {sb}".format(name='wangchao',age=90,sb='sb'))

name='root:x:0:0: :/root:/bin/bash'
print(name.split()) #默认分隔符为空格
print(name.split(":"))
print(name.split("/"))
print(name.split("/",1)) #加参代表指定/ 输出的list 前面 1个，后面的作为一个整体不分割
print(name.split("/",2)) #加参代表指定/ 输出的list 前面 2个，后面的作为一个整体不分割

name="a|b|c|d"
print(name.rsplit("|",1)) #从右侧拆分
print(name.rsplit("|",2)) #从右侧拆分

tag='-'
print(tag.join(["wangchao",'18','sb'])) #按照指定字符链接

name="wangchao say :i have one tesla,my name is wangchao"
print(name.replace("wangchao",'SB',1))
print(name.replace("wangchao",'SB',2))
print(name.replace("wangchao",'SB',-1)) #-1 指代所有的出现
#替换字符串中指定 内容，多次出现可使用附加参数，指定修改次数，从左至右

age='123'
print(age.isdigit())
#判断字符串是否全是数字

name="wangchao say hello"
print(name.find("h"))
print(name.find("h",0,10))#0,0 是索引，要是在该范围内则返回第一个位置索引
print(name.find("h",0,200))#后面的所有可变大，不需要准确。
print(name.find("h",0,1)) #要是不在指定的范围内，则返回-1 不会报错

name="wangchao"
print(name.center(30,'-'))
'''返回长度和宽度居中的字符串。
填充使用指定的填充字符(默认为空格)完成。'''
print(name.center(30,"*"))
print(name.ljust(30,"*"))#一侧填充
print(name.rjust(30,'*'))#一侧填充
print(name.zfill(50)) #填充左侧有0的字符串

name="wahngchao\thello"
print(name)
print(name.expandtabs(1))#tab 制表符转换成空格

print(name.capitalize())#首字母大写
print(name.swapcase())#大小写反转

name="wang chao sb"
print(name.title()) #每个单词首字母大写

