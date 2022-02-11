import socket
import turtle

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

IP = socket.gethostbyname(socket.gethostname())

PORT = 8888

s.bind((IP,PORT))

print("Server on, waiting for client call")

while True:
    data, addr = s.recvfrom(1024)
    data = data.decode()
    print(f'Info received is: {data}')
    if data.lower() == 'exit':
        break

s.close()
