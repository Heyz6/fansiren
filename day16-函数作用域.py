#coding=utf-8
name="alex"
def foo():
    name="this is foo"
    def bar():
        print(name)
    return bar #return 函数的内存地址,这里需要注意的是 return是和函数同一个缩进级别的
                #拿到内存地址加上个括号就能运行
#foo() #所以要是你直接foo()，调用函数是print不出结果的
foo_1=foo() #所以你要将内存地址赋值给变量
print(foo_1)
foo_1() #将内存地址加() 就代表调用，相当于bar()

#作用域和在哪里调用没关系，和在哪里定义有关系
