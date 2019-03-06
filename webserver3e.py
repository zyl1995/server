import socket
import time
import os
import signal


SERVER_ADDRESS = (HOST, PORT) = '', 8888
REQUEST_QUEUE_SIZE = 1

def handle_pid(signum, frame):
    pid, status = os.wait()
    print(
        'child {pid} terminated with status{status}'.format(
            pid=pid, status=status
        )
    )

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

    signal.signal(signal.SIGCHLD, handle_pid)

    while True:
        connection, address = _socket.accept()
        pid = os.fork()
        if pid == 0:
            _socket.close()
            handle_request(connection)
            connection.close()
            os._exit(0)
        else:
            connection.close()


if __name__ == '__main__':
    start_server()