from socket import *
import os, sys


def client_handler(c):
    print("客户端：", c.getpeername())
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b"Thank you!")
    c.close()

# 创建套接字
s = socket()  # 创建TCP套接字

HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(5)



# 循环等到接收客户端连接请求
print("Listen to the port 8888")
while True:
    try:
       c, addr = s.accept()

    except KeyboardInterrupt as e:
        print(e)
        sys.exit('退出服务器')
    except Exception as e:
        print("Error:", e)
        continue

    # 创建新的进程处理客户端请求
    pid = os.fork()
    if pid == 0:

        p = os.fork()
        if p == 0:

            s.close()
            client_handler(c)
            sys.exit(0) # 子进程处理完进程即退出
        else:
            os._exit(0)
    # 父进程或者创建进程失败都继续等待客户端连接
    else:
        c.close()
        os.wait()



##