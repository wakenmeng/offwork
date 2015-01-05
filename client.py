import socket
import time

def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('0.0.0.0', 8080))
    while True:
        client.send('hi')
        print client.recv(1024)
        time.sleep(1)

    client.close()

if __name__ == '__main__':
    run_client()
