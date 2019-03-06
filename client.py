import errno
import os
import socket
import argparse

SERVER_ADDRESS = (HOST, PORT) = 'localhost', 8888
REQUEST_DEMO = b'test'

def main(max_clients, max_conns):
    print(max_clients, max_conns)
    _sockets = list()
    for client_num in range(max_clients):
        pid = os.fork()
        print(pid)
        if pid == 0:
            for connection_num in range(max_conns):
                _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                _socket.connect(SERVER_ADDRESS)
                _socket.sendall(REQUEST_DEMO)
                _sockets.append(_socket)
                print(connection_num)
                os._exit(0)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Test client for webserver',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        'max_clients',
        type=int,
        default=1,
        help='Maximum number of connections per client.'
    )
    parser.add_argument(
        'max_conns',
        type=int,
        default=1024,
        help='Maximum number of connections per client.'
    )
    args = parser.parse_args()
    main(args.max_clients, args.max_conns)