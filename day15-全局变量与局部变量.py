#coding=utf-8
print("你好，我的名字叫 %s,我的年龄是 %s"%("老瓦","18"))
print("年收入 %d W"%(500))

name="wangchao"
passwd="123123"
# while True:
#     name_1=input("输入账户名>>:")
#     passwd_1=input("输入密码>>:")
#     if name_1 == name and passwd_1 == passwd:
#         while True:
#             cmd=input("》》：")
#             if not cmd:
#                 continue
#                 if cmd == "quit":
#                     break
#                 print("run <%s>"%cmd)
#             else:
#                 print("用户名或者密码错误")
#                 continue
#             break

#
# while True:
#     print("123")
#     break
#     print("456")

# while True:
#     print("123")
#     continue
#     print("456")
#

for i in range(1,10):
    for j in range(1,i+1):
        print('%s*%s=%s' %(i,j,i*j),end=' ')
    print()

name='*egon**'
print(name.strip('*'))
print(name.lstrip('*'))
print(name.rstrip('*'))

name='egon'
print(name.lower())
print(name.upper())

name='alex_SB'
print(name.endswith('SB'))
print(name.startswith('alex'))


res='{} {} {}'.format('egon',18,'male')
print(res)
res='{1} {0} {1}'.format('egon',18,'male')
print(res)
res='{name} {age} {sex}'.format(sex='male',name='egon',age=18)
print(res)
res='{0} {1} {1}'.format('egon',18,'male')
print(res)


name='root:x:0:0::/root:/bin/bash'
print(name.split(':')) #默认分隔符为空格
name='C:/a/b/c/d.txt' #只想拿到顶级目录
print(name.split('/',2))

name='a|b|c'
print(name.rsplit('|',1)) #从右开始切分

#join
tag=' '
print(tag.join(['egon','say','hello','world'])) #可迭代对象必须都是字符串

#replace
name='alex say :i have one tesla,my name is alex'
print(name.replace('alex','SB',1))

#isdigit：可以判断bytes和unicode类型,是最常用的用于于判断字符是否为"数字"的方法
# age=input('>>: ')
# print(age.isdigit())

# #掌握
# f.read() #读取所有内容,光标移动到文件末尾
# f.readline() #读取一行内容,光标移动到第二行首部
# f.readlines() #读取每一行内容,存放于列表中
#
# f.write('1111\n222\n') #针对文本模式的写,需要自己写换行符
# f.write('1111\n222\n'.encode('utf-8')) #针对b模式的写,需要自己写换行符
# f.writelines(['333\n','444\n']) #文件模式
# f.writelines([bytes('333\n',encoding='utf-8'),'444\n'.encode('utf-8')]) #b模式
#
# #了解
# f.readable() #文件是否可读
# f.writable() #文件是否可读
# f.closed #文件是否关闭
# f.encoding #如果文件打开模式为b,则没有该属性
# f.flush() #立刻将文件内容从内存刷到硬盘
# f.name

# import sys
# sys.argv


menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}


#part2（改进）：加上退出机制
layers=[menu,]
print(type(layers))
while True:
    if len(layers) == 0: break
    current_layer=layers[-1]

    for key in current_layer:
        print(key)

    choice=input('>>: ').strip()

    if choice == 'b':
        layers.pop(-1)
        continue
    if choice == 'q':break

    if choice not in current_layer:continue

    layers.append(current_layer[choice])