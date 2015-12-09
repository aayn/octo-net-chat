import socket
import threading
import time

t_lock = threading.Lock()
shutdown = False


def receiving(name, sock):
    while not shutdown:
        try:
            t_lock.acquire()
            while True:
                data, addr = sock.recvfrom(1024)
                print(str(data.decode()))
        except:
            pass
        finally:
            t_lock.release()

host_ip = socket.gethostbyname('0.0.0.0')
port = 0
server = ('192.168.1.5', 7777)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host_ip, port))
sock.setblocking(0)

rec_thread = threading.Thread(target=receiving, args=("RecvThread", sock))
rec_thread.start()

alias = input("Enter nickname: ")
message = input(alias + '-->')

while message != 'q':
    if message != '':
        sock.sendto((alias + ": " + message).encode(), server)
        t_lock.acquire()
        message = input(alias + '-->')
        t_lock.release()
        time.sleep(0.2)

shutdown = True
rec_thread.join()
sock.close()
