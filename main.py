from BatteryClass import BatteryPack
import numpy as np
from matplotlib import pyplot as plt


if __name__ == '__main__':

    battery = BatteryPack(4, 1, 3, 50)
    dt=0.1
    t=0

    while t<30:
        battery.updateBattery(dt,70)
        t+=dt

    tabCapacity = battery.getTabCapacity()
    tabEnergy = battery.getTabEnergy()

    plt.plot(tabCapacity)
    plt.plot(tabEnergy)
    plt.plot(battery.getTab_pOut())
    plt.show()


