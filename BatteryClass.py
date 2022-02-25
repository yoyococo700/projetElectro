import numpy as np



class BatteryPack:

    def __init__(self, nbS, nbP, capacity, dechargeMaxParElem):
        self.tech = 1
        self.nbS = nbS
        self.nbP = nbP
        self.pOut = 0
        self.capacityMax = capacity
        self.energieMax = capacity * nbS * 3.7
        self.puissanceMaxChargement = self.capacityMax * nbS * 3.7
        self.capacity = 0
        self.dischargeMaxPerElement = dechargeMaxParElem
        self.energie = self.capacity * nbS * 3.7
        self.courantDischargeMaxTotal = capacity * nbP

        self.tabCapacity = []
        self.tabEnergy = []
        self.tab_pOut = []


    def updateCapacityFromEnergy(self):
        self.capacity = self.energie / (3.7 * self.nbS)


    def checkLowBattery(self):
        if self.capacity < 0.2 * self.capacityMax:
            print("La batterie est en dessous de 20 pourcent de sa capacite initial(Capacite initial=",
                  self.capacityMax, "Capacite restante=", self.capacity)

    def charge(self, dt, pDispo):

        pRestante = 0
        pFinal = 0
        TimeConstant = 5

        if (self.energie < 0.8 * self.energieMax):
            if (pDispo>self.puissanceMaxChargement):
                pFinal=self.puissanceMaxChargement
            else:
                pFinal= pDispo
            #print("en charge rapide")

        else:
            pFinal = pDispo*(self.energieMax-self.energie)/self.energieMax

        self.energie+= pFinal*dt
            #print("fin de chargement")

        self.pOut = pDispo - pFinal


    def updateBattery(self, dt, pIn):

        self.charge(dt, pIn)
        self.updateCapacityFromEnergy()
        self.tabCapacity.append(self.getCapacity())
        self.tabEnergy.append(self.getEnergy())
        self.tab_pOut.append(self.get_pOut())





    def getCapacity(self):
        return self.capacity

    def getCapacityNp(self):
        return self.npCapacity

    def getTabCapacity(self):
        return self.tabCapacity

    def printCapacity(self):
        print(self.capacity)

    def getEnergy(self):
        return self.energie

    def getTabEnergy(self):
        return self.tabEnergy

    def get_pOut(self):
        print(self.pOut)
        return self.pOut


    def getTab_pOut(self):
        return self.tab_pOut








