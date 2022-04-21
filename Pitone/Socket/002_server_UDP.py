import socket

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("192.168.0.130",5000))#solo nel server
dati, indirizzo_client=s.recvfrom(4096)
while(dati.decode()!="exit"):
    print(f"{dati.decode()} ")#ricevuti da {indirizzo_client}")
    dati, indirizzo_client=s.recvfrom(4096)
