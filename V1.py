import numpy as np



class BatteryPack:

    def __init__(self, nbS, nbP, capacity, dechargeMaxParElem):
        self.tech = 1
        self.nbS = nbS
        self.nbP = nbP
        self.capacityMax = capacity
        self.energieMax = capacity * nbS * 3.7
        self.capacity = 0
        self.dischargeMaxPerElement = dechargeMaxParElem
        self.energie = capacity * nbS * 3.7
        self.courantDischargeMaxTotal = capacity * nbP

        self.tabCapacity = []


    def checkLowBattery(self):
        if self.capacity < 0.2 * self.capacityMax:
            print("La batterie est en dessous de 20 pourcent de sa capacite initial(Capacite initial=",
                  self.capacityMax, "Capacite restante=", self.capacity)

    def charge(self, dt, pDispo):
        if self.capacity < 0.8 * self.capacityMax:
            self.capacity += max((pDispo / (3.7 * self.nbS)) * dt, 2 * self.capacityMax * dt)
            print("en charge rapide")

    def updateBattery(self, dt, pIn, pOut):

        self.tabCapacity.append(self.capacity)
        self.charge(dt, 50)
        print(self.capacity)


    def getcapacity(self):
        return self.capacity

    def getCapacityNp(self):
        return self.npCapacity

    def getTabCapacity(self):
        return self.tabCapacity

    def printCapacity(self):
        print(self.capacity)








