import socket
import time


SERVER_ADDRESS = (HOST, PORT) = '', 8888
REQUEST_QUEUE_SIZE = 5


def handle_request(connection):
    request = connection.recv(1014)
    response = b"""
HTTP/1.1 200 OK

Hello World!
"""
    connection.sendall(response)


def start_server():
    _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    _socket.bind(SERVER_ADDRESS)
    _socket.listen(REQUEST_QUEUE_SIZE)
    print('Serving Http on port {0}'.format(PORT))

    while True:
        connection, address = _socket.accept()
        handle_request(connection)
        connection.close()


if __name__ == '__main__':
    start_server()
