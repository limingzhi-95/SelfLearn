# coding:utf-8

import socket

EOL1 = '\n\n'
EOL2 = '\n\r\n'
body = '''Hello world! <h1> from self learn </h1>'''
response_params = [
    'HTTP/1.0 200 OK',
    'Date: Sat, 10 jun 2019 01:01:01 GMT',
    'Content-Type: text/html; charset=utf-8',
    'Content-Length: {}\r\n'.format(len(body)),
    body
]
response = b'\r\n'.join(response_params)


def handle_connection(conn, addr):
    request = ""
    while EOL1 not in request and EOL2 not in request:
        request += conn.recv(1024)
    print(request)
    conn.send(response)
    conn.close()


def main():
    """
    Python支持的3种地址族。最常见的AF_INET，用于IPv4的互联网寻址。几乎目前所有互联网联网使用IP版本4。AF_INET6 用于IPv6互联网寻址。
    IPv6是“下一代”版本的互联网协议。它支持128位的地址，流量控制和IPv4不支持的路由功能。IPv6有限使用，但继续 增长。
    AF_UNIX是UNIX域套接字（UDS），是POSIX兼容的系统上进程间的通信协议。UDS的实现通常允许操作系统不用通过网络堆栈在进程间 直接通信。
    这比使用AF_INET更高效，但使用文件系统被作为命名空间进行寻址，UDS限制在同一系统。吸引力在于在IPC使用UDS，
    比如命名管道或 共享内存的编程接口和IP网络一致。这应用程序可以使用网络通信同样的代码在单机上实现有效的通信机制。
    套接字类型通常是为SOCK_DGRAM用户数据 报协议（UDP）或SOCK_STREAM传输控制协议（TCP）。
    tcp一般用户传送大量数据，udp一般用于传送少量数据或者多播
    :return:
    """
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口可复用
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 三个值分别为要对哪一层进行设置,设置哪个选项,设置为哪个值
    serversocket.bind(('127.0.0.1', 8080))
    serversocket.listen(1)
    print('http://127.0.0.1:8080')

    try:
        while True:
            conn, address = serversocket.accept()
            handle_connection(conn, address)
    finally:
        serversocket.close()


if __name__ == '__main__':
    main()
