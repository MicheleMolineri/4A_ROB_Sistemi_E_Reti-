import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("192.168.0.133",5000))

while True:
    msg,ind_client = s.recvfrom(4096)
    print(msg.decode())
    msg = input("Inserisci messaggio: ")
    s.sendto(msg.encode(),ind_client)