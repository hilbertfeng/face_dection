# try-finally.py

# 此示例以前煎鸡蛋

def fry_egg():
    print("打开天然气点燃...")
    try:
        try:
            count = int(input("请输入鸡蛋个数: "))
            print("完成煎鸡蛋", count)
        finally:
            print("关闭天然气")
    except ValueError:
        print("煎鸡蛋失败")


fry_egg()
