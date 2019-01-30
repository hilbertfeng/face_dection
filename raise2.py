# raise.py

# 本示例示意用raise语句来传递错误信息


def f1():
    n = int(input("请输入整数： "))



def f2():

    try:
        f1()
    except ValueError as err:
        print("f1函数被调用")
        print("f2里的err=", err)
        raise

try:
    f2()
except ValueError as err:
    print("f2内发生了ValueError类型错误")
    print("err=", err)
print("test raise2")
>>>>>> Jame_dev
