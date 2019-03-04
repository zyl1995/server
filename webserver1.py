import socket
# 地址,端口
host, port = '', 8888
# 支持ip协议类型
IS_IPV4 = socket.AF_INET
# 协议类型
IS_TCP = socket.SOCK_STREAM

_socket = socket.socket(IS_IPV4, IS_TCP)
# 允许重用本地地址, 一般来说关闭socket, 不会立即关闭，　而是经历time_wait过程,而这是允许再次重用该socket
_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 绑定组成的地址族
_socket.bind((host, port))
# 监听socket,　1代表最多可挂起的连接数
_socket.listen(1)
print('listen port with {0}'.format(port))
while True:
    _connect, _address = _socket.accept()
    # 读请求,socket读缓存区
    request = _connect.recv(1024)
    print(request)
    # 遵从http报文的格式
    response = b"""
HTTP/1.1 200 OK

hello world
"""
    # 发送响应, socket写缓存区
    _connect.sendall(response)
    # 关闭连接
    _connect.close()



