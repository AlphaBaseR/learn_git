import socket

IP = '127.0.0.1'

PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    toSend = input(">>>")
    s.sendto(toSend.encode(),(IP,PORT))
    if toSend == "exit" :
        break

s.close()
