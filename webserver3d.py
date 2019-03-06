import socket
import time
import os


SERVER_ADDRESS = (HOST, PORT) = '', 8888
REQUEST_QUEUE_SIZE = 5


def handle_request(connection):
    request = connection.recv(1014)
    response = b"""
HTTP/1.1 200 OK

Hello World!
"""
    connection.sendall(response)
    time.sleep(60)


def start_server():
    _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    _socket.bind(SERVER_ADDRESS)
    _socket.listen(REQUEST_QUEUE_SIZE)
    print('Serving Http on port {0}'.format(PORT))

    while True:
        connection, address = _socket.accept()
        print(address)
        pid = os.fork()
        if pid == 0:
            _socket.close()
            handle_request(connection)
            connection.close()
            os._exit(0)
        else:
            pass
            # connection.close()


if __name__ == '__main__':
    start_server()