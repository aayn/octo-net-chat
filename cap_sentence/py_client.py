import socket


def main():
    host = '127.0.0.1'
    port = 7777

    sock = socket.socket()
    sock.connect((host, port))

    mssg = input('-->')
    while mssg != 'q':
        sock.send(mssg.encode())
        data = sock.recv(1024).decode()
        print('Received from server: ', str(data))
        mssg = input('-->')
    sock.close()

if __name__ == '__main__':
        main()
