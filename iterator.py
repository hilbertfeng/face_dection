# iterator.py
# 此示例示意用迭代器遍历一个列表
L = [2, 3, 5, 7]
# 循环从可迭代器中获取数据，直到数据接收到StopIteration异常为止
it = iter(L)

while True:
    
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break
