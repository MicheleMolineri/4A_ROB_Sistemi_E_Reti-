import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import matplotlib as mpl


def readFile(fileName, years,total,gasFuel,liquidFuel,solidFuel,cement,gasFlaring,perCapita):
    f = open(fileName,"r")
    lines = f.readlines()

    for line in lines[1:]:
        values = line.split(",")
        years.append(int(values[0]))
        total.append(float(values[1]))
        gasFuel.append(float(values[2]))
        liquidFuel.append(float(values[3]))
        solidFuel.append(float(values[4]))
        cement.append(float(values[5]))
        gasFlaring.append(float(values[6]))
        if int(values[0])>=1950:
            perCapita.append(float(values[7]))
    
    return years,total,gasFuel,liquidFuel,solidFuel,cement,gasFlaring,perCapita

def drawGraphs():

    #Temperature Anomaly graph

    fig,axs = plt.subplots(nrows=2,ncols=1,figsize=(105,95)) 
    fig.subplots_adjust(hspace=0.5)

    cmap = mpl.cm.jet
    nBars = Normalize(vmin=-0.5, vmax=0.750)

    f = open("./Temp.csv","r")
    lines = f.readlines()
    years,temp=[],[]

    for line in lines[5:]:
        values = line.split(",")
        years.append(int(values[0]))
        temp.append(float(values[1]))
        
    axs[0].bar(years, temp, color=cmap(nBars(temp)))
    axs[0].set_title("Temperature anomaly", color="Red",fontsize = 15 )
    axs[0].set_xlabel("Year")
    axs[0].set_ylabel("Degrees (C°)")
    axs[0].grid()

    axs[1].plot(years, temp,'ro',linewidth=1,markersize = 2 )
    axs[1].set_title("Temperature anomaly (dispersive graph)", color="Red",fontsize = 15 )
    axs[1].set_xlabel("Year")
    axs[1].set_ylabel("Degrees (C°)")
    axs[1].grid()

    plt.scatter(years,temp, marker=" ", c = temp, cmap='jet')
    plt.colorbar(ax = axs[0])
    plt.clim(-0.5,0.750)


    #CO2 emissions graph

    years,total,gasFuel,liquidFuel,solidFuel,cement,gasFlaring,perCapita = [],[],[],[],[],[],[],[]
    years,total,gasFuel,liquidFuel,solidFuel,cement,gasFlaring,perCapita = readFile("./CO2_emissions.csv",years,total,gasFuel,liquidFuel,solidFuel,cement,gasFlaring,perCapita)
    
   
    fig,axs = plt.subplots(nrows=2,ncols=2,figsize=(125,255)) 
    fig.subplots_adjust(hspace=0.5)
    
    axs[0][0].plot(years,total,'-',linewidth=1.5,color='#FF4500')
    axs[0,0].bar(years, total,width = 1, color="#FF4500")
    axs[0][0].set_title("Total emissions", color="#FF4500")
    axs[0][0].set_xlabel("Years",color="#FF4500")
    axs[0][0].set_ylabel("Emissions",color="#FF4500")
    axs[0][0].grid()

    axs[0][1].plot(years,gasFuel,'r-',linewidth=1.5,markersize = 2 )
    axs[0][1].set_title("gasFuel emissions", color="Red")
    axs[0][1].set_xlabel("years",color="Red")
    axs[0][1].set_ylabel("Days",color="Red")
    axs[0][1].grid()

    axs[1][0].plot(years,liquidFuel,'y-' ,linewidth=1.5,markersize = 2)
    axs[1][0].set_title("liquid fuel emissions", color="Yellow")
    axs[1][0].set_xlabel("years",color="Yellow")
    axs[1][0].set_ylabel("Emissions",color="Yellow")
    axs[1][0].grid()

    axs[1][1].plot(years,solidFuel,'-',color='#4b0082',linewidth=1.5,markersize = 2)
    axs[1][1].set_title("Solid Fuel emissions", color="Purple")
    axs[1][1].set_xlabel("years",color="Purple")
    axs[1][1].set_ylabel("Emissions",color="Purple")
    axs[1][1].grid()

    fig,axs = plt.subplots(nrows=2,ncols=2,figsize=(95,95))
    fig.subplots_adjust(hspace=0.5)
    
    axs[0][0].plot(years,cement,'go',markersize = 0.5 )
    axs[0][0].plot(years,gasFlaring,'ro',markersize = 1 )
    axs[0,0].plot(years[199:],perCapita,'bo',markersize = 0.5)
    axs[0][0].set_title("Cement production,Gas Flaring,PerCapita", color="Green")
    axs[0][0].set_xlabel("years", color="Green")
    axs[0][0].set_ylabel("Emissions", color="Green")
    axs[0][0].grid()

    axs[0][1].plot(years,cement,'g-',linewidth = 1.5,markersize = 2 )
    axs[0][1].set_title("Cement production", color="Green")
    axs[0][1].set_xlabel("years", color="Green")
    axs[0][1].set_ylabel("Emissions", color="Green")
    axs[0][1].grid()

    axs[1][0].plot(years,gasFlaring,'-', color='#2F4F4F',linewidth = 1.5,markersize = 2 )
    axs[1][0].set_title("Gas Flaring", color="#2F4F4F")
    axs[1][0].set_xlabel("years", color="#2F4F4F")
    axs[1][0].set_ylabel("Emissions", color="#2F4F4F")
    axs[1][0].grid()

    axs[1,1].plot(years[199:],perCapita,'r-',linewidth = 1.5,markersize = 2)
    axs[1,1].set_title("Per Capita", color="Red")
    axs[1,1].set_xlabel("years")
    axs[1,1].set_ylabel("Emissions")
    axs[1,1].grid()

    plt.show()

def main():
    drawGraphs()

if __name__ == "__main__":
    main()