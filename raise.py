# raise.py

# 发送错误通知给调用者

def make_except():
    print("开始。。。")
    '''
    raise ValueError   # 触发ValueError类型的错误
    raise ZeroDivisionError
    raise ImportError
    raise IndexError
    '''

    # 创建一个错误对象用error来绑定
    error = ValueError('XXX大街YYY号着火了')
    raise error  # 触发ValueError的错误通知
    print("结束！！！")

try:
    make_except()
    print("make_except 调用完成")
except ValueError as err:
    print("收到 ValueError类型的错误通知")
    print("err=", err)
except ZeroDivisionError:
    print("被零除！！！")

print("程序正常结束")
print("end test")
print("end test2")
