from V1 import BatteryPack
import numpy as np
from matplotlib import pyplot as plt

def print_hi(name):

    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    battery = BatteryPack(4, 1, 3, 50)
    dt=0.1
    t=0
    essai = np.array([0,1,2,3,4])
    while t<360:
        battery.updateBattery(dt,50,60)
        t+=dt

    tab = battery.getTabCapacity()
    f= np.array(tab)
    plt.plot(tab)
    plt.show()


