import matplotlib.pyplot as plt

def readFile(fileName, array1,array2):
    f = open(fileName,"r")
    lines = f.readlines()

    for line in lines[1:]:
        values = line.split(",")
        array1.append(values[0])
        array2.append(int(values[1]))
    
    return array1,array2

def generateGraph(arrayX,arrayY,title,xLbl,yLbl):
    fig,ax = plt.subplots(figsize=(10,10)) 

    ax.plot(arrayX,arrayY,'bd')
    ax.set_title(title)
    ax.set_xlabel(xLbl)
    ax.set_ylabel(yLbl)

    plt.bar(arrayX,arrayY)
    plt.show()

def daysInMonth(month,temp):
    jacketDays,videoGameDays,schoolDays =  [],[],[]

    for m in month:
        if m == 'Luglio' or m== 'Agosto':
            schoolDays.append(0)
        elif m == 'Giugno':
            schoolDays.append(7)
        else : schoolDays.append(24)
    for t in temp :
        if t >= 25:
            jacketDays.append(1)
            videoGameDays.append(3)
        elif t<25:
            jacketDays.append(6)
            videoGameDays.append(4)
        elif t<=20:
            jacketDays.append(10)
            videoGameDays.append(4)
        elif t <=15:
            jacketDays.append(20)
            videoGameDays.append(7)
        elif t <=10:
            jacketDays.append(31)
            videoGameDays.append(15)    
    fig,axs = plt.subplots(nrows=2,ncols=2,figsize=(10,10)) 
    
 
    axs[0][0].plot(month,jacketDays,'bd-',linewidth = 2 )
    axs[0][0].set_title("jacket Days")
    axs[0][0].set_xlabel("month")
    axs[0][0].set_ylabel("Days")

    axs[0][1].plot(month,videoGameDays,'ro-',linewidth = 2 )
    axs[0][1].set_title("videoGame Days")
    axs[0][1].set_xlabel("Month")
    axs[0][1].set_ylabel("Days")

    axs[1][0].plot(month,schoolDays,'yo-',linewidth = 2 )
    axs[1][0].set_title("school Days")
    axs[1][0].set_xlabel("Month")
    axs[1][0].set_ylabel("Days")

    axs[1][1].plot(month,temp,'yo-',linewidth = 2 )
    axs[1][1].set_title("Caraglio's Temperatures")
    axs[1][1].set_xlabel("Month")
    axs[1][1].set_ylabel("Temp")

    plt.show()

        

            

def main():
    month,temperature = [],[]
    readFile("./meteo.csv",month,temperature)
    daysInMonth(month,temperature)


if __name__=="__main__":
    main()