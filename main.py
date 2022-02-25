from BatteryClass import BatteryPack
import numpy as np
from matplotlib import pyplot as plt


if __name__ == '__main__':

    battery = BatteryPack(4, 1, 3, 50)
    dt=0.1
    t=0

    while t<10 and not battery.checkLowBattery() :
        battery.updateBattery(dt,50,100)
        t+=dt

    tabCapacity = battery.getTabCapacity()
    tabEnergy = battery.getTabEnergy()

    #plt.plot(tabCapacity,"-b", label = "Capacity")
    plt.plot(tabEnergy, label = "Energy")
    plt.plot(battery.getTab_pTropPlein(),"-g", label = "Trop plein batterie")
    plt.plot(battery.tab_Current, "-r", label = "Courant")
    plt.legend(loc="upper right")
    plt.show()


