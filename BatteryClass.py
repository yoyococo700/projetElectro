import numpy as np


class BatteryPack:

    def __init__(self, nbS, nbP, capacityMax, C_rate):
        self.tech = 1
        self.nbS = nbS
        self.voltage = 3.7 * nbS
        self.nbP = nbP
        self.capacityMax = capacityMax
        self.C_rate = C_rate
        self.pTropPlein = 0
        self.capacity = capacityMax * 0.9
        self.currentOut = 0

        self.energieMax = self.capacityMax * self.voltage
        self.puissanceMaxChargement = self.capacityMax * self.voltage

        self.pMaxOut = C_rate * self.capacityMax * self.voltage
        self.energie = self.capacity * self.voltage


        self.tabCapacity = []
        self.tabEnergy = []
        self.tab_pTropPlein = []
        self.tab_Current = []

    def updateCapacityFromEnergy(self):
        self.capacity = self.energie / self.voltage

    def checkLowBattery(self):
        if self.capacity < 0.2 * self.capacityMax:
            print("La batterie est en dessous de 20 pourcent de sa capacite initial(Capacite initial=",
                  self.capacityMax, "Capacite restante=", self.capacity)
            return 1
        return 0

    def charge(self, dt, pDispo):
        pRestante = 0
        pFinal = 0
        TimeConstant = 5

        # Charge rapide
        if (self.energie < 0.8 * self.energieMax):
            if (pDispo > self.puissanceMaxChargement):
                pFinal = self.puissanceMaxChargement
            else:
                pFinal = pDispo

        # Fin de charge
        else:
            pFinal = pDispo * (self.energieMax - self.energie) / self.energieMax

        self.pTropPlein = max(pDispo - pFinal, 0)
        self.energie += pFinal * dt


    def discharge(self,dt,pOut):
        self.energie -= max(pOut - self.pTropPlein, 0) * dt
        self.currentOut = (pOut - self.pTropPlein) / self.voltage

    def chargeOrDischarge(self, dt, tempEnergie):
        print((self.energie - tempEnergie)/dt)

    def updateBattery(self, dt, pIn, pOut):
        tempEnergie = self.energie
        self.charge(dt, pIn)
        self.discharge(dt, pOut)
        self.updateCapacityFromEnergy()

        self.chargeOrDischarge(dt, tempEnergie)

        self.tabCapacity.append(self.getCapacity())
        self.tabEnergy.append(self.getEnergy())
        self.tab_pTropPlein.append(self.get_pTropPlein())
        self.tab_Current.append(self.currentOut)

    def getCapacity(self):
        return self.capacity

    def getTabCapacity(self):
        return self.tabCapacity

    def printCapacity(self):
        print(self.capacity)

    def getEnergy(self):
        return self.energie

    def getTabEnergy(self):
        return self.tabEnergy

    def get_pTropPlein(self):
        return self.pTropPlein

    def getTab_pTropPlein(self):
        return self.tab_pTropPlein
