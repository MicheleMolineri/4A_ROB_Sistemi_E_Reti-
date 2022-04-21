import socket

s,IP_LOOPBACK,IP_PERSONAL,IP_OTHER= socket.socket(socket.AF_INET, socket.SOCK_DGRAM),"127.0.0.1","192.168.","192.168."
s.bind((IP_LOOPBACK, 5000)) 

while True:
    #send the msg to a specific IP
    msg = input("Insert a message: ")
    s.sendto(msg.encode(), (IP_LOOPBACK,5000))
    #receive the msg from a specific IP and print it
    datas, client_address = s.recvfrom(4096) 
    print(f"{datas.decode()} recived from {client_address}")
