import socket
import time

def run_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', 8080))
    sock.listen(5)
    client, addr = sock.accept()
    while(True):
        msg = client.recv(1024)
        print msg
        client.send('from server %s' % msg)
        time.sleep(1)
    client.close()
    sock.close()

if __name__ == '__main__':
    run_server()
