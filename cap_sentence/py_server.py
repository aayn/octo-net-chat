import socket


def main():
    host_name = socket.gethostbyname('0.0.0.0')
    port = 7777
    sock = socket.socket()
    sock.bind((host_name, port))

    sock.listen(2)
    conn, addr = sock.accept()
    print("Connectiion accepted from ", str(addr))

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        data = str(data).upper()
        print("Capped message: ", data)
        conn.send(data.encode())
    conn.close()

if __name__ == '__main__':
    main()
