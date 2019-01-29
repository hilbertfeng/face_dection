# try_exception.py

# 此示例示意异常捕捉的过程
def div_apple(n):

    print("%d你想分给几个人" % n)
    s = input("请输入人数： ")
    count = int(s)  # 可能触发 Value Error
    result = n / count  # 可能触发ZeroDivisionError错误
    print("每个人分了", result, '个苹果')


try:
    div_apple(10)
    print("苹果分配成功")

except (ValueError) as err:
    print("分苹果失败，苹果被收回 err=", err)
else:
    print("此语句没有发生异常，此语句在没有发生异常时才能被执行")



print("程序结束")