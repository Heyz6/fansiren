#coding=utf-8
lambda x:x+1
#第一哥X是形参 X+1是返回值
def calcx(x):
    return x+1
q=calcx(2)
print(q)

a=lambda x:x+10
print(a(1))

name="alex"
def change_name(x):
    return name+"_sb"
a=change_name(name)
print(a)

#lambda 是会自动return的,lamdba是匿名函数，所以不屑函数名，直接写形参，变量
f=lambda x:name+"_sb"
a=f(name)
print(a)

name="alex"
name_1="sbalex"
name_2="superalex"
a=lambda x,y,z:(x+1,y+1,z+1)
print(a(1,2,3))
#def 定义函数的时候，会自动给return组装成元组

#name,name_1,name_2: