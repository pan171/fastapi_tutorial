# web 应用程序：遵循 HTTP 协议 —— 先有请求，才有反应
import socket

sock = socket.socket()

sock.bind(("127.0.0.1", 8080))
sock.listen(5)

while 1:
    conn, addr = sock.accept()  # 阻塞等待客户连接，coon 全双工管道
    data = conn.recv(1024)  # 客户端发送数据
    print("客户端发送的请求信息:\n", data)
    conn.send(
        b"HTTP/1.1 200 ok\r\nserver:panzhonglu\r\ncontent-type:text/html\r\n\r\n<h1>hello world</h1>"
    )
    conn.close()
