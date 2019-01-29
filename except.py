# except.py

def f1():
    '''此函数可能触发错误'''
    s = "这是错误信息"
    raise ValueError(s)

def f2():
    f1()

def f3():
    f2()

def f4():
    f3()

try:
    f4()
except ValueError as err:
    print('err=', err)

