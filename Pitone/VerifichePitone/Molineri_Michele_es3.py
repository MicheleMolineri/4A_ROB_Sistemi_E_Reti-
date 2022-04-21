ip_address=["192.168.222.0/27","192,168.100.0/24","192.168.200.0/28","192.168.50.0/22"]

f=open("./file.txt","w")

for mask in range(4):
    f.write("Mask = "+ip_address[mask][-3:]+"\n")  #scrivo le ultrime 3 lettere della stringa
