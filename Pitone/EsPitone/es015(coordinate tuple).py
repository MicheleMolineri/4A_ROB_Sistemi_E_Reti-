x1,y1,x2,y2=float(input("Inserire la cordinata x1 : ")),float(input("Inserire la cordinata y1 : ")),float(input("Inserire la cordinata x2 : ")),float(input("Inserire la cordinata y2 : "))
punto1,punto2=(x1,y1),(x2,y2) # assegnamento tuple
diffX,diffY=punto2[0]-punto1[0],punto2[1]-punto1[1]
dist=(diffY**2 + diffX **2)**(1/2)
print(dist)