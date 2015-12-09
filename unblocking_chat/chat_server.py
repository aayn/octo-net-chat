import socket
import time

hostname = socket.gethostbyname('0.0.0.0')
port = 7777

clients = []

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((hostname, port))

sock.setblocking(0)
quitting = False
print("Server started")

while not quitting:
    try:
        data, addr = sock.recvfrom(1024)
        print("haha")
        if "Quit" in str(data):
            quitting = True
        if addr not in clients:
            clients.append(addr)
        print(time.ctime(time.time()) + str(addr) + ": :" + str(data.decode()))

        for client in clients:
            # print(client)
            # print(data)
            sock.sendto(data, client)
    except:
        pass
sock.close()
