import numpy as np
import matplotlib.pyplot as plt

fiveSizes = [1./10,1./20,1./30,1./40,1./50]

dataL0g0010011010 = np.genfromtxt('./L0/gK001/aK001/S1/N010/HamVals.txt')

MomentumAxL0g0010011010 = dataL0g0010011010[:,][:,5*0+0]
KineticEneL0g0010011010 = dataL0g0010011010[:,][:,5*0+1]
SelfEnergyL0g0010011010 = dataL0g0010011010[:,][:,5*0+2]
EigenValReL0g0010011010 = dataL0g0010011010[:,][:,5*0+3]
EigenValImL0g0010011010 = dataL0g0010011010[:,][:,5*0+4]

dataL0g0010011020 = np.genfromtxt('./L0/gK001/aK001/S1/N020/HamVals.txt')

MomentumAxL0g0010011020 = dataL0g0010011020[:,][:,5*0+0]
KineticEneL0g0010011020 = dataL0g0010011020[:,][:,5*0+1]
SelfEnergyL0g0010011020 = dataL0g0010011020[:,][:,5*0+2]
EigenValReL0g0010011020 = dataL0g0010011020[:,][:,5*0+3]
EigenValImL0g0010011020 = dataL0g0010011020[:,][:,5*0+4]

dataL0g0010011030 = np.genfromtxt('./L0/gK001/aK001/S1/N030/HamVals.txt')

MomentumAxL0g0010011030 = dataL0g0010011030[:,][:,5*0+0]
KineticEneL0g0010011030 = dataL0g0010011030[:,][:,5*0+1]
SelfEnergyL0g0010011030 = dataL0g0010011030[:,][:,5*0+2]
EigenValReL0g0010011030 = dataL0g0010011030[:,][:,5*0+3]
EigenValImL0g0010011030 = dataL0g0010011030[:,][:,5*0+4]

dataL0g0010011040 = np.genfromtxt('./L0/gK001/aK001/S1/N040/HamVals.txt')

MomentumAxL0g0010011040 = dataL0g0010011040[:,][:,5*0+0]
KineticEneL0g0010011040 = dataL0g0010011040[:,][:,5*0+1]
SelfEnergyL0g0010011040 = dataL0g0010011040[:,][:,5*0+2]
EigenValReL0g0010011040 = dataL0g0010011040[:,][:,5*0+3]
EigenValImL0g0010011040 = dataL0g0010011040[:,][:,5*0+4]

dataL0g0010011050 = np.genfromtxt('./L0/gK001/aK001/S1/N050/HamVals.txt')

MomentumAxL0g0010011050 = dataL0g0010011050[:,][:,5*0+0]
KineticEneL0g0010011050 = dataL0g0010011050[:,][:,5*0+1]
SelfEnergyL0g0010011050 = dataL0g0010011050[:,][:,5*0+2]
EigenValReL0g0010011050 = dataL0g0010011050[:,][:,5*0+3]
EigenValImL0g0010011050 = dataL0g0010011050[:,][:,5*0+4]

dataL0g0010021010 = np.genfromtxt('./L0/gK001/aK002/S1/N010/HamVals.txt')

MomentumAxL0g0010021010 = dataL0g0010021010[:,][:,5*0+0]
KineticEneL0g0010021010 = dataL0g0010021010[:,][:,5*0+1]
SelfEnergyL0g0010021010 = dataL0g0010021010[:,][:,5*0+2]
EigenValReL0g0010021010 = dataL0g0010021010[:,][:,5*0+3]
EigenValImL0g0010021010 = dataL0g0010021010[:,][:,5*0+4]

dataL0g0010021020 = np.genfromtxt('./L0/gK001/aK002/S1/N020/HamVals.txt')

MomentumAxL0g0010021020 = dataL0g0010021020[:,][:,5*0+0]
KineticEneL0g0010021020 = dataL0g0010021020[:,][:,5*0+1]
SelfEnergyL0g0010021020 = dataL0g0010021020[:,][:,5*0+2]
EigenValReL0g0010021020 = dataL0g0010021020[:,][:,5*0+3]
EigenValImL0g0010021020 = dataL0g0010021020[:,][:,5*0+4]

dataL0g0010021030 = np.genfromtxt('./L0/gK001/aK002/S1/N030/HamVals.txt')

MomentumAxL0g0010021030 = dataL0g0010021030[:,][:,5*0+0]
KineticEneL0g0010021030 = dataL0g0010021030[:,][:,5*0+1]
SelfEnergyL0g0010021030 = dataL0g0010021030[:,][:,5*0+2]
EigenValReL0g0010021030 = dataL0g0010021030[:,][:,5*0+3]
EigenValImL0g0010021030 = dataL0g0010021030[:,][:,5*0+4]

dataL0g0010021040 = np.genfromtxt('./L0/gK001/aK002/S1/N040/HamVals.txt')

MomentumAxL0g0010021040 = dataL0g0010021040[:,][:,5*0+0]
KineticEneL0g0010021040 = dataL0g0010021040[:,][:,5*0+1]
SelfEnergyL0g0010021040 = dataL0g0010021040[:,][:,5*0+2]
EigenValReL0g0010021040 = dataL0g0010021040[:,][:,5*0+3]
EigenValImL0g0010021040 = dataL0g0010021040[:,][:,5*0+4]

dataL0g0010021050 = np.genfromtxt('./L0/gK001/aK002/S1/N050/HamVals.txt')

MomentumAxL0g0010021050 = dataL0g0010021050[:,][:,5*0+0]
KineticEneL0g0010021050 = dataL0g0010021050[:,][:,5*0+1]
SelfEnergyL0g0010021050 = dataL0g0010021050[:,][:,5*0+2]
EigenValReL0g0010021050 = dataL0g0010021050[:,][:,5*0+3]
EigenValImL0g0010021050 = dataL0g0010021050[:,][:,5*0+4]

dataL0g0010051010 = np.genfromtxt('./L0/gK001/aK005/S1/N010/HamVals.txt')

MomentumAxL0g0010051010 = dataL0g0010051010[:,][:,5*0+0]
KineticEneL0g0010051010 = dataL0g0010051010[:,][:,5*0+1]
SelfEnergyL0g0010051010 = dataL0g0010051010[:,][:,5*0+2]
EigenValReL0g0010051010 = dataL0g0010051010[:,][:,5*0+3]
EigenValImL0g0010051010 = dataL0g0010051010[:,][:,5*0+4]

dataL0g0010051020 = np.genfromtxt('./L0/gK001/aK005/S1/N020/HamVals.txt')

MomentumAxL0g0010051020 = dataL0g0010051020[:,][:,5*0+0]
KineticEneL0g0010051020 = dataL0g0010051020[:,][:,5*0+1]
SelfEnergyL0g0010051020 = dataL0g0010051020[:,][:,5*0+2]
EigenValReL0g0010051020 = dataL0g0010051020[:,][:,5*0+3]
EigenValImL0g0010051020 = dataL0g0010051020[:,][:,5*0+4]

dataL0g0010051030 = np.genfromtxt('./L0/gK001/aK005/S1/N030/HamVals.txt')

MomentumAxL0g0010051030 = dataL0g0010051030[:,][:,5*0+0]
KineticEneL0g0010051030 = dataL0g0010051030[:,][:,5*0+1]
SelfEnergyL0g0010051030 = dataL0g0010051030[:,][:,5*0+2]
EigenValReL0g0010051030 = dataL0g0010051030[:,][:,5*0+3]
EigenValImL0g0010051030 = dataL0g0010051030[:,][:,5*0+4]

dataL0g0010051040 = np.genfromtxt('./L0/gK001/aK005/S1/N040/HamVals.txt')

MomentumAxL0g0010051040 = dataL0g0010051040[:,][:,5*0+0]
KineticEneL0g0010051040 = dataL0g0010051040[:,][:,5*0+1]
SelfEnergyL0g0010051040 = dataL0g0010051040[:,][:,5*0+2]
EigenValReL0g0010051040 = dataL0g0010051040[:,][:,5*0+3]
EigenValImL0g0010051040 = dataL0g0010051040[:,][:,5*0+4]

dataL0g0010051050 = np.genfromtxt('./L0/gK001/aK005/S1/N050/HamVals.txt')

MomentumAxL0g0010051050 = dataL0g0010051050[:,][:,5*0+0]
KineticEneL0g0010051050 = dataL0g0010051050[:,][:,5*0+1]
SelfEnergyL0g0010051050 = dataL0g0010051050[:,][:,5*0+2]
EigenValReL0g0010051050 = dataL0g0010051050[:,][:,5*0+3]
EigenValImL0g0010051050 = dataL0g0010051050[:,][:,5*0+4]

dataL0g0010101010 = np.genfromtxt('./L0/gK001/aK010/S1/N010/HamVals.txt')

MomentumAxL0g0010101010 = dataL0g0010101010[:,][:,5*0+0]
KineticEneL0g0010101010 = dataL0g0010101010[:,][:,5*0+1]
SelfEnergyL0g0010101010 = dataL0g0010101010[:,][:,5*0+2]
EigenValReL0g0010101010 = dataL0g0010101010[:,][:,5*0+3]
EigenValImL0g0010101010 = dataL0g0010101010[:,][:,5*0+4]

dataL0g0010101020 = np.genfromtxt('./L0/gK001/aK010/S1/N020/HamVals.txt')

MomentumAxL0g0010101020 = dataL0g0010101020[:,][:,5*0+0]
KineticEneL0g0010101020 = dataL0g0010101020[:,][:,5*0+1]
SelfEnergyL0g0010101020 = dataL0g0010101020[:,][:,5*0+2]
EigenValReL0g0010101020 = dataL0g0010101020[:,][:,5*0+3]
EigenValImL0g0010101020 = dataL0g0010101020[:,][:,5*0+4]

dataL0g0010101030 = np.genfromtxt('./L0/gK001/aK010/S1/N030/HamVals.txt')

MomentumAxL0g0010101030 = dataL0g0010101030[:,][:,5*0+0]
KineticEneL0g0010101030 = dataL0g0010101030[:,][:,5*0+1]
SelfEnergyL0g0010101030 = dataL0g0010101030[:,][:,5*0+2]
EigenValReL0g0010101030 = dataL0g0010101030[:,][:,5*0+3]
EigenValImL0g0010101030 = dataL0g0010101030[:,][:,5*0+4]

dataL0g0010101040 = np.genfromtxt('./L0/gK001/aK010/S1/N040/HamVals.txt')

MomentumAxL0g0010101040 = dataL0g0010101040[:,][:,5*0+0]
KineticEneL0g0010101040 = dataL0g0010101040[:,][:,5*0+1]
SelfEnergyL0g0010101040 = dataL0g0010101040[:,][:,5*0+2]
EigenValReL0g0010101040 = dataL0g0010101040[:,][:,5*0+3]
EigenValImL0g0010101040 = dataL0g0010101040[:,][:,5*0+4]

dataL0g0010101050 = np.genfromtxt('./L0/gK001/aK010/S1/N050/HamVals.txt')

MomentumAxL0g0010101050 = dataL0g0010101050[:,][:,5*0+0]
KineticEneL0g0010101050 = dataL0g0010101050[:,][:,5*0+1]
SelfEnergyL0g0010101050 = dataL0g0010101050[:,][:,5*0+2]
EigenValReL0g0010101050 = dataL0g0010101050[:,][:,5*0+3]
EigenValImL0g0010101050 = dataL0g0010101050[:,][:,5*0+4]

dataL0g0010201010 = np.genfromtxt('./L0/gK001/aK020/S1/N010/HamVals.txt')

MomentumAxL0g0010201010 = dataL0g0010201010[:,][:,5*0+0]
KineticEneL0g0010201010 = dataL0g0010201010[:,][:,5*0+1]
SelfEnergyL0g0010201010 = dataL0g0010201010[:,][:,5*0+2]
EigenValReL0g0010201010 = dataL0g0010201010[:,][:,5*0+3]
EigenValImL0g0010201010 = dataL0g0010201010[:,][:,5*0+4]

dataL0g0010201020 = np.genfromtxt('./L0/gK001/aK020/S1/N020/HamVals.txt')

MomentumAxL0g0010201020 = dataL0g0010201020[:,][:,5*0+0]
KineticEneL0g0010201020 = dataL0g0010201020[:,][:,5*0+1]
SelfEnergyL0g0010201020 = dataL0g0010201020[:,][:,5*0+2]
EigenValReL0g0010201020 = dataL0g0010201020[:,][:,5*0+3]
EigenValImL0g0010201020 = dataL0g0010201020[:,][:,5*0+4]

dataL0g0010201030 = np.genfromtxt('./L0/gK001/aK020/S1/N030/HamVals.txt')

MomentumAxL0g0010201030 = dataL0g0010201030[:,][:,5*0+0]
KineticEneL0g0010201030 = dataL0g0010201030[:,][:,5*0+1]
SelfEnergyL0g0010201030 = dataL0g0010201030[:,][:,5*0+2]
EigenValReL0g0010201030 = dataL0g0010201030[:,][:,5*0+3]
EigenValImL0g0010201030 = dataL0g0010201030[:,][:,5*0+4]

dataL0g0010201040 = np.genfromtxt('./L0/gK001/aK020/S1/N040/HamVals.txt')

MomentumAxL0g0010201040 = dataL0g0010201040[:,][:,5*0+0]
KineticEneL0g0010201040 = dataL0g0010201040[:,][:,5*0+1]
SelfEnergyL0g0010201040 = dataL0g0010201040[:,][:,5*0+2]
EigenValReL0g0010201040 = dataL0g0010201040[:,][:,5*0+3]
EigenValImL0g0010201040 = dataL0g0010201040[:,][:,5*0+4]

dataL0g0010201050 = np.genfromtxt('./L0/gK001/aK020/S1/N050/HamVals.txt')

MomentumAxL0g0010201050 = dataL0g0010201050[:,][:,5*0+0]
KineticEneL0g0010201050 = dataL0g0010201050[:,][:,5*0+1]
SelfEnergyL0g0010201050 = dataL0g0010201050[:,][:,5*0+2]
EigenValReL0g0010201050 = dataL0g0010201050[:,][:,5*0+3]
EigenValImL0g0010201050 = dataL0g0010201050[:,][:,5*0+4]

MaxEigenValImL0g0011010 = np.zeros((4))
MaxEigenValImL0g0011020 = np.zeros((4))
MaxEigenValImL0g0011030 = np.zeros((4))
MaxEigenValImL0g0011040 = np.zeros((4))
MaxEigenValImL0g0011050 = np.zeros((4))
MaxEigenValImL0g0011Inf = np.zeros((4))

MaxEigenValImL0g0011010[0] = np.max(EigenValImL0g0010011010)
MaxEigenValImL0g0011010[1] = np.max(EigenValImL0g0010021010)
MaxEigenValImL0g0011010[2] = np.max(EigenValImL0g0010051010)
MaxEigenValImL0g0011010[3] = np.max(EigenValImL0g0010101010)
#MaxEigenValImL0g0011010[4] = np.max(EigenValImL0g0010201010)

MaxEigenValImL0g0011020[0] = np.max(EigenValImL0g0010011020)
MaxEigenValImL0g0011020[1] = np.max(EigenValImL0g0010021020)
MaxEigenValImL0g0011020[2] = np.max(EigenValImL0g0010051020)
MaxEigenValImL0g0011020[3] = np.max(EigenValImL0g0010101020)
#MaxEigenValImL0g0011020[4] = np.max(EigenValImL0g0010201020)

MaxEigenValImL0g0011030[0] = np.max(EigenValImL0g0010011030)
MaxEigenValImL0g0011030[1] = np.max(EigenValImL0g0010021030)
MaxEigenValImL0g0011030[2] = np.max(EigenValImL0g0010051030)
MaxEigenValImL0g0011030[3] = np.max(EigenValImL0g0010101030)
#MaxEigenValImL0g0011030[4] = np.max(EigenValImL0g0010201030)

MaxEigenValImL0g0011040[0] = np.max(EigenValImL0g0010011040)
MaxEigenValImL0g0011040[1] = np.max(EigenValImL0g0010021040)
MaxEigenValImL0g0011040[2] = np.max(EigenValImL0g0010051040)
MaxEigenValImL0g0011040[3] = np.max(EigenValImL0g0010101040)
#MaxEigenValImL0g0011040[4] = np.max(EigenValImL0g0010201040)

MaxEigenValImL0g0011050[0] = np.max(EigenValImL0g0010011050)
MaxEigenValImL0g0011050[1] = np.max(EigenValImL0g0010021050)
MaxEigenValImL0g0011050[2] = np.max(EigenValImL0g0010051050)
MaxEigenValImL0g0011050[3] = np.max(EigenValImL0g0010101050)
#MaxEigenValImL0g0011050[4] = np.max(EigenValImL0g0010201050)

MaxEigenValImL0g0011Inf[0] = np.polyfit(fiveSizes, [MaxEigenValImL0g0011010[0],MaxEigenValImL0g0011020[0],MaxEigenValImL0g0011030[0],MaxEigenValImL0g0011040[0],MaxEigenValImL0g0011050[0]], 1)[[1]]
MaxEigenValImL0g0011Inf[1] = np.polyfit(fiveSizes, [MaxEigenValImL0g0011010[1],MaxEigenValImL0g0011020[1],MaxEigenValImL0g0011030[1],MaxEigenValImL0g0011040[1],MaxEigenValImL0g0011050[1]], 1)[[1]]
MaxEigenValImL0g0011Inf[2] = np.polyfit(fiveSizes, [MaxEigenValImL0g0011010[2],MaxEigenValImL0g0011020[2],MaxEigenValImL0g0011030[2],MaxEigenValImL0g0011040[2],MaxEigenValImL0g0011050[2]], 1)[[1]]
MaxEigenValImL0g0011Inf[3] = np.polyfit(fiveSizes, [MaxEigenValImL0g0011010[3],MaxEigenValImL0g0011020[3],MaxEigenValImL0g0011030[3],MaxEigenValImL0g0011040[3],MaxEigenValImL0g0011050[3]], 1)[[1]]
#MaxEigenValImL0g0011Inf[4] = np.polyfit(fiveSizes, [MaxEigenValImL0g0011010[4],MaxEigenValImL0g0011020[4],MaxEigenValImL0g0011030[4],MaxEigenValImL0g0011040[4],MaxEigenValImL0g0011050[4]], 1)[[1]]

########################################################################

dataL0g0010011010 = np.genfromtxt('./L0/gK002/aK001/S1/N010/HamVals.txt')

MomentumAxL0g0010011010 = dataL0g0010011010[:,][:,5*0+0]
KineticEneL0g0010011010 = dataL0g0010011010[:,][:,5*0+1]
SelfEnergyL0g0010011010 = dataL0g0010011010[:,][:,5*0+2]
EigenValReL0g0010011010 = dataL0g0010011010[:,][:,5*0+3]
EigenValImL0g0010011010 = dataL0g0010011010[:,][:,5*0+4]

dataL0g0010011020 = np.genfromtxt('./L0/gK002/aK001/S1/N020/HamVals.txt')

MomentumAxL0g0010011020 = dataL0g0010011020[:,][:,5*0+0]
KineticEneL0g0010011020 = dataL0g0010011020[:,][:,5*0+1]
SelfEnergyL0g0010011020 = dataL0g0010011020[:,][:,5*0+2]
EigenValReL0g0010011020 = dataL0g0010011020[:,][:,5*0+3]
EigenValImL0g0010011020 = dataL0g0010011020[:,][:,5*0+4]

dataL0g0010011030 = np.genfromtxt('./L0/gK002/aK001/S1/N030/HamVals.txt')

MomentumAxL0g0010011030 = dataL0g0010011030[:,][:,5*0+0]
KineticEneL0g0010011030 = dataL0g0010011030[:,][:,5*0+1]
SelfEnergyL0g0010011030 = dataL0g0010011030[:,][:,5*0+2]
EigenValReL0g0010011030 = dataL0g0010011030[:,][:,5*0+3]
EigenValImL0g0010011030 = dataL0g0010011030[:,][:,5*0+4]

dataL0g0010011040 = np.genfromtxt('./L0/gK002/aK001/S1/N040/HamVals.txt')

MomentumAxL0g0010011040 = dataL0g0010011040[:,][:,5*0+0]
KineticEneL0g0010011040 = dataL0g0010011040[:,][:,5*0+1]
SelfEnergyL0g0010011040 = dataL0g0010011040[:,][:,5*0+2]
EigenValReL0g0010011040 = dataL0g0010011040[:,][:,5*0+3]
EigenValImL0g0010011040 = dataL0g0010011040[:,][:,5*0+4]

dataL0g0010011050 = np.genfromtxt('./L0/gK002/aK001/S1/N050/HamVals.txt')

MomentumAxL0g0010011050 = dataL0g0010011050[:,][:,5*0+0]
KineticEneL0g0010011050 = dataL0g0010011050[:,][:,5*0+1]
SelfEnergyL0g0010011050 = dataL0g0010011050[:,][:,5*0+2]
EigenValReL0g0010011050 = dataL0g0010011050[:,][:,5*0+3]
EigenValImL0g0010011050 = dataL0g0010011050[:,][:,5*0+4]

dataL0g0010021010 = np.genfromtxt('./L0/gK002/aK002/S1/N010/HamVals.txt')

MomentumAxL0g0010021010 = dataL0g0010021010[:,][:,5*0+0]
KineticEneL0g0010021010 = dataL0g0010021010[:,][:,5*0+1]
SelfEnergyL0g0010021010 = dataL0g0010021010[:,][:,5*0+2]
EigenValReL0g0010021010 = dataL0g0010021010[:,][:,5*0+3]
EigenValImL0g0010021010 = dataL0g0010021010[:,][:,5*0+4]

dataL0g0010021020 = np.genfromtxt('./L0/gK002/aK002/S1/N020/HamVals.txt')

MomentumAxL0g0010021020 = dataL0g0010021020[:,][:,5*0+0]
KineticEneL0g0010021020 = dataL0g0010021020[:,][:,5*0+1]
SelfEnergyL0g0010021020 = dataL0g0010021020[:,][:,5*0+2]
EigenValReL0g0010021020 = dataL0g0010021020[:,][:,5*0+3]
EigenValImL0g0010021020 = dataL0g0010021020[:,][:,5*0+4]

dataL0g0010021030 = np.genfromtxt('./L0/gK002/aK002/S1/N030/HamVals.txt')

MomentumAxL0g0010021030 = dataL0g0010021030[:,][:,5*0+0]
KineticEneL0g0010021030 = dataL0g0010021030[:,][:,5*0+1]
SelfEnergyL0g0010021030 = dataL0g0010021030[:,][:,5*0+2]
EigenValReL0g0010021030 = dataL0g0010021030[:,][:,5*0+3]
EigenValImL0g0010021030 = dataL0g0010021030[:,][:,5*0+4]

dataL0g0010021040 = np.genfromtxt('./L0/gK002/aK002/S1/N040/HamVals.txt')

MomentumAxL0g0010021040 = dataL0g0010021040[:,][:,5*0+0]
KineticEneL0g0010021040 = dataL0g0010021040[:,][:,5*0+1]
SelfEnergyL0g0010021040 = dataL0g0010021040[:,][:,5*0+2]
EigenValReL0g0010021040 = dataL0g0010021040[:,][:,5*0+3]
EigenValImL0g0010021040 = dataL0g0010021040[:,][:,5*0+4]

dataL0g0010021050 = np.genfromtxt('./L0/gK002/aK002/S1/N050/HamVals.txt')

MomentumAxL0g0010021050 = dataL0g0010021050[:,][:,5*0+0]
KineticEneL0g0010021050 = dataL0g0010021050[:,][:,5*0+1]
SelfEnergyL0g0010021050 = dataL0g0010021050[:,][:,5*0+2]
EigenValReL0g0010021050 = dataL0g0010021050[:,][:,5*0+3]
EigenValImL0g0010021050 = dataL0g0010021050[:,][:,5*0+4]

dataL0g0010051010 = np.genfromtxt('./L0/gK002/aK005/S1/N010/HamVals.txt')

MomentumAxL0g0010051010 = dataL0g0010051010[:,][:,5*0+0]
KineticEneL0g0010051010 = dataL0g0010051010[:,][:,5*0+1]
SelfEnergyL0g0010051010 = dataL0g0010051010[:,][:,5*0+2]
EigenValReL0g0010051010 = dataL0g0010051010[:,][:,5*0+3]
EigenValImL0g0010051010 = dataL0g0010051010[:,][:,5*0+4]

dataL0g0010051020 = np.genfromtxt('./L0/gK002/aK005/S1/N020/HamVals.txt')

MomentumAxL0g0010051020 = dataL0g0010051020[:,][:,5*0+0]
KineticEneL0g0010051020 = dataL0g0010051020[:,][:,5*0+1]
SelfEnergyL0g0010051020 = dataL0g0010051020[:,][:,5*0+2]
EigenValReL0g0010051020 = dataL0g0010051020[:,][:,5*0+3]
EigenValImL0g0010051020 = dataL0g0010051020[:,][:,5*0+4]

dataL0g0010051030 = np.genfromtxt('./L0/gK002/aK005/S1/N030/HamVals.txt')

MomentumAxL0g0010051030 = dataL0g0010051030[:,][:,5*0+0]
KineticEneL0g0010051030 = dataL0g0010051030[:,][:,5*0+1]
SelfEnergyL0g0010051030 = dataL0g0010051030[:,][:,5*0+2]
EigenValReL0g0010051030 = dataL0g0010051030[:,][:,5*0+3]
EigenValImL0g0010051030 = dataL0g0010051030[:,][:,5*0+4]

dataL0g0010051040 = np.genfromtxt('./L0/gK002/aK005/S1/N040/HamVals.txt')

MomentumAxL0g0010051040 = dataL0g0010051040[:,][:,5*0+0]
KineticEneL0g0010051040 = dataL0g0010051040[:,][:,5*0+1]
SelfEnergyL0g0010051040 = dataL0g0010051040[:,][:,5*0+2]
EigenValReL0g0010051040 = dataL0g0010051040[:,][:,5*0+3]
EigenValImL0g0010051040 = dataL0g0010051040[:,][:,5*0+4]

dataL0g0010051050 = np.genfromtxt('./L0/gK002/aK005/S1/N050/HamVals.txt')

MomentumAxL0g0010051050 = dataL0g0010051050[:,][:,5*0+0]
KineticEneL0g0010051050 = dataL0g0010051050[:,][:,5*0+1]
SelfEnergyL0g0010051050 = dataL0g0010051050[:,][:,5*0+2]
EigenValReL0g0010051050 = dataL0g0010051050[:,][:,5*0+3]
EigenValImL0g0010051050 = dataL0g0010051050[:,][:,5*0+4]

dataL0g0010101010 = np.genfromtxt('./L0/gK002/aK010/S1/N010/HamVals.txt')

MomentumAxL0g0010101010 = dataL0g0010101010[:,][:,5*0+0]
KineticEneL0g0010101010 = dataL0g0010101010[:,][:,5*0+1]
SelfEnergyL0g0010101010 = dataL0g0010101010[:,][:,5*0+2]
EigenValReL0g0010101010 = dataL0g0010101010[:,][:,5*0+3]
EigenValImL0g0010101010 = dataL0g0010101010[:,][:,5*0+4]

dataL0g0010101020 = np.genfromtxt('./L0/gK002/aK010/S1/N020/HamVals.txt')

MomentumAxL0g0010101020 = dataL0g0010101020[:,][:,5*0+0]
KineticEneL0g0010101020 = dataL0g0010101020[:,][:,5*0+1]
SelfEnergyL0g0010101020 = dataL0g0010101020[:,][:,5*0+2]
EigenValReL0g0010101020 = dataL0g0010101020[:,][:,5*0+3]
EigenValImL0g0010101020 = dataL0g0010101020[:,][:,5*0+4]

dataL0g0010101030 = np.genfromtxt('./L0/gK002/aK010/S1/N030/HamVals.txt')

MomentumAxL0g0010101030 = dataL0g0010101030[:,][:,5*0+0]
KineticEneL0g0010101030 = dataL0g0010101030[:,][:,5*0+1]
SelfEnergyL0g0010101030 = dataL0g0010101030[:,][:,5*0+2]
EigenValReL0g0010101030 = dataL0g0010101030[:,][:,5*0+3]
EigenValImL0g0010101030 = dataL0g0010101030[:,][:,5*0+4]

dataL0g0010101040 = np.genfromtxt('./L0/gK002/aK010/S1/N040/HamVals.txt')

MomentumAxL0g0010101040 = dataL0g0010101040[:,][:,5*0+0]
KineticEneL0g0010101040 = dataL0g0010101040[:,][:,5*0+1]
SelfEnergyL0g0010101040 = dataL0g0010101040[:,][:,5*0+2]
EigenValReL0g0010101040 = dataL0g0010101040[:,][:,5*0+3]
EigenValImL0g0010101040 = dataL0g0010101040[:,][:,5*0+4]

dataL0g0010101050 = np.genfromtxt('./L0/gK002/aK010/S1/N050/HamVals.txt')

MomentumAxL0g0010101050 = dataL0g0010101050[:,][:,5*0+0]
KineticEneL0g0010101050 = dataL0g0010101050[:,][:,5*0+1]
SelfEnergyL0g0010101050 = dataL0g0010101050[:,][:,5*0+2]
EigenValReL0g0010101050 = dataL0g0010101050[:,][:,5*0+3]
EigenValImL0g0010101050 = dataL0g0010101050[:,][:,5*0+4]

dataL0g0010201010 = np.genfromtxt('./L0/gK002/aK020/S1/N010/HamVals.txt')

MomentumAxL0g0010201010 = dataL0g0010201010[:,][:,5*0+0]
KineticEneL0g0010201010 = dataL0g0010201010[:,][:,5*0+1]
SelfEnergyL0g0010201010 = dataL0g0010201010[:,][:,5*0+2]
EigenValReL0g0010201010 = dataL0g0010201010[:,][:,5*0+3]
EigenValImL0g0010201010 = dataL0g0010201010[:,][:,5*0+4]

dataL0g0010201020 = np.genfromtxt('./L0/gK002/aK020/S1/N020/HamVals.txt')

MomentumAxL0g0010201020 = dataL0g0010201020[:,][:,5*0+0]
KineticEneL0g0010201020 = dataL0g0010201020[:,][:,5*0+1]
SelfEnergyL0g0010201020 = dataL0g0010201020[:,][:,5*0+2]
EigenValReL0g0010201020 = dataL0g0010201020[:,][:,5*0+3]
EigenValImL0g0010201020 = dataL0g0010201020[:,][:,5*0+4]

dataL0g0010201030 = np.genfromtxt('./L0/gK002/aK020/S1/N030/HamVals.txt')

MomentumAxL0g0010201030 = dataL0g0010201030[:,][:,5*0+0]
KineticEneL0g0010201030 = dataL0g0010201030[:,][:,5*0+1]
SelfEnergyL0g0010201030 = dataL0g0010201030[:,][:,5*0+2]
EigenValReL0g0010201030 = dataL0g0010201030[:,][:,5*0+3]
EigenValImL0g0010201030 = dataL0g0010201030[:,][:,5*0+4]

dataL0g0010201040 = np.genfromtxt('./L0/gK002/aK020/S1/N040/HamVals.txt')

MomentumAxL0g0010201040 = dataL0g0010201040[:,][:,5*0+0]
KineticEneL0g0010201040 = dataL0g0010201040[:,][:,5*0+1]
SelfEnergyL0g0010201040 = dataL0g0010201040[:,][:,5*0+2]
EigenValReL0g0010201040 = dataL0g0010201040[:,][:,5*0+3]
EigenValImL0g0010201040 = dataL0g0010201040[:,][:,5*0+4]

dataL0g0010201050 = np.genfromtxt('./L0/gK002/aK020/S1/N050/HamVals.txt')

MomentumAxL0g0010201050 = dataL0g0010201050[:,][:,5*0+0]
KineticEneL0g0010201050 = dataL0g0010201050[:,][:,5*0+1]
SelfEnergyL0g0010201050 = dataL0g0010201050[:,][:,5*0+2]
EigenValReL0g0010201050 = dataL0g0010201050[:,][:,5*0+3]
EigenValImL0g0010201050 = dataL0g0010201050[:,][:,5*0+4]

MaxEigenValImL0g0021010 = np.zeros((4))
MaxEigenValImL0g0021020 = np.zeros((4))
MaxEigenValImL0g0021030 = np.zeros((4))
MaxEigenValImL0g0021040 = np.zeros((4))
MaxEigenValImL0g0021050 = np.zeros((4))
MaxEigenValImL0g0021Inf = np.zeros((4))

MaxEigenValImL0g0021010[0] = np.max(EigenValImL0g0010011010)
MaxEigenValImL0g0021010[1] = np.max(EigenValImL0g0010021010)
MaxEigenValImL0g0021010[2] = np.max(EigenValImL0g0010051010)
MaxEigenValImL0g0021010[3] = np.max(EigenValImL0g0010101010)
#MaxEigenValImL0g0021010[4] = np.max(EigenValImL0g0010201010)

MaxEigenValImL0g0021020[0] = np.max(EigenValImL0g0010011020)
MaxEigenValImL0g0021020[1] = np.max(EigenValImL0g0010021020)
MaxEigenValImL0g0021020[2] = np.max(EigenValImL0g0010051020)
MaxEigenValImL0g0021020[3] = np.max(EigenValImL0g0010101020)
#MaxEigenValImL0g0021020[4] = np.max(EigenValImL0g0010201020)

MaxEigenValImL0g0021030[0] = np.max(EigenValImL0g0010011030)
MaxEigenValImL0g0021030[1] = np.max(EigenValImL0g0010021030)
MaxEigenValImL0g0021030[2] = np.max(EigenValImL0g0010051030)
MaxEigenValImL0g0021030[3] = np.max(EigenValImL0g0010101030)
#MaxEigenValImL0g0021030[4] = np.max(EigenValImL0g0010201030)

MaxEigenValImL0g0021040[0] = np.max(EigenValImL0g0010011040)
MaxEigenValImL0g0021040[1] = np.max(EigenValImL0g0010021040)
MaxEigenValImL0g0021040[2] = np.max(EigenValImL0g0010051040)
MaxEigenValImL0g0021040[3] = np.max(EigenValImL0g0010101040)
#MaxEigenValImL0g0021040[4] = np.max(EigenValImL0g0010201040)

MaxEigenValImL0g0021050[0] = np.max(EigenValImL0g0010011050)
MaxEigenValImL0g0021050[1] = np.max(EigenValImL0g0010021050)
MaxEigenValImL0g0021050[2] = np.max(EigenValImL0g0010051050)
MaxEigenValImL0g0021050[3] = np.max(EigenValImL0g0010101050)
#MaxEigenValImL0g0021050[4] = np.max(EigenValImL0g0010201050)

MaxEigenValImL0g0021Inf[0] = np.polyfit(fiveSizes, [MaxEigenValImL0g0021010[0],MaxEigenValImL0g0021020[0],MaxEigenValImL0g0021030[0],MaxEigenValImL0g0021040[0],MaxEigenValImL0g0021050[0]], 1)[[1]]
MaxEigenValImL0g0021Inf[1] = np.polyfit(fiveSizes, [MaxEigenValImL0g0021010[1],MaxEigenValImL0g0021020[1],MaxEigenValImL0g0021030[1],MaxEigenValImL0g0021040[1],MaxEigenValImL0g0021050[1]], 1)[[1]]
MaxEigenValImL0g0021Inf[2] = np.polyfit(fiveSizes, [MaxEigenValImL0g0021010[2],MaxEigenValImL0g0021020[2],MaxEigenValImL0g0021030[2],MaxEigenValImL0g0021040[2],MaxEigenValImL0g0021050[2]], 1)[[1]]
MaxEigenValImL0g0021Inf[3] = np.polyfit(fiveSizes, [MaxEigenValImL0g0021010[3],MaxEigenValImL0g0021020[3],MaxEigenValImL0g0021030[3],MaxEigenValImL0g0021040[3],MaxEigenValImL0g0021050[3]], 1)[[1]]
#MaxEigenValImL0g0021Inf[4] = np.polyfit(fiveSizes, [MaxEigenValImL0g0021010[4],MaxEigenValImL0g0021020[4],MaxEigenValImL0g0021030[4],MaxEigenValImL0g0021040[4],MaxEigenValImL0g0021050[4]], 1)[[1]]

########################################################################

dataL0g0010011010 = np.genfromtxt('./L0/gK005/aK001/S1/N010/HamVals.txt')

MomentumAxL0g0010011010 = dataL0g0010011010[:,][:,5*0+0]
KineticEneL0g0010011010 = dataL0g0010011010[:,][:,5*0+1]
SelfEnergyL0g0010011010 = dataL0g0010011010[:,][:,5*0+2]
EigenValReL0g0010011010 = dataL0g0010011010[:,][:,5*0+3]
EigenValImL0g0010011010 = dataL0g0010011010[:,][:,5*0+4]

dataL0g0010011020 = np.genfromtxt('./L0/gK005/aK001/S1/N020/HamVals.txt')

MomentumAxL0g0010011020 = dataL0g0010011020[:,][:,5*0+0]
KineticEneL0g0010011020 = dataL0g0010011020[:,][:,5*0+1]
SelfEnergyL0g0010011020 = dataL0g0010011020[:,][:,5*0+2]
EigenValReL0g0010011020 = dataL0g0010011020[:,][:,5*0+3]
EigenValImL0g0010011020 = dataL0g0010011020[:,][:,5*0+4]

dataL0g0010011030 = np.genfromtxt('./L0/gK005/aK001/S1/N030/HamVals.txt')

MomentumAxL0g0010011030 = dataL0g0010011030[:,][:,5*0+0]
KineticEneL0g0010011030 = dataL0g0010011030[:,][:,5*0+1]
SelfEnergyL0g0010011030 = dataL0g0010011030[:,][:,5*0+2]
EigenValReL0g0010011030 = dataL0g0010011030[:,][:,5*0+3]
EigenValImL0g0010011030 = dataL0g0010011030[:,][:,5*0+4]

dataL0g0010011040 = np.genfromtxt('./L0/gK005/aK001/S1/N040/HamVals.txt')

MomentumAxL0g0010011040 = dataL0g0010011040[:,][:,5*0+0]
KineticEneL0g0010011040 = dataL0g0010011040[:,][:,5*0+1]
SelfEnergyL0g0010011040 = dataL0g0010011040[:,][:,5*0+2]
EigenValReL0g0010011040 = dataL0g0010011040[:,][:,5*0+3]
EigenValImL0g0010011040 = dataL0g0010011040[:,][:,5*0+4]

dataL0g0010011050 = np.genfromtxt('./L0/gK005/aK001/S1/N050/HamVals.txt')

MomentumAxL0g0010011050 = dataL0g0010011050[:,][:,5*0+0]
KineticEneL0g0010011050 = dataL0g0010011050[:,][:,5*0+1]
SelfEnergyL0g0010011050 = dataL0g0010011050[:,][:,5*0+2]
EigenValReL0g0010011050 = dataL0g0010011050[:,][:,5*0+3]
EigenValImL0g0010011050 = dataL0g0010011050[:,][:,5*0+4]

dataL0g0010021010 = np.genfromtxt('./L0/gK005/aK002/S1/N010/HamVals.txt')

MomentumAxL0g0010021010 = dataL0g0010021010[:,][:,5*0+0]
KineticEneL0g0010021010 = dataL0g0010021010[:,][:,5*0+1]
SelfEnergyL0g0010021010 = dataL0g0010021010[:,][:,5*0+2]
EigenValReL0g0010021010 = dataL0g0010021010[:,][:,5*0+3]
EigenValImL0g0010021010 = dataL0g0010021010[:,][:,5*0+4]

dataL0g0010021020 = np.genfromtxt('./L0/gK005/aK002/S1/N020/HamVals.txt')

MomentumAxL0g0010021020 = dataL0g0010021020[:,][:,5*0+0]
KineticEneL0g0010021020 = dataL0g0010021020[:,][:,5*0+1]
SelfEnergyL0g0010021020 = dataL0g0010021020[:,][:,5*0+2]
EigenValReL0g0010021020 = dataL0g0010021020[:,][:,5*0+3]
EigenValImL0g0010021020 = dataL0g0010021020[:,][:,5*0+4]

dataL0g0010021030 = np.genfromtxt('./L0/gK005/aK002/S1/N030/HamVals.txt')

MomentumAxL0g0010021030 = dataL0g0010021030[:,][:,5*0+0]
KineticEneL0g0010021030 = dataL0g0010021030[:,][:,5*0+1]
SelfEnergyL0g0010021030 = dataL0g0010021030[:,][:,5*0+2]
EigenValReL0g0010021030 = dataL0g0010021030[:,][:,5*0+3]
EigenValImL0g0010021030 = dataL0g0010021030[:,][:,5*0+4]

dataL0g0010021040 = np.genfromtxt('./L0/gK005/aK002/S1/N040/HamVals.txt')

MomentumAxL0g0010021040 = dataL0g0010021040[:,][:,5*0+0]
KineticEneL0g0010021040 = dataL0g0010021040[:,][:,5*0+1]
SelfEnergyL0g0010021040 = dataL0g0010021040[:,][:,5*0+2]
EigenValReL0g0010021040 = dataL0g0010021040[:,][:,5*0+3]
EigenValImL0g0010021040 = dataL0g0010021040[:,][:,5*0+4]

dataL0g0010021050 = np.genfromtxt('./L0/gK005/aK002/S1/N050/HamVals.txt')

MomentumAxL0g0010021050 = dataL0g0010021050[:,][:,5*0+0]
KineticEneL0g0010021050 = dataL0g0010021050[:,][:,5*0+1]
SelfEnergyL0g0010021050 = dataL0g0010021050[:,][:,5*0+2]
EigenValReL0g0010021050 = dataL0g0010021050[:,][:,5*0+3]
EigenValImL0g0010021050 = dataL0g0010021050[:,][:,5*0+4]

dataL0g0010051010 = np.genfromtxt('./L0/gK005/aK005/S1/N010/HamVals.txt')

MomentumAxL0g0010051010 = dataL0g0010051010[:,][:,5*0+0]
KineticEneL0g0010051010 = dataL0g0010051010[:,][:,5*0+1]
SelfEnergyL0g0010051010 = dataL0g0010051010[:,][:,5*0+2]
EigenValReL0g0010051010 = dataL0g0010051010[:,][:,5*0+3]
EigenValImL0g0010051010 = dataL0g0010051010[:,][:,5*0+4]

dataL0g0010051020 = np.genfromtxt('./L0/gK005/aK005/S1/N020/HamVals.txt')

MomentumAxL0g0010051020 = dataL0g0010051020[:,][:,5*0+0]
KineticEneL0g0010051020 = dataL0g0010051020[:,][:,5*0+1]
SelfEnergyL0g0010051020 = dataL0g0010051020[:,][:,5*0+2]
EigenValReL0g0010051020 = dataL0g0010051020[:,][:,5*0+3]
EigenValImL0g0010051020 = dataL0g0010051020[:,][:,5*0+4]

dataL0g0010051030 = np.genfromtxt('./L0/gK005/aK005/S1/N030/HamVals.txt')

MomentumAxL0g0010051030 = dataL0g0010051030[:,][:,5*0+0]
KineticEneL0g0010051030 = dataL0g0010051030[:,][:,5*0+1]
SelfEnergyL0g0010051030 = dataL0g0010051030[:,][:,5*0+2]
EigenValReL0g0010051030 = dataL0g0010051030[:,][:,5*0+3]
EigenValImL0g0010051030 = dataL0g0010051030[:,][:,5*0+4]

dataL0g0010051040 = np.genfromtxt('./L0/gK005/aK005/S1/N040/HamVals.txt')

MomentumAxL0g0010051040 = dataL0g0010051040[:,][:,5*0+0]
KineticEneL0g0010051040 = dataL0g0010051040[:,][:,5*0+1]
SelfEnergyL0g0010051040 = dataL0g0010051040[:,][:,5*0+2]
EigenValReL0g0010051040 = dataL0g0010051040[:,][:,5*0+3]
EigenValImL0g0010051040 = dataL0g0010051040[:,][:,5*0+4]

dataL0g0010051050 = np.genfromtxt('./L0/gK005/aK005/S1/N050/HamVals.txt')

MomentumAxL0g0010051050 = dataL0g0010051050[:,][:,5*0+0]
KineticEneL0g0010051050 = dataL0g0010051050[:,][:,5*0+1]
SelfEnergyL0g0010051050 = dataL0g0010051050[:,][:,5*0+2]
EigenValReL0g0010051050 = dataL0g0010051050[:,][:,5*0+3]
EigenValImL0g0010051050 = dataL0g0010051050[:,][:,5*0+4]

dataL0g0010101010 = np.genfromtxt('./L0/gK005/aK010/S1/N010/HamVals.txt')

MomentumAxL0g0010101010 = dataL0g0010101010[:,][:,5*0+0]
KineticEneL0g0010101010 = dataL0g0010101010[:,][:,5*0+1]
SelfEnergyL0g0010101010 = dataL0g0010101010[:,][:,5*0+2]
EigenValReL0g0010101010 = dataL0g0010101010[:,][:,5*0+3]
EigenValImL0g0010101010 = dataL0g0010101010[:,][:,5*0+4]

dataL0g0010101020 = np.genfromtxt('./L0/gK005/aK010/S1/N020/HamVals.txt')

MomentumAxL0g0010101020 = dataL0g0010101020[:,][:,5*0+0]
KineticEneL0g0010101020 = dataL0g0010101020[:,][:,5*0+1]
SelfEnergyL0g0010101020 = dataL0g0010101020[:,][:,5*0+2]
EigenValReL0g0010101020 = dataL0g0010101020[:,][:,5*0+3]
EigenValImL0g0010101020 = dataL0g0010101020[:,][:,5*0+4]

dataL0g0010101030 = np.genfromtxt('./L0/gK005/aK010/S1/N030/HamVals.txt')

MomentumAxL0g0010101030 = dataL0g0010101030[:,][:,5*0+0]
KineticEneL0g0010101030 = dataL0g0010101030[:,][:,5*0+1]
SelfEnergyL0g0010101030 = dataL0g0010101030[:,][:,5*0+2]
EigenValReL0g0010101030 = dataL0g0010101030[:,][:,5*0+3]
EigenValImL0g0010101030 = dataL0g0010101030[:,][:,5*0+4]

dataL0g0010101040 = np.genfromtxt('./L0/gK005/aK010/S1/N040/HamVals.txt')

MomentumAxL0g0010101040 = dataL0g0010101040[:,][:,5*0+0]
KineticEneL0g0010101040 = dataL0g0010101040[:,][:,5*0+1]
SelfEnergyL0g0010101040 = dataL0g0010101040[:,][:,5*0+2]
EigenValReL0g0010101040 = dataL0g0010101040[:,][:,5*0+3]
EigenValImL0g0010101040 = dataL0g0010101040[:,][:,5*0+4]

dataL0g0010101050 = np.genfromtxt('./L0/gK005/aK010/S1/N050/HamVals.txt')

MomentumAxL0g0010101050 = dataL0g0010101050[:,][:,5*0+0]
KineticEneL0g0010101050 = dataL0g0010101050[:,][:,5*0+1]
SelfEnergyL0g0010101050 = dataL0g0010101050[:,][:,5*0+2]
EigenValReL0g0010101050 = dataL0g0010101050[:,][:,5*0+3]
EigenValImL0g0010101050 = dataL0g0010101050[:,][:,5*0+4]

dataL0g0010201010 = np.genfromtxt('./L0/gK005/aK020/S1/N010/HamVals.txt')

MomentumAxL0g0010201010 = dataL0g0010201010[:,][:,5*0+0]
KineticEneL0g0010201010 = dataL0g0010201010[:,][:,5*0+1]
SelfEnergyL0g0010201010 = dataL0g0010201010[:,][:,5*0+2]
EigenValReL0g0010201010 = dataL0g0010201010[:,][:,5*0+3]
EigenValImL0g0010201010 = dataL0g0010201010[:,][:,5*0+4]

dataL0g0010201020 = np.genfromtxt('./L0/gK005/aK020/S1/N020/HamVals.txt')

MomentumAxL0g0010201020 = dataL0g0010201020[:,][:,5*0+0]
KineticEneL0g0010201020 = dataL0g0010201020[:,][:,5*0+1]
SelfEnergyL0g0010201020 = dataL0g0010201020[:,][:,5*0+2]
EigenValReL0g0010201020 = dataL0g0010201020[:,][:,5*0+3]
EigenValImL0g0010201020 = dataL0g0010201020[:,][:,5*0+4]

dataL0g0010201030 = np.genfromtxt('./L0/gK005/aK020/S1/N030/HamVals.txt')

MomentumAxL0g0010201030 = dataL0g0010201030[:,][:,5*0+0]
KineticEneL0g0010201030 = dataL0g0010201030[:,][:,5*0+1]
SelfEnergyL0g0010201030 = dataL0g0010201030[:,][:,5*0+2]
EigenValReL0g0010201030 = dataL0g0010201030[:,][:,5*0+3]
EigenValImL0g0010201030 = dataL0g0010201030[:,][:,5*0+4]

dataL0g0010201040 = np.genfromtxt('./L0/gK005/aK020/S1/N040/HamVals.txt')

MomentumAxL0g0010201040 = dataL0g0010201040[:,][:,5*0+0]
KineticEneL0g0010201040 = dataL0g0010201040[:,][:,5*0+1]
SelfEnergyL0g0010201040 = dataL0g0010201040[:,][:,5*0+2]
EigenValReL0g0010201040 = dataL0g0010201040[:,][:,5*0+3]
EigenValImL0g0010201040 = dataL0g0010201040[:,][:,5*0+4]

dataL0g0010201050 = np.genfromtxt('./L0/gK005/aK020/S1/N050/HamVals.txt')

MomentumAxL0g0010201050 = dataL0g0010201050[:,][:,5*0+0]
KineticEneL0g0010201050 = dataL0g0010201050[:,][:,5*0+1]
SelfEnergyL0g0010201050 = dataL0g0010201050[:,][:,5*0+2]
EigenValReL0g0010201050 = dataL0g0010201050[:,][:,5*0+3]
EigenValImL0g0010201050 = dataL0g0010201050[:,][:,5*0+4]

MaxEigenValImL0g0051010 = np.zeros((4))
MaxEigenValImL0g0051020 = np.zeros((4))
MaxEigenValImL0g0051030 = np.zeros((4))
MaxEigenValImL0g0051040 = np.zeros((4))
MaxEigenValImL0g0051050 = np.zeros((4))
MaxEigenValImL0g0051Inf = np.zeros((4))

MaxEigenValImL0g0051010[0] = np.max(EigenValImL0g0010011010)
MaxEigenValImL0g0051010[1] = np.max(EigenValImL0g0010021010)
MaxEigenValImL0g0051010[2] = np.max(EigenValImL0g0010051010)
MaxEigenValImL0g0051010[3] = np.max(EigenValImL0g0010101010)
#MaxEigenValImL0g0051010[4] = np.max(EigenValImL0g0010201010)

MaxEigenValImL0g0051020[0] = np.max(EigenValImL0g0010011020)
MaxEigenValImL0g0051020[1] = np.max(EigenValImL0g0010021020)
MaxEigenValImL0g0051020[2] = np.max(EigenValImL0g0010051020)
MaxEigenValImL0g0051020[3] = np.max(EigenValImL0g0010101020)
#MaxEigenValImL0g0051020[4] = np.max(EigenValImL0g0010201020)

MaxEigenValImL0g0051030[0] = np.max(EigenValImL0g0010011030)
MaxEigenValImL0g0051030[1] = np.max(EigenValImL0g0010021030)
MaxEigenValImL0g0051030[2] = np.max(EigenValImL0g0010051030)
MaxEigenValImL0g0051030[3] = np.max(EigenValImL0g0010101030)
#MaxEigenValImL0g0051030[4] = np.max(EigenValImL0g0010201030)

MaxEigenValImL0g0051040[0] = np.max(EigenValImL0g0010011040)
MaxEigenValImL0g0051040[1] = np.max(EigenValImL0g0010021040)
MaxEigenValImL0g0051040[2] = np.max(EigenValImL0g0010051040)
MaxEigenValImL0g0051040[3] = np.max(EigenValImL0g0010101040)
#MaxEigenValImL0g0051040[4] = np.max(EigenValImL0g0010201040)

MaxEigenValImL0g0051050[0] = np.max(EigenValImL0g0010011050)
MaxEigenValImL0g0051050[1] = np.max(EigenValImL0g0010021050)
MaxEigenValImL0g0051050[2] = np.max(EigenValImL0g0010051050)
MaxEigenValImL0g0051050[3] = np.max(EigenValImL0g0010101050)
#MaxEigenValImL0g0051050[4] = np.max(EigenValImL0g0010201050)

MaxEigenValImL0g0051Inf[0] = np.polyfit(fiveSizes, [MaxEigenValImL0g0051010[0],MaxEigenValImL0g0051020[0],MaxEigenValImL0g0051030[0],MaxEigenValImL0g0051040[0],MaxEigenValImL0g0051050[0]], 1)[[1]]
MaxEigenValImL0g0051Inf[1] = np.polyfit(fiveSizes, [MaxEigenValImL0g0051010[1],MaxEigenValImL0g0051020[1],MaxEigenValImL0g0051030[1],MaxEigenValImL0g0051040[1],MaxEigenValImL0g0051050[1]], 1)[[1]]
MaxEigenValImL0g0051Inf[2] = np.polyfit(fiveSizes, [MaxEigenValImL0g0051010[2],MaxEigenValImL0g0051020[2],MaxEigenValImL0g0051030[2],MaxEigenValImL0g0051040[2],MaxEigenValImL0g0051050[2]], 1)[[1]]
MaxEigenValImL0g0051Inf[3] = np.polyfit(fiveSizes, [MaxEigenValImL0g0051010[3],MaxEigenValImL0g0051020[3],MaxEigenValImL0g0051030[3],MaxEigenValImL0g0051040[3],MaxEigenValImL0g0051050[3]], 1)[[1]]
#MaxEigenValImL0g0051Inf[4] = np.polyfit(fiveSizes, [MaxEigenValImL0g0051010[4],MaxEigenValImL0g0051020[4],MaxEigenValImL0g0051030[4],MaxEigenValImL0g0051040[4],MaxEigenValImL0g0051050[4]], 1)[[1]]

########################################################################

dataL0g0010011010 = np.genfromtxt('./L0/gK010/aK001/S1/N010/HamVals.txt')

MomentumAxL0g0010011010 = dataL0g0010011010[:,][:,5*0+0]
KineticEneL0g0010011010 = dataL0g0010011010[:,][:,5*0+1]
SelfEnergyL0g0010011010 = dataL0g0010011010[:,][:,5*0+2]
EigenValReL0g0010011010 = dataL0g0010011010[:,][:,5*0+3]
EigenValImL0g0010011010 = dataL0g0010011010[:,][:,5*0+4]

dataL0g0010011020 = np.genfromtxt('./L0/gK010/aK001/S1/N020/HamVals.txt')

MomentumAxL0g0010011020 = dataL0g0010011020[:,][:,5*0+0]
KineticEneL0g0010011020 = dataL0g0010011020[:,][:,5*0+1]
SelfEnergyL0g0010011020 = dataL0g0010011020[:,][:,5*0+2]
EigenValReL0g0010011020 = dataL0g0010011020[:,][:,5*0+3]
EigenValImL0g0010011020 = dataL0g0010011020[:,][:,5*0+4]

dataL0g0010011030 = np.genfromtxt('./L0/gK010/aK001/S1/N030/HamVals.txt')

MomentumAxL0g0010011030 = dataL0g0010011030[:,][:,5*0+0]
KineticEneL0g0010011030 = dataL0g0010011030[:,][:,5*0+1]
SelfEnergyL0g0010011030 = dataL0g0010011030[:,][:,5*0+2]
EigenValReL0g0010011030 = dataL0g0010011030[:,][:,5*0+3]
EigenValImL0g0010011030 = dataL0g0010011030[:,][:,5*0+4]

dataL0g0010011040 = np.genfromtxt('./L0/gK010/aK001/S1/N040/HamVals.txt')

MomentumAxL0g0010011040 = dataL0g0010011040[:,][:,5*0+0]
KineticEneL0g0010011040 = dataL0g0010011040[:,][:,5*0+1]
SelfEnergyL0g0010011040 = dataL0g0010011040[:,][:,5*0+2]
EigenValReL0g0010011040 = dataL0g0010011040[:,][:,5*0+3]
EigenValImL0g0010011040 = dataL0g0010011040[:,][:,5*0+4]

dataL0g0010011050 = np.genfromtxt('./L0/gK010/aK001/S1/N050/HamVals.txt')

MomentumAxL0g0010011050 = dataL0g0010011050[:,][:,5*0+0]
KineticEneL0g0010011050 = dataL0g0010011050[:,][:,5*0+1]
SelfEnergyL0g0010011050 = dataL0g0010011050[:,][:,5*0+2]
EigenValReL0g0010011050 = dataL0g0010011050[:,][:,5*0+3]
EigenValImL0g0010011050 = dataL0g0010011050[:,][:,5*0+4]

dataL0g0010021010 = np.genfromtxt('./L0/gK010/aK002/S1/N010/HamVals.txt')

MomentumAxL0g0010021010 = dataL0g0010021010[:,][:,5*0+0]
KineticEneL0g0010021010 = dataL0g0010021010[:,][:,5*0+1]
SelfEnergyL0g0010021010 = dataL0g0010021010[:,][:,5*0+2]
EigenValReL0g0010021010 = dataL0g0010021010[:,][:,5*0+3]
EigenValImL0g0010021010 = dataL0g0010021010[:,][:,5*0+4]

dataL0g0010021020 = np.genfromtxt('./L0/gK010/aK002/S1/N020/HamVals.txt')

MomentumAxL0g0010021020 = dataL0g0010021020[:,][:,5*0+0]
KineticEneL0g0010021020 = dataL0g0010021020[:,][:,5*0+1]
SelfEnergyL0g0010021020 = dataL0g0010021020[:,][:,5*0+2]
EigenValReL0g0010021020 = dataL0g0010021020[:,][:,5*0+3]
EigenValImL0g0010021020 = dataL0g0010021020[:,][:,5*0+4]

dataL0g0010021030 = np.genfromtxt('./L0/gK010/aK002/S1/N030/HamVals.txt')

MomentumAxL0g0010021030 = dataL0g0010021030[:,][:,5*0+0]
KineticEneL0g0010021030 = dataL0g0010021030[:,][:,5*0+1]
SelfEnergyL0g0010021030 = dataL0g0010021030[:,][:,5*0+2]
EigenValReL0g0010021030 = dataL0g0010021030[:,][:,5*0+3]
EigenValImL0g0010021030 = dataL0g0010021030[:,][:,5*0+4]

dataL0g0010021040 = np.genfromtxt('./L0/gK010/aK002/S1/N040/HamVals.txt')

MomentumAxL0g0010021040 = dataL0g0010021040[:,][:,5*0+0]
KineticEneL0g0010021040 = dataL0g0010021040[:,][:,5*0+1]
SelfEnergyL0g0010021040 = dataL0g0010021040[:,][:,5*0+2]
EigenValReL0g0010021040 = dataL0g0010021040[:,][:,5*0+3]
EigenValImL0g0010021040 = dataL0g0010021040[:,][:,5*0+4]

dataL0g0010021050 = np.genfromtxt('./L0/gK010/aK002/S1/N050/HamVals.txt')

MomentumAxL0g0010021050 = dataL0g0010021050[:,][:,5*0+0]
KineticEneL0g0010021050 = dataL0g0010021050[:,][:,5*0+1]
SelfEnergyL0g0010021050 = dataL0g0010021050[:,][:,5*0+2]
EigenValReL0g0010021050 = dataL0g0010021050[:,][:,5*0+3]
EigenValImL0g0010021050 = dataL0g0010021050[:,][:,5*0+4]

dataL0g0010051010 = np.genfromtxt('./L0/gK010/aK005/S1/N010/HamVals.txt')

MomentumAxL0g0010051010 = dataL0g0010051010[:,][:,5*0+0]
KineticEneL0g0010051010 = dataL0g0010051010[:,][:,5*0+1]
SelfEnergyL0g0010051010 = dataL0g0010051010[:,][:,5*0+2]
EigenValReL0g0010051010 = dataL0g0010051010[:,][:,5*0+3]
EigenValImL0g0010051010 = dataL0g0010051010[:,][:,5*0+4]

dataL0g0010051020 = np.genfromtxt('./L0/gK010/aK005/S1/N020/HamVals.txt')

MomentumAxL0g0010051020 = dataL0g0010051020[:,][:,5*0+0]
KineticEneL0g0010051020 = dataL0g0010051020[:,][:,5*0+1]
SelfEnergyL0g0010051020 = dataL0g0010051020[:,][:,5*0+2]
EigenValReL0g0010051020 = dataL0g0010051020[:,][:,5*0+3]
EigenValImL0g0010051020 = dataL0g0010051020[:,][:,5*0+4]

dataL0g0010051030 = np.genfromtxt('./L0/gK010/aK005/S1/N030/HamVals.txt')

MomentumAxL0g0010051030 = dataL0g0010051030[:,][:,5*0+0]
KineticEneL0g0010051030 = dataL0g0010051030[:,][:,5*0+1]
SelfEnergyL0g0010051030 = dataL0g0010051030[:,][:,5*0+2]
EigenValReL0g0010051030 = dataL0g0010051030[:,][:,5*0+3]
EigenValImL0g0010051030 = dataL0g0010051030[:,][:,5*0+4]

dataL0g0010051040 = np.genfromtxt('./L0/gK010/aK005/S1/N040/HamVals.txt')

MomentumAxL0g0010051040 = dataL0g0010051040[:,][:,5*0+0]
KineticEneL0g0010051040 = dataL0g0010051040[:,][:,5*0+1]
SelfEnergyL0g0010051040 = dataL0g0010051040[:,][:,5*0+2]
EigenValReL0g0010051040 = dataL0g0010051040[:,][:,5*0+3]
EigenValImL0g0010051040 = dataL0g0010051040[:,][:,5*0+4]

dataL0g0010051050 = np.genfromtxt('./L0/gK010/aK005/S1/N050/HamVals.txt')

MomentumAxL0g0010051050 = dataL0g0010051050[:,][:,5*0+0]
KineticEneL0g0010051050 = dataL0g0010051050[:,][:,5*0+1]
SelfEnergyL0g0010051050 = dataL0g0010051050[:,][:,5*0+2]
EigenValReL0g0010051050 = dataL0g0010051050[:,][:,5*0+3]
EigenValImL0g0010051050 = dataL0g0010051050[:,][:,5*0+4]

dataL0g0010101010 = np.genfromtxt('./L0/gK010/aK010/S1/N010/HamVals.txt')

MomentumAxL0g0010101010 = dataL0g0010101010[:,][:,5*0+0]
KineticEneL0g0010101010 = dataL0g0010101010[:,][:,5*0+1]
SelfEnergyL0g0010101010 = dataL0g0010101010[:,][:,5*0+2]
EigenValReL0g0010101010 = dataL0g0010101010[:,][:,5*0+3]
EigenValImL0g0010101010 = dataL0g0010101010[:,][:,5*0+4]

dataL0g0010101020 = np.genfromtxt('./L0/gK010/aK010/S1/N020/HamVals.txt')

MomentumAxL0g0010101020 = dataL0g0010101020[:,][:,5*0+0]
KineticEneL0g0010101020 = dataL0g0010101020[:,][:,5*0+1]
SelfEnergyL0g0010101020 = dataL0g0010101020[:,][:,5*0+2]
EigenValReL0g0010101020 = dataL0g0010101020[:,][:,5*0+3]
EigenValImL0g0010101020 = dataL0g0010101020[:,][:,5*0+4]

dataL0g0010101030 = np.genfromtxt('./L0/gK010/aK010/S1/N030/HamVals.txt')

MomentumAxL0g0010101030 = dataL0g0010101030[:,][:,5*0+0]
KineticEneL0g0010101030 = dataL0g0010101030[:,][:,5*0+1]
SelfEnergyL0g0010101030 = dataL0g0010101030[:,][:,5*0+2]
EigenValReL0g0010101030 = dataL0g0010101030[:,][:,5*0+3]
EigenValImL0g0010101030 = dataL0g0010101030[:,][:,5*0+4]

dataL0g0010101040 = np.genfromtxt('./L0/gK010/aK010/S1/N040/HamVals.txt')

MomentumAxL0g0010101040 = dataL0g0010101040[:,][:,5*0+0]
KineticEneL0g0010101040 = dataL0g0010101040[:,][:,5*0+1]
SelfEnergyL0g0010101040 = dataL0g0010101040[:,][:,5*0+2]
EigenValReL0g0010101040 = dataL0g0010101040[:,][:,5*0+3]
EigenValImL0g0010101040 = dataL0g0010101040[:,][:,5*0+4]

dataL0g0010101050 = np.genfromtxt('./L0/gK010/aK010/S1/N050/HamVals.txt')

MomentumAxL0g0010101050 = dataL0g0010101050[:,][:,5*0+0]
KineticEneL0g0010101050 = dataL0g0010101050[:,][:,5*0+1]
SelfEnergyL0g0010101050 = dataL0g0010101050[:,][:,5*0+2]
EigenValReL0g0010101050 = dataL0g0010101050[:,][:,5*0+3]
EigenValImL0g0010101050 = dataL0g0010101050[:,][:,5*0+4]

dataL0g0010201010 = np.genfromtxt('./L0/gK010/aK020/S1/N010/HamVals.txt')

MomentumAxL0g0010201010 = dataL0g0010201010[:,][:,5*0+0]
KineticEneL0g0010201010 = dataL0g0010201010[:,][:,5*0+1]
SelfEnergyL0g0010201010 = dataL0g0010201010[:,][:,5*0+2]
EigenValReL0g0010201010 = dataL0g0010201010[:,][:,5*0+3]
EigenValImL0g0010201010 = dataL0g0010201010[:,][:,5*0+4]

dataL0g0010201020 = np.genfromtxt('./L0/gK010/aK020/S1/N020/HamVals.txt')

MomentumAxL0g0010201020 = dataL0g0010201020[:,][:,5*0+0]
KineticEneL0g0010201020 = dataL0g0010201020[:,][:,5*0+1]
SelfEnergyL0g0010201020 = dataL0g0010201020[:,][:,5*0+2]
EigenValReL0g0010201020 = dataL0g0010201020[:,][:,5*0+3]
EigenValImL0g0010201020 = dataL0g0010201020[:,][:,5*0+4]

dataL0g0010201030 = np.genfromtxt('./L0/gK010/aK020/S1/N030/HamVals.txt')

MomentumAxL0g0010201030 = dataL0g0010201030[:,][:,5*0+0]
KineticEneL0g0010201030 = dataL0g0010201030[:,][:,5*0+1]
SelfEnergyL0g0010201030 = dataL0g0010201030[:,][:,5*0+2]
EigenValReL0g0010201030 = dataL0g0010201030[:,][:,5*0+3]
EigenValImL0g0010201030 = dataL0g0010201030[:,][:,5*0+4]

dataL0g0010201040 = np.genfromtxt('./L0/gK010/aK020/S1/N040/HamVals.txt')

MomentumAxL0g0010201040 = dataL0g0010201040[:,][:,5*0+0]
KineticEneL0g0010201040 = dataL0g0010201040[:,][:,5*0+1]
SelfEnergyL0g0010201040 = dataL0g0010201040[:,][:,5*0+2]
EigenValReL0g0010201040 = dataL0g0010201040[:,][:,5*0+3]
EigenValImL0g0010201040 = dataL0g0010201040[:,][:,5*0+4]

dataL0g0010201050 = np.genfromtxt('./L0/gK010/aK020/S1/N050/HamVals.txt')

MomentumAxL0g0010201050 = dataL0g0010201050[:,][:,5*0+0]
KineticEneL0g0010201050 = dataL0g0010201050[:,][:,5*0+1]
SelfEnergyL0g0010201050 = dataL0g0010201050[:,][:,5*0+2]
EigenValReL0g0010201050 = dataL0g0010201050[:,][:,5*0+3]
EigenValImL0g0010201050 = dataL0g0010201050[:,][:,5*0+4]

MaxEigenValImL0g0101010 = np.zeros((4))
MaxEigenValImL0g0101020 = np.zeros((4))
MaxEigenValImL0g0101030 = np.zeros((4))
MaxEigenValImL0g0101040 = np.zeros((4))
MaxEigenValImL0g0101050 = np.zeros((4))
MaxEigenValImL0g0101Inf = np.zeros((4))

MaxEigenValImL0g0101010[0] = np.max(EigenValImL0g0010011010)
MaxEigenValImL0g0101010[1] = np.max(EigenValImL0g0010021010)
MaxEigenValImL0g0101010[2] = np.max(EigenValImL0g0010051010)
MaxEigenValImL0g0101010[3] = np.max(EigenValImL0g0010101010)
#MaxEigenValImL0g0101010[4] = np.max(EigenValImL0g0010201010)

MaxEigenValImL0g0101020[0] = np.max(EigenValImL0g0010011020)
MaxEigenValImL0g0101020[1] = np.max(EigenValImL0g0010021020)
MaxEigenValImL0g0101020[2] = np.max(EigenValImL0g0010051020)
MaxEigenValImL0g0101020[3] = np.max(EigenValImL0g0010101020)
#MaxEigenValImL0g0101020[4] = np.max(EigenValImL0g0010201020)

MaxEigenValImL0g0101030[0] = np.max(EigenValImL0g0010011030)
MaxEigenValImL0g0101030[1] = np.max(EigenValImL0g0010021030)
MaxEigenValImL0g0101030[2] = np.max(EigenValImL0g0010051030)
MaxEigenValImL0g0101030[3] = np.max(EigenValImL0g0010101030)
#MaxEigenValImL0g0101030[4] = np.max(EigenValImL0g0010201030)

MaxEigenValImL0g0101040[0] = np.max(EigenValImL0g0010011040)
MaxEigenValImL0g0101040[1] = np.max(EigenValImL0g0010021040)
MaxEigenValImL0g0101040[2] = np.max(EigenValImL0g0010051040)
MaxEigenValImL0g0101040[3] = np.max(EigenValImL0g0010101040)
#MaxEigenValImL0g0101040[4] = np.max(EigenValImL0g0010201040)

MaxEigenValImL0g0101050[0] = np.max(EigenValImL0g0010011050)
MaxEigenValImL0g0101050[1] = np.max(EigenValImL0g0010021050)
MaxEigenValImL0g0101050[2] = np.max(EigenValImL0g0010051050)
MaxEigenValImL0g0101050[3] = np.max(EigenValImL0g0010101050)
#MaxEigenValImL0g0101050[4] = np.max(EigenValImL0g0010201050)

MaxEigenValImL0g0101Inf[0] = np.polyfit(fiveSizes, [MaxEigenValImL0g0101010[0],MaxEigenValImL0g0101020[0],MaxEigenValImL0g0101030[0],MaxEigenValImL0g0101040[0],MaxEigenValImL0g0101050[0]], 1)[[1]]
MaxEigenValImL0g0101Inf[1] = np.polyfit(fiveSizes, [MaxEigenValImL0g0101010[1],MaxEigenValImL0g0101020[1],MaxEigenValImL0g0101030[1],MaxEigenValImL0g0101040[1],MaxEigenValImL0g0101050[1]], 1)[[1]]
MaxEigenValImL0g0101Inf[2] = np.polyfit(fiveSizes, [MaxEigenValImL0g0101010[2],MaxEigenValImL0g0101020[2],MaxEigenValImL0g0101030[2],MaxEigenValImL0g0101040[2],MaxEigenValImL0g0101050[2]], 1)[[1]]
MaxEigenValImL0g0101Inf[3] = np.polyfit(fiveSizes, [MaxEigenValImL0g0101010[3],MaxEigenValImL0g0101020[3],MaxEigenValImL0g0101030[3],MaxEigenValImL0g0101040[3],MaxEigenValImL0g0101050[3]], 1)[[1]]
#MaxEigenValImL0g0101Inf[4] = np.polyfit(fiveSizes, [MaxEigenValImL0g0101010[4],MaxEigenValImL0g0101020[4],MaxEigenValImL0g0101030[4],MaxEigenValImL0g0101040[4],MaxEigenValImL0g0101050[4]], 1)[[1]]

########################################################################
########################################################################











































########################################################################
########################################################################

dataL2g0010011010 = np.genfromtxt('./L2/gK001/aK001/S1/N010/HamVals.txt')

MomentumAxL2g0010011010 = dataL2g0010011010[:,][:,5*0+0]
KineticEneL2g0010011010 = dataL2g0010011010[:,][:,5*0+1]
SelfEnergyL2g0010011010 = dataL2g0010011010[:,][:,5*0+2]
EigenValReL2g0010011010 = dataL2g0010011010[:,][:,5*0+3]
EigenValImL2g0010011010 = dataL2g0010011010[:,][:,5*0+4]

dataL2g0010011020 = np.genfromtxt('./L2/gK001/aK001/S1/N020/HamVals.txt')

MomentumAxL2g0010011020 = dataL2g0010011020[:,][:,5*0+0]
KineticEneL2g0010011020 = dataL2g0010011020[:,][:,5*0+1]
SelfEnergyL2g0010011020 = dataL2g0010011020[:,][:,5*0+2]
EigenValReL2g0010011020 = dataL2g0010011020[:,][:,5*0+3]
EigenValImL2g0010011020 = dataL2g0010011020[:,][:,5*0+4]

dataL2g0010011030 = np.genfromtxt('./L2/gK001/aK001/S1/N030/HamVals.txt')

MomentumAxL2g0010011030 = dataL2g0010011030[:,][:,5*0+0]
KineticEneL2g0010011030 = dataL2g0010011030[:,][:,5*0+1]
SelfEnergyL2g0010011030 = dataL2g0010011030[:,][:,5*0+2]
EigenValReL2g0010011030 = dataL2g0010011030[:,][:,5*0+3]
EigenValImL2g0010011030 = dataL2g0010011030[:,][:,5*0+4]

dataL2g0010011040 = np.genfromtxt('./L2/gK001/aK001/S1/N040/HamVals.txt')

MomentumAxL2g0010011040 = dataL2g0010011040[:,][:,5*0+0]
KineticEneL2g0010011040 = dataL2g0010011040[:,][:,5*0+1]
SelfEnergyL2g0010011040 = dataL2g0010011040[:,][:,5*0+2]
EigenValReL2g0010011040 = dataL2g0010011040[:,][:,5*0+3]
EigenValImL2g0010011040 = dataL2g0010011040[:,][:,5*0+4]

dataL2g0010011050 = np.genfromtxt('./L2/gK001/aK001/S1/N050/HamVals.txt')

MomentumAxL2g0010011050 = dataL2g0010011050[:,][:,5*0+0]
KineticEneL2g0010011050 = dataL2g0010011050[:,][:,5*0+1]
SelfEnergyL2g0010011050 = dataL2g0010011050[:,][:,5*0+2]
EigenValReL2g0010011050 = dataL2g0010011050[:,][:,5*0+3]
EigenValImL2g0010011050 = dataL2g0010011050[:,][:,5*0+4]

dataL2g0010021010 = np.genfromtxt('./L2/gK001/aK002/S1/N010/HamVals.txt')

MomentumAxL2g0010021010 = dataL2g0010021010[:,][:,5*0+0]
KineticEneL2g0010021010 = dataL2g0010021010[:,][:,5*0+1]
SelfEnergyL2g0010021010 = dataL2g0010021010[:,][:,5*0+2]
EigenValReL2g0010021010 = dataL2g0010021010[:,][:,5*0+3]
EigenValImL2g0010021010 = dataL2g0010021010[:,][:,5*0+4]

dataL2g0010021020 = np.genfromtxt('./L2/gK001/aK002/S1/N020/HamVals.txt')

MomentumAxL2g0010021020 = dataL2g0010021020[:,][:,5*0+0]
KineticEneL2g0010021020 = dataL2g0010021020[:,][:,5*0+1]
SelfEnergyL2g0010021020 = dataL2g0010021020[:,][:,5*0+2]
EigenValReL2g0010021020 = dataL2g0010021020[:,][:,5*0+3]
EigenValImL2g0010021020 = dataL2g0010021020[:,][:,5*0+4]

dataL2g0010021030 = np.genfromtxt('./L2/gK001/aK002/S1/N030/HamVals.txt')

MomentumAxL2g0010021030 = dataL2g0010021030[:,][:,5*0+0]
KineticEneL2g0010021030 = dataL2g0010021030[:,][:,5*0+1]
SelfEnergyL2g0010021030 = dataL2g0010021030[:,][:,5*0+2]
EigenValReL2g0010021030 = dataL2g0010021030[:,][:,5*0+3]
EigenValImL2g0010021030 = dataL2g0010021030[:,][:,5*0+4]

dataL2g0010021040 = np.genfromtxt('./L2/gK001/aK002/S1/N040/HamVals.txt')

MomentumAxL2g0010021040 = dataL2g0010021040[:,][:,5*0+0]
KineticEneL2g0010021040 = dataL2g0010021040[:,][:,5*0+1]
SelfEnergyL2g0010021040 = dataL2g0010021040[:,][:,5*0+2]
EigenValReL2g0010021040 = dataL2g0010021040[:,][:,5*0+3]
EigenValImL2g0010021040 = dataL2g0010021040[:,][:,5*0+4]

dataL2g0010021050 = np.genfromtxt('./L2/gK001/aK002/S1/N050/HamVals.txt')

MomentumAxL2g0010021050 = dataL2g0010021050[:,][:,5*0+0]
KineticEneL2g0010021050 = dataL2g0010021050[:,][:,5*0+1]
SelfEnergyL2g0010021050 = dataL2g0010021050[:,][:,5*0+2]
EigenValReL2g0010021050 = dataL2g0010021050[:,][:,5*0+3]
EigenValImL2g0010021050 = dataL2g0010021050[:,][:,5*0+4]

dataL2g0010051010 = np.genfromtxt('./L2/gK001/aK005/S1/N010/HamVals.txt')

MomentumAxL2g0010051010 = dataL2g0010051010[:,][:,5*0+0]
KineticEneL2g0010051010 = dataL2g0010051010[:,][:,5*0+1]
SelfEnergyL2g0010051010 = dataL2g0010051010[:,][:,5*0+2]
EigenValReL2g0010051010 = dataL2g0010051010[:,][:,5*0+3]
EigenValImL2g0010051010 = dataL2g0010051010[:,][:,5*0+4]

dataL2g0010051020 = np.genfromtxt('./L2/gK001/aK005/S1/N020/HamVals.txt')

MomentumAxL2g0010051020 = dataL2g0010051020[:,][:,5*0+0]
KineticEneL2g0010051020 = dataL2g0010051020[:,][:,5*0+1]
SelfEnergyL2g0010051020 = dataL2g0010051020[:,][:,5*0+2]
EigenValReL2g0010051020 = dataL2g0010051020[:,][:,5*0+3]
EigenValImL2g0010051020 = dataL2g0010051020[:,][:,5*0+4]

dataL2g0010051030 = np.genfromtxt('./L2/gK001/aK005/S1/N030/HamVals.txt')

MomentumAxL2g0010051030 = dataL2g0010051030[:,][:,5*0+0]
KineticEneL2g0010051030 = dataL2g0010051030[:,][:,5*0+1]
SelfEnergyL2g0010051030 = dataL2g0010051030[:,][:,5*0+2]
EigenValReL2g0010051030 = dataL2g0010051030[:,][:,5*0+3]
EigenValImL2g0010051030 = dataL2g0010051030[:,][:,5*0+4]

dataL2g0010051040 = np.genfromtxt('./L2/gK001/aK005/S1/N040/HamVals.txt')

MomentumAxL2g0010051040 = dataL2g0010051040[:,][:,5*0+0]
KineticEneL2g0010051040 = dataL2g0010051040[:,][:,5*0+1]
SelfEnergyL2g0010051040 = dataL2g0010051040[:,][:,5*0+2]
EigenValReL2g0010051040 = dataL2g0010051040[:,][:,5*0+3]
EigenValImL2g0010051040 = dataL2g0010051040[:,][:,5*0+4]

dataL2g0010051050 = np.genfromtxt('./L2/gK001/aK005/S1/N050/HamVals.txt')

MomentumAxL2g0010051050 = dataL2g0010051050[:,][:,5*0+0]
KineticEneL2g0010051050 = dataL2g0010051050[:,][:,5*0+1]
SelfEnergyL2g0010051050 = dataL2g0010051050[:,][:,5*0+2]
EigenValReL2g0010051050 = dataL2g0010051050[:,][:,5*0+3]
EigenValImL2g0010051050 = dataL2g0010051050[:,][:,5*0+4]

dataL2g0010101010 = np.genfromtxt('./L2/gK001/aK010/S1/N010/HamVals.txt')

MomentumAxL2g0010101010 = dataL2g0010101010[:,][:,5*0+0]
KineticEneL2g0010101010 = dataL2g0010101010[:,][:,5*0+1]
SelfEnergyL2g0010101010 = dataL2g0010101010[:,][:,5*0+2]
EigenValReL2g0010101010 = dataL2g0010101010[:,][:,5*0+3]
EigenValImL2g0010101010 = dataL2g0010101010[:,][:,5*0+4]

dataL2g0010101020 = np.genfromtxt('./L2/gK001/aK010/S1/N020/HamVals.txt')

MomentumAxL2g0010101020 = dataL2g0010101020[:,][:,5*0+0]
KineticEneL2g0010101020 = dataL2g0010101020[:,][:,5*0+1]
SelfEnergyL2g0010101020 = dataL2g0010101020[:,][:,5*0+2]
EigenValReL2g0010101020 = dataL2g0010101020[:,][:,5*0+3]
EigenValImL2g0010101020 = dataL2g0010101020[:,][:,5*0+4]

dataL2g0010101030 = np.genfromtxt('./L2/gK001/aK010/S1/N030/HamVals.txt')

MomentumAxL2g0010101030 = dataL2g0010101030[:,][:,5*0+0]
KineticEneL2g0010101030 = dataL2g0010101030[:,][:,5*0+1]
SelfEnergyL2g0010101030 = dataL2g0010101030[:,][:,5*0+2]
EigenValReL2g0010101030 = dataL2g0010101030[:,][:,5*0+3]
EigenValImL2g0010101030 = dataL2g0010101030[:,][:,5*0+4]

dataL2g0010101040 = np.genfromtxt('./L2/gK001/aK010/S1/N040/HamVals.txt')

MomentumAxL2g0010101040 = dataL2g0010101040[:,][:,5*0+0]
KineticEneL2g0010101040 = dataL2g0010101040[:,][:,5*0+1]
SelfEnergyL2g0010101040 = dataL2g0010101040[:,][:,5*0+2]
EigenValReL2g0010101040 = dataL2g0010101040[:,][:,5*0+3]
EigenValImL2g0010101040 = dataL2g0010101040[:,][:,5*0+4]

dataL2g0010101050 = np.genfromtxt('./L2/gK001/aK010/S1/N050/HamVals.txt')

MomentumAxL2g0010101050 = dataL2g0010101050[:,][:,5*0+0]
KineticEneL2g0010101050 = dataL2g0010101050[:,][:,5*0+1]
SelfEnergyL2g0010101050 = dataL2g0010101050[:,][:,5*0+2]
EigenValReL2g0010101050 = dataL2g0010101050[:,][:,5*0+3]
EigenValImL2g0010101050 = dataL2g0010101050[:,][:,5*0+4]

dataL2g0010201010 = np.genfromtxt('./L2/gK001/aK020/S1/N010/HamVals.txt')

MomentumAxL2g0010201010 = dataL2g0010201010[:,][:,5*0+0]
KineticEneL2g0010201010 = dataL2g0010201010[:,][:,5*0+1]
SelfEnergyL2g0010201010 = dataL2g0010201010[:,][:,5*0+2]
EigenValReL2g0010201010 = dataL2g0010201010[:,][:,5*0+3]
EigenValImL2g0010201010 = dataL2g0010201010[:,][:,5*0+4]

dataL2g0010201020 = np.genfromtxt('./L2/gK001/aK020/S1/N020/HamVals.txt')

MomentumAxL2g0010201020 = dataL2g0010201020[:,][:,5*0+0]
KineticEneL2g0010201020 = dataL2g0010201020[:,][:,5*0+1]
SelfEnergyL2g0010201020 = dataL2g0010201020[:,][:,5*0+2]
EigenValReL2g0010201020 = dataL2g0010201020[:,][:,5*0+3]
EigenValImL2g0010201020 = dataL2g0010201020[:,][:,5*0+4]

dataL2g0010201030 = np.genfromtxt('./L2/gK001/aK020/S1/N030/HamVals.txt')

MomentumAxL2g0010201030 = dataL2g0010201030[:,][:,5*0+0]
KineticEneL2g0010201030 = dataL2g0010201030[:,][:,5*0+1]
SelfEnergyL2g0010201030 = dataL2g0010201030[:,][:,5*0+2]
EigenValReL2g0010201030 = dataL2g0010201030[:,][:,5*0+3]
EigenValImL2g0010201030 = dataL2g0010201030[:,][:,5*0+4]

dataL2g0010201040 = np.genfromtxt('./L2/gK001/aK020/S1/N040/HamVals.txt')

MomentumAxL2g0010201040 = dataL2g0010201040[:,][:,5*0+0]
KineticEneL2g0010201040 = dataL2g0010201040[:,][:,5*0+1]
SelfEnergyL2g0010201040 = dataL2g0010201040[:,][:,5*0+2]
EigenValReL2g0010201040 = dataL2g0010201040[:,][:,5*0+3]
EigenValImL2g0010201040 = dataL2g0010201040[:,][:,5*0+4]

dataL2g0010201050 = np.genfromtxt('./L2/gK001/aK020/S1/N050/HamVals.txt')

MomentumAxL2g0010201050 = dataL2g0010201050[:,][:,5*0+0]
KineticEneL2g0010201050 = dataL2g0010201050[:,][:,5*0+1]
SelfEnergyL2g0010201050 = dataL2g0010201050[:,][:,5*0+2]
EigenValReL2g0010201050 = dataL2g0010201050[:,][:,5*0+3]
EigenValImL2g0010201050 = dataL2g0010201050[:,][:,5*0+4]

MaxEigenValImL2g0011010 = np.zeros((4))
MaxEigenValImL2g0011020 = np.zeros((4))
MaxEigenValImL2g0011030 = np.zeros((4))
MaxEigenValImL2g0011040 = np.zeros((4))
MaxEigenValImL2g0011050 = np.zeros((4))
MaxEigenValImL2g0011Inf = np.zeros((4))

MaxEigenValImL2g0011010[0] = np.max(EigenValImL2g0010011010)
MaxEigenValImL2g0011010[1] = np.max(EigenValImL2g0010021010)
MaxEigenValImL2g0011010[2] = np.max(EigenValImL2g0010051010)
MaxEigenValImL2g0011010[3] = np.max(EigenValImL2g0010101010)
#MaxEigenValImL2g0011010[4] = np.max(EigenValImL2g0010201010)

MaxEigenValImL2g0011020[0] = np.max(EigenValImL2g0010011020)
MaxEigenValImL2g0011020[1] = np.max(EigenValImL2g0010021020)
MaxEigenValImL2g0011020[2] = np.max(EigenValImL2g0010051020)
MaxEigenValImL2g0011020[3] = np.max(EigenValImL2g0010101020)
#MaxEigenValImL2g0011020[4] = np.max(EigenValImL2g0010201020)

MaxEigenValImL2g0011030[0] = np.max(EigenValImL2g0010011030)
MaxEigenValImL2g0011030[1] = np.max(EigenValImL2g0010021030)
MaxEigenValImL2g0011030[2] = np.max(EigenValImL2g0010051030)
MaxEigenValImL2g0011030[3] = np.max(EigenValImL2g0010101030)
#MaxEigenValImL2g0011030[4] = np.max(EigenValImL2g0010201030)

MaxEigenValImL2g0011040[0] = np.max(EigenValImL2g0010011040)
MaxEigenValImL2g0011040[1] = np.max(EigenValImL2g0010021040)
MaxEigenValImL2g0011040[2] = np.max(EigenValImL2g0010051040)
MaxEigenValImL2g0011040[3] = np.max(EigenValImL2g0010101040)
#MaxEigenValImL2g0011040[4] = np.max(EigenValImL2g0010201040)

MaxEigenValImL2g0011050[0] = np.max(EigenValImL2g0010011050)
MaxEigenValImL2g0011050[1] = np.max(EigenValImL2g0010021050)
MaxEigenValImL2g0011050[2] = np.max(EigenValImL2g0010051050)
MaxEigenValImL2g0011050[3] = np.max(EigenValImL2g0010101050)
#MaxEigenValImL2g0011050[4] = np.max(EigenValImL2g0010201050)

MaxEigenValImL2g0011Inf[0] = np.polyfit(fiveSizes, [MaxEigenValImL2g0011010[0],MaxEigenValImL2g0011020[0],MaxEigenValImL2g0011030[0],MaxEigenValImL2g0011040[0],MaxEigenValImL2g0011050[0]], 1)[[1]]
MaxEigenValImL2g0011Inf[1] = np.polyfit(fiveSizes, [MaxEigenValImL2g0011010[1],MaxEigenValImL2g0011020[1],MaxEigenValImL2g0011030[1],MaxEigenValImL2g0011040[1],MaxEigenValImL2g0011050[1]], 1)[[1]]
MaxEigenValImL2g0011Inf[2] = np.polyfit(fiveSizes, [MaxEigenValImL2g0011010[2],MaxEigenValImL2g0011020[2],MaxEigenValImL2g0011030[2],MaxEigenValImL2g0011040[2],MaxEigenValImL2g0011050[2]], 1)[[1]]
MaxEigenValImL2g0011Inf[3] = np.polyfit(fiveSizes, [MaxEigenValImL2g0011010[3],MaxEigenValImL2g0011020[3],MaxEigenValImL2g0011030[3],MaxEigenValImL2g0011040[3],MaxEigenValImL2g0011050[3]], 1)[[1]]
#MaxEigenValImL2g0011Inf[4] = np.polyfit(fiveSizes, [MaxEigenValImL2g0011010[4],MaxEigenValImL2g0011020[4],MaxEigenValImL2g0011030[4],MaxEigenValImL2g0011040[4],MaxEigenValImL2g0011050[4]], 1)[[1]]

########################################################################

dataL2g0010011010 = np.genfromtxt('./L2/gK002/aK001/S1/N010/HamVals.txt')

MomentumAxL2g0010011010 = dataL2g0010011010[:,][:,5*0+0]
KineticEneL2g0010011010 = dataL2g0010011010[:,][:,5*0+1]
SelfEnergyL2g0010011010 = dataL2g0010011010[:,][:,5*0+2]
EigenValReL2g0010011010 = dataL2g0010011010[:,][:,5*0+3]
EigenValImL2g0010011010 = dataL2g0010011010[:,][:,5*0+4]

dataL2g0010011020 = np.genfromtxt('./L2/gK002/aK001/S1/N020/HamVals.txt')

MomentumAxL2g0010011020 = dataL2g0010011020[:,][:,5*0+0]
KineticEneL2g0010011020 = dataL2g0010011020[:,][:,5*0+1]
SelfEnergyL2g0010011020 = dataL2g0010011020[:,][:,5*0+2]
EigenValReL2g0010011020 = dataL2g0010011020[:,][:,5*0+3]
EigenValImL2g0010011020 = dataL2g0010011020[:,][:,5*0+4]

dataL2g0010011030 = np.genfromtxt('./L2/gK002/aK001/S1/N030/HamVals.txt')

MomentumAxL2g0010011030 = dataL2g0010011030[:,][:,5*0+0]
KineticEneL2g0010011030 = dataL2g0010011030[:,][:,5*0+1]
SelfEnergyL2g0010011030 = dataL2g0010011030[:,][:,5*0+2]
EigenValReL2g0010011030 = dataL2g0010011030[:,][:,5*0+3]
EigenValImL2g0010011030 = dataL2g0010011030[:,][:,5*0+4]

dataL2g0010011040 = np.genfromtxt('./L2/gK002/aK001/S1/N040/HamVals.txt')

MomentumAxL2g0010011040 = dataL2g0010011040[:,][:,5*0+0]
KineticEneL2g0010011040 = dataL2g0010011040[:,][:,5*0+1]
SelfEnergyL2g0010011040 = dataL2g0010011040[:,][:,5*0+2]
EigenValReL2g0010011040 = dataL2g0010011040[:,][:,5*0+3]
EigenValImL2g0010011040 = dataL2g0010011040[:,][:,5*0+4]

dataL2g0010011050 = np.genfromtxt('./L2/gK002/aK001/S1/N050/HamVals.txt')

MomentumAxL2g0010011050 = dataL2g0010011050[:,][:,5*0+0]
KineticEneL2g0010011050 = dataL2g0010011050[:,][:,5*0+1]
SelfEnergyL2g0010011050 = dataL2g0010011050[:,][:,5*0+2]
EigenValReL2g0010011050 = dataL2g0010011050[:,][:,5*0+3]
EigenValImL2g0010011050 = dataL2g0010011050[:,][:,5*0+4]

dataL2g0010021010 = np.genfromtxt('./L2/gK002/aK002/S1/N010/HamVals.txt')

MomentumAxL2g0010021010 = dataL2g0010021010[:,][:,5*0+0]
KineticEneL2g0010021010 = dataL2g0010021010[:,][:,5*0+1]
SelfEnergyL2g0010021010 = dataL2g0010021010[:,][:,5*0+2]
EigenValReL2g0010021010 = dataL2g0010021010[:,][:,5*0+3]
EigenValImL2g0010021010 = dataL2g0010021010[:,][:,5*0+4]

dataL2g0010021020 = np.genfromtxt('./L2/gK002/aK002/S1/N020/HamVals.txt')

MomentumAxL2g0010021020 = dataL2g0010021020[:,][:,5*0+0]
KineticEneL2g0010021020 = dataL2g0010021020[:,][:,5*0+1]
SelfEnergyL2g0010021020 = dataL2g0010021020[:,][:,5*0+2]
EigenValReL2g0010021020 = dataL2g0010021020[:,][:,5*0+3]
EigenValImL2g0010021020 = dataL2g0010021020[:,][:,5*0+4]

dataL2g0010021030 = np.genfromtxt('./L2/gK002/aK002/S1/N030/HamVals.txt')

MomentumAxL2g0010021030 = dataL2g0010021030[:,][:,5*0+0]
KineticEneL2g0010021030 = dataL2g0010021030[:,][:,5*0+1]
SelfEnergyL2g0010021030 = dataL2g0010021030[:,][:,5*0+2]
EigenValReL2g0010021030 = dataL2g0010021030[:,][:,5*0+3]
EigenValImL2g0010021030 = dataL2g0010021030[:,][:,5*0+4]

dataL2g0010021040 = np.genfromtxt('./L2/gK002/aK002/S1/N040/HamVals.txt')

MomentumAxL2g0010021040 = dataL2g0010021040[:,][:,5*0+0]
KineticEneL2g0010021040 = dataL2g0010021040[:,][:,5*0+1]
SelfEnergyL2g0010021040 = dataL2g0010021040[:,][:,5*0+2]
EigenValReL2g0010021040 = dataL2g0010021040[:,][:,5*0+3]
EigenValImL2g0010021040 = dataL2g0010021040[:,][:,5*0+4]

dataL2g0010021050 = np.genfromtxt('./L2/gK002/aK002/S1/N050/HamVals.txt')

MomentumAxL2g0010021050 = dataL2g0010021050[:,][:,5*0+0]
KineticEneL2g0010021050 = dataL2g0010021050[:,][:,5*0+1]
SelfEnergyL2g0010021050 = dataL2g0010021050[:,][:,5*0+2]
EigenValReL2g0010021050 = dataL2g0010021050[:,][:,5*0+3]
EigenValImL2g0010021050 = dataL2g0010021050[:,][:,5*0+4]

dataL2g0010051010 = np.genfromtxt('./L2/gK002/aK005/S1/N010/HamVals.txt')

MomentumAxL2g0010051010 = dataL2g0010051010[:,][:,5*0+0]
KineticEneL2g0010051010 = dataL2g0010051010[:,][:,5*0+1]
SelfEnergyL2g0010051010 = dataL2g0010051010[:,][:,5*0+2]
EigenValReL2g0010051010 = dataL2g0010051010[:,][:,5*0+3]
EigenValImL2g0010051010 = dataL2g0010051010[:,][:,5*0+4]

dataL2g0010051020 = np.genfromtxt('./L2/gK002/aK005/S1/N020/HamVals.txt')

MomentumAxL2g0010051020 = dataL2g0010051020[:,][:,5*0+0]
KineticEneL2g0010051020 = dataL2g0010051020[:,][:,5*0+1]
SelfEnergyL2g0010051020 = dataL2g0010051020[:,][:,5*0+2]
EigenValReL2g0010051020 = dataL2g0010051020[:,][:,5*0+3]
EigenValImL2g0010051020 = dataL2g0010051020[:,][:,5*0+4]

dataL2g0010051030 = np.genfromtxt('./L2/gK002/aK005/S1/N030/HamVals.txt')

MomentumAxL2g0010051030 = dataL2g0010051030[:,][:,5*0+0]
KineticEneL2g0010051030 = dataL2g0010051030[:,][:,5*0+1]
SelfEnergyL2g0010051030 = dataL2g0010051030[:,][:,5*0+2]
EigenValReL2g0010051030 = dataL2g0010051030[:,][:,5*0+3]
EigenValImL2g0010051030 = dataL2g0010051030[:,][:,5*0+4]

dataL2g0010051040 = np.genfromtxt('./L2/gK002/aK005/S1/N040/HamVals.txt')

MomentumAxL2g0010051040 = dataL2g0010051040[:,][:,5*0+0]
KineticEneL2g0010051040 = dataL2g0010051040[:,][:,5*0+1]
SelfEnergyL2g0010051040 = dataL2g0010051040[:,][:,5*0+2]
EigenValReL2g0010051040 = dataL2g0010051040[:,][:,5*0+3]
EigenValImL2g0010051040 = dataL2g0010051040[:,][:,5*0+4]

dataL2g0010051050 = np.genfromtxt('./L2/gK002/aK005/S1/N050/HamVals.txt')

MomentumAxL2g0010051050 = dataL2g0010051050[:,][:,5*0+0]
KineticEneL2g0010051050 = dataL2g0010051050[:,][:,5*0+1]
SelfEnergyL2g0010051050 = dataL2g0010051050[:,][:,5*0+2]
EigenValReL2g0010051050 = dataL2g0010051050[:,][:,5*0+3]
EigenValImL2g0010051050 = dataL2g0010051050[:,][:,5*0+4]

dataL2g0010101010 = np.genfromtxt('./L2/gK002/aK010/S1/N010/HamVals.txt')

MomentumAxL2g0010101010 = dataL2g0010101010[:,][:,5*0+0]
KineticEneL2g0010101010 = dataL2g0010101010[:,][:,5*0+1]
SelfEnergyL2g0010101010 = dataL2g0010101010[:,][:,5*0+2]
EigenValReL2g0010101010 = dataL2g0010101010[:,][:,5*0+3]
EigenValImL2g0010101010 = dataL2g0010101010[:,][:,5*0+4]

dataL2g0010101020 = np.genfromtxt('./L2/gK002/aK010/S1/N020/HamVals.txt')

MomentumAxL2g0010101020 = dataL2g0010101020[:,][:,5*0+0]
KineticEneL2g0010101020 = dataL2g0010101020[:,][:,5*0+1]
SelfEnergyL2g0010101020 = dataL2g0010101020[:,][:,5*0+2]
EigenValReL2g0010101020 = dataL2g0010101020[:,][:,5*0+3]
EigenValImL2g0010101020 = dataL2g0010101020[:,][:,5*0+4]

dataL2g0010101030 = np.genfromtxt('./L2/gK002/aK010/S1/N030/HamVals.txt')

MomentumAxL2g0010101030 = dataL2g0010101030[:,][:,5*0+0]
KineticEneL2g0010101030 = dataL2g0010101030[:,][:,5*0+1]
SelfEnergyL2g0010101030 = dataL2g0010101030[:,][:,5*0+2]
EigenValReL2g0010101030 = dataL2g0010101030[:,][:,5*0+3]
EigenValImL2g0010101030 = dataL2g0010101030[:,][:,5*0+4]

dataL2g0010101040 = np.genfromtxt('./L2/gK002/aK010/S1/N040/HamVals.txt')

MomentumAxL2g0010101040 = dataL2g0010101040[:,][:,5*0+0]
KineticEneL2g0010101040 = dataL2g0010101040[:,][:,5*0+1]
SelfEnergyL2g0010101040 = dataL2g0010101040[:,][:,5*0+2]
EigenValReL2g0010101040 = dataL2g0010101040[:,][:,5*0+3]
EigenValImL2g0010101040 = dataL2g0010101040[:,][:,5*0+4]

dataL2g0010101050 = np.genfromtxt('./L2/gK002/aK010/S1/N050/HamVals.txt')

MomentumAxL2g0010101050 = dataL2g0010101050[:,][:,5*0+0]
KineticEneL2g0010101050 = dataL2g0010101050[:,][:,5*0+1]
SelfEnergyL2g0010101050 = dataL2g0010101050[:,][:,5*0+2]
EigenValReL2g0010101050 = dataL2g0010101050[:,][:,5*0+3]
EigenValImL2g0010101050 = dataL2g0010101050[:,][:,5*0+4]

dataL2g0010201010 = np.genfromtxt('./L2/gK002/aK020/S1/N010/HamVals.txt')

MomentumAxL2g0010201010 = dataL2g0010201010[:,][:,5*0+0]
KineticEneL2g0010201010 = dataL2g0010201010[:,][:,5*0+1]
SelfEnergyL2g0010201010 = dataL2g0010201010[:,][:,5*0+2]
EigenValReL2g0010201010 = dataL2g0010201010[:,][:,5*0+3]
EigenValImL2g0010201010 = dataL2g0010201010[:,][:,5*0+4]

dataL2g0010201020 = np.genfromtxt('./L2/gK002/aK020/S1/N020/HamVals.txt')

MomentumAxL2g0010201020 = dataL2g0010201020[:,][:,5*0+0]
KineticEneL2g0010201020 = dataL2g0010201020[:,][:,5*0+1]
SelfEnergyL2g0010201020 = dataL2g0010201020[:,][:,5*0+2]
EigenValReL2g0010201020 = dataL2g0010201020[:,][:,5*0+3]
EigenValImL2g0010201020 = dataL2g0010201020[:,][:,5*0+4]

dataL2g0010201030 = np.genfromtxt('./L2/gK002/aK020/S1/N030/HamVals.txt')

MomentumAxL2g0010201030 = dataL2g0010201030[:,][:,5*0+0]
KineticEneL2g0010201030 = dataL2g0010201030[:,][:,5*0+1]
SelfEnergyL2g0010201030 = dataL2g0010201030[:,][:,5*0+2]
EigenValReL2g0010201030 = dataL2g0010201030[:,][:,5*0+3]
EigenValImL2g0010201030 = dataL2g0010201030[:,][:,5*0+4]

dataL2g0010201040 = np.genfromtxt('./L2/gK002/aK020/S1/N040/HamVals.txt')

MomentumAxL2g0010201040 = dataL2g0010201040[:,][:,5*0+0]
KineticEneL2g0010201040 = dataL2g0010201040[:,][:,5*0+1]
SelfEnergyL2g0010201040 = dataL2g0010201040[:,][:,5*0+2]
EigenValReL2g0010201040 = dataL2g0010201040[:,][:,5*0+3]
EigenValImL2g0010201040 = dataL2g0010201040[:,][:,5*0+4]

dataL2g0010201050 = np.genfromtxt('./L2/gK002/aK020/S1/N050/HamVals.txt')

MomentumAxL2g0010201050 = dataL2g0010201050[:,][:,5*0+0]
KineticEneL2g0010201050 = dataL2g0010201050[:,][:,5*0+1]
SelfEnergyL2g0010201050 = dataL2g0010201050[:,][:,5*0+2]
EigenValReL2g0010201050 = dataL2g0010201050[:,][:,5*0+3]
EigenValImL2g0010201050 = dataL2g0010201050[:,][:,5*0+4]

MaxEigenValImL2g0021010 = np.zeros((4))
MaxEigenValImL2g0021020 = np.zeros((4))
MaxEigenValImL2g0021030 = np.zeros((4))
MaxEigenValImL2g0021040 = np.zeros((4))
MaxEigenValImL2g0021050 = np.zeros((4))
MaxEigenValImL2g0021Inf = np.zeros((4))

MaxEigenValImL2g0021010[0] = np.max(EigenValImL2g0010011010)
MaxEigenValImL2g0021010[1] = np.max(EigenValImL2g0010021010)
MaxEigenValImL2g0021010[2] = np.max(EigenValImL2g0010051010)
MaxEigenValImL2g0021010[3] = np.max(EigenValImL2g0010101010)
#MaxEigenValImL2g0021010[4] = np.max(EigenValImL2g0010201010)

MaxEigenValImL2g0021020[0] = np.max(EigenValImL2g0010011020)
MaxEigenValImL2g0021020[1] = np.max(EigenValImL2g0010021020)
MaxEigenValImL2g0021020[2] = np.max(EigenValImL2g0010051020)
MaxEigenValImL2g0021020[3] = np.max(EigenValImL2g0010101020)
#MaxEigenValImL2g0021020[4] = np.max(EigenValImL2g0010201020)

MaxEigenValImL2g0021030[0] = np.max(EigenValImL2g0010011030)
MaxEigenValImL2g0021030[1] = np.max(EigenValImL2g0010021030)
MaxEigenValImL2g0021030[2] = np.max(EigenValImL2g0010051030)
MaxEigenValImL2g0021030[3] = np.max(EigenValImL2g0010101030)
#MaxEigenValImL2g0021030[4] = np.max(EigenValImL2g0010201030)

MaxEigenValImL2g0021040[0] = np.max(EigenValImL2g0010011040)
MaxEigenValImL2g0021040[1] = np.max(EigenValImL2g0010021040)
MaxEigenValImL2g0021040[2] = np.max(EigenValImL2g0010051040)
MaxEigenValImL2g0021040[3] = np.max(EigenValImL2g0010101040)
#MaxEigenValImL2g0021040[4] = np.max(EigenValImL2g0010201040)

MaxEigenValImL2g0021050[0] = np.max(EigenValImL2g0010011050)
MaxEigenValImL2g0021050[1] = np.max(EigenValImL2g0010021050)
MaxEigenValImL2g0021050[2] = np.max(EigenValImL2g0010051050)
MaxEigenValImL2g0021050[3] = np.max(EigenValImL2g0010101050)
#MaxEigenValImL2g0021050[4] = np.max(EigenValImL2g0010201050)

MaxEigenValImL2g0021Inf[0] = np.polyfit(fiveSizes, [MaxEigenValImL2g0021010[0],MaxEigenValImL2g0021020[0],MaxEigenValImL2g0021030[0],MaxEigenValImL2g0021040[0],MaxEigenValImL2g0021050[0]], 1)[[1]]
MaxEigenValImL2g0021Inf[1] = np.polyfit(fiveSizes, [MaxEigenValImL2g0021010[1],MaxEigenValImL2g0021020[1],MaxEigenValImL2g0021030[1],MaxEigenValImL2g0021040[1],MaxEigenValImL2g0021050[1]], 1)[[1]]
MaxEigenValImL2g0021Inf[2] = np.polyfit(fiveSizes, [MaxEigenValImL2g0021010[2],MaxEigenValImL2g0021020[2],MaxEigenValImL2g0021030[2],MaxEigenValImL2g0021040[2],MaxEigenValImL2g0021050[2]], 1)[[1]]
MaxEigenValImL2g0021Inf[3] = np.polyfit(fiveSizes, [MaxEigenValImL2g0021010[3],MaxEigenValImL2g0021020[3],MaxEigenValImL2g0021030[3],MaxEigenValImL2g0021040[3],MaxEigenValImL2g0021050[3]], 1)[[1]]
#MaxEigenValImL2g0021Inf[4] = np.polyfit(fiveSizes, [MaxEigenValImL2g0021010[4],MaxEigenValImL2g0021020[4],MaxEigenValImL2g0021030[4],MaxEigenValImL2g0021040[4],MaxEigenValImL2g0021050[4]], 1)[[1]]

########################################################################

dataL2g0010011010 = np.genfromtxt('./L2/gK005/aK001/S1/N010/HamVals.txt')

MomentumAxL2g0010011010 = dataL2g0010011010[:,][:,5*0+0]
KineticEneL2g0010011010 = dataL2g0010011010[:,][:,5*0+1]
SelfEnergyL2g0010011010 = dataL2g0010011010[:,][:,5*0+2]
EigenValReL2g0010011010 = dataL2g0010011010[:,][:,5*0+3]
EigenValImL2g0010011010 = dataL2g0010011010[:,][:,5*0+4]

dataL2g0010011020 = np.genfromtxt('./L2/gK005/aK001/S1/N020/HamVals.txt')

MomentumAxL2g0010011020 = dataL2g0010011020[:,][:,5*0+0]
KineticEneL2g0010011020 = dataL2g0010011020[:,][:,5*0+1]
SelfEnergyL2g0010011020 = dataL2g0010011020[:,][:,5*0+2]
EigenValReL2g0010011020 = dataL2g0010011020[:,][:,5*0+3]
EigenValImL2g0010011020 = dataL2g0010011020[:,][:,5*0+4]

dataL2g0010011030 = np.genfromtxt('./L2/gK005/aK001/S1/N030/HamVals.txt')

MomentumAxL2g0010011030 = dataL2g0010011030[:,][:,5*0+0]
KineticEneL2g0010011030 = dataL2g0010011030[:,][:,5*0+1]
SelfEnergyL2g0010011030 = dataL2g0010011030[:,][:,5*0+2]
EigenValReL2g0010011030 = dataL2g0010011030[:,][:,5*0+3]
EigenValImL2g0010011030 = dataL2g0010011030[:,][:,5*0+4]

dataL2g0010011040 = np.genfromtxt('./L2/gK005/aK001/S1/N040/HamVals.txt')

MomentumAxL2g0010011040 = dataL2g0010011040[:,][:,5*0+0]
KineticEneL2g0010011040 = dataL2g0010011040[:,][:,5*0+1]
SelfEnergyL2g0010011040 = dataL2g0010011040[:,][:,5*0+2]
EigenValReL2g0010011040 = dataL2g0010011040[:,][:,5*0+3]
EigenValImL2g0010011040 = dataL2g0010011040[:,][:,5*0+4]

dataL2g0010011050 = np.genfromtxt('./L2/gK005/aK001/S1/N050/HamVals.txt')

MomentumAxL2g0010011050 = dataL2g0010011050[:,][:,5*0+0]
KineticEneL2g0010011050 = dataL2g0010011050[:,][:,5*0+1]
SelfEnergyL2g0010011050 = dataL2g0010011050[:,][:,5*0+2]
EigenValReL2g0010011050 = dataL2g0010011050[:,][:,5*0+3]
EigenValImL2g0010011050 = dataL2g0010011050[:,][:,5*0+4]

dataL2g0010021010 = np.genfromtxt('./L2/gK005/aK002/S1/N010/HamVals.txt')

MomentumAxL2g0010021010 = dataL2g0010021010[:,][:,5*0+0]
KineticEneL2g0010021010 = dataL2g0010021010[:,][:,5*0+1]
SelfEnergyL2g0010021010 = dataL2g0010021010[:,][:,5*0+2]
EigenValReL2g0010021010 = dataL2g0010021010[:,][:,5*0+3]
EigenValImL2g0010021010 = dataL2g0010021010[:,][:,5*0+4]

dataL2g0010021020 = np.genfromtxt('./L2/gK005/aK002/S1/N020/HamVals.txt')

MomentumAxL2g0010021020 = dataL2g0010021020[:,][:,5*0+0]
KineticEneL2g0010021020 = dataL2g0010021020[:,][:,5*0+1]
SelfEnergyL2g0010021020 = dataL2g0010021020[:,][:,5*0+2]
EigenValReL2g0010021020 = dataL2g0010021020[:,][:,5*0+3]
EigenValImL2g0010021020 = dataL2g0010021020[:,][:,5*0+4]

dataL2g0010021030 = np.genfromtxt('./L2/gK005/aK002/S1/N030/HamVals.txt')

MomentumAxL2g0010021030 = dataL2g0010021030[:,][:,5*0+0]
KineticEneL2g0010021030 = dataL2g0010021030[:,][:,5*0+1]
SelfEnergyL2g0010021030 = dataL2g0010021030[:,][:,5*0+2]
EigenValReL2g0010021030 = dataL2g0010021030[:,][:,5*0+3]
EigenValImL2g0010021030 = dataL2g0010021030[:,][:,5*0+4]

dataL2g0010021040 = np.genfromtxt('./L2/gK005/aK002/S1/N040/HamVals.txt')

MomentumAxL2g0010021040 = dataL2g0010021040[:,][:,5*0+0]
KineticEneL2g0010021040 = dataL2g0010021040[:,][:,5*0+1]
SelfEnergyL2g0010021040 = dataL2g0010021040[:,][:,5*0+2]
EigenValReL2g0010021040 = dataL2g0010021040[:,][:,5*0+3]
EigenValImL2g0010021040 = dataL2g0010021040[:,][:,5*0+4]

dataL2g0010021050 = np.genfromtxt('./L2/gK005/aK002/S1/N050/HamVals.txt')

MomentumAxL2g0010021050 = dataL2g0010021050[:,][:,5*0+0]
KineticEneL2g0010021050 = dataL2g0010021050[:,][:,5*0+1]
SelfEnergyL2g0010021050 = dataL2g0010021050[:,][:,5*0+2]
EigenValReL2g0010021050 = dataL2g0010021050[:,][:,5*0+3]
EigenValImL2g0010021050 = dataL2g0010021050[:,][:,5*0+4]

dataL2g0010051010 = np.genfromtxt('./L2/gK005/aK005/S1/N010/HamVals.txt')

MomentumAxL2g0010051010 = dataL2g0010051010[:,][:,5*0+0]
KineticEneL2g0010051010 = dataL2g0010051010[:,][:,5*0+1]
SelfEnergyL2g0010051010 = dataL2g0010051010[:,][:,5*0+2]
EigenValReL2g0010051010 = dataL2g0010051010[:,][:,5*0+3]
EigenValImL2g0010051010 = dataL2g0010051010[:,][:,5*0+4]

dataL2g0010051020 = np.genfromtxt('./L2/gK005/aK005/S1/N020/HamVals.txt')

MomentumAxL2g0010051020 = dataL2g0010051020[:,][:,5*0+0]
KineticEneL2g0010051020 = dataL2g0010051020[:,][:,5*0+1]
SelfEnergyL2g0010051020 = dataL2g0010051020[:,][:,5*0+2]
EigenValReL2g0010051020 = dataL2g0010051020[:,][:,5*0+3]
EigenValImL2g0010051020 = dataL2g0010051020[:,][:,5*0+4]

dataL2g0010051030 = np.genfromtxt('./L2/gK005/aK005/S1/N030/HamVals.txt')

MomentumAxL2g0010051030 = dataL2g0010051030[:,][:,5*0+0]
KineticEneL2g0010051030 = dataL2g0010051030[:,][:,5*0+1]
SelfEnergyL2g0010051030 = dataL2g0010051030[:,][:,5*0+2]
EigenValReL2g0010051030 = dataL2g0010051030[:,][:,5*0+3]
EigenValImL2g0010051030 = dataL2g0010051030[:,][:,5*0+4]

dataL2g0010051040 = np.genfromtxt('./L2/gK005/aK005/S1/N040/HamVals.txt')

MomentumAxL2g0010051040 = dataL2g0010051040[:,][:,5*0+0]
KineticEneL2g0010051040 = dataL2g0010051040[:,][:,5*0+1]
SelfEnergyL2g0010051040 = dataL2g0010051040[:,][:,5*0+2]
EigenValReL2g0010051040 = dataL2g0010051040[:,][:,5*0+3]
EigenValImL2g0010051040 = dataL2g0010051040[:,][:,5*0+4]

dataL2g0010051050 = np.genfromtxt('./L2/gK005/aK005/S1/N050/HamVals.txt')

MomentumAxL2g0010051050 = dataL2g0010051050[:,][:,5*0+0]
KineticEneL2g0010051050 = dataL2g0010051050[:,][:,5*0+1]
SelfEnergyL2g0010051050 = dataL2g0010051050[:,][:,5*0+2]
EigenValReL2g0010051050 = dataL2g0010051050[:,][:,5*0+3]
EigenValImL2g0010051050 = dataL2g0010051050[:,][:,5*0+4]

dataL2g0010101010 = np.genfromtxt('./L2/gK005/aK010/S1/N010/HamVals.txt')

MomentumAxL2g0010101010 = dataL2g0010101010[:,][:,5*0+0]
KineticEneL2g0010101010 = dataL2g0010101010[:,][:,5*0+1]
SelfEnergyL2g0010101010 = dataL2g0010101010[:,][:,5*0+2]
EigenValReL2g0010101010 = dataL2g0010101010[:,][:,5*0+3]
EigenValImL2g0010101010 = dataL2g0010101010[:,][:,5*0+4]

dataL2g0010101020 = np.genfromtxt('./L2/gK005/aK010/S1/N020/HamVals.txt')

MomentumAxL2g0010101020 = dataL2g0010101020[:,][:,5*0+0]
KineticEneL2g0010101020 = dataL2g0010101020[:,][:,5*0+1]
SelfEnergyL2g0010101020 = dataL2g0010101020[:,][:,5*0+2]
EigenValReL2g0010101020 = dataL2g0010101020[:,][:,5*0+3]
EigenValImL2g0010101020 = dataL2g0010101020[:,][:,5*0+4]

dataL2g0010101030 = np.genfromtxt('./L2/gK005/aK010/S1/N030/HamVals.txt')

MomentumAxL2g0010101030 = dataL2g0010101030[:,][:,5*0+0]
KineticEneL2g0010101030 = dataL2g0010101030[:,][:,5*0+1]
SelfEnergyL2g0010101030 = dataL2g0010101030[:,][:,5*0+2]
EigenValReL2g0010101030 = dataL2g0010101030[:,][:,5*0+3]
EigenValImL2g0010101030 = dataL2g0010101030[:,][:,5*0+4]

dataL2g0010101040 = np.genfromtxt('./L2/gK005/aK010/S1/N040/HamVals.txt')

MomentumAxL2g0010101040 = dataL2g0010101040[:,][:,5*0+0]
KineticEneL2g0010101040 = dataL2g0010101040[:,][:,5*0+1]
SelfEnergyL2g0010101040 = dataL2g0010101040[:,][:,5*0+2]
EigenValReL2g0010101040 = dataL2g0010101040[:,][:,5*0+3]
EigenValImL2g0010101040 = dataL2g0010101040[:,][:,5*0+4]

dataL2g0010101050 = np.genfromtxt('./L2/gK005/aK010/S1/N050/HamVals.txt')

MomentumAxL2g0010101050 = dataL2g0010101050[:,][:,5*0+0]
KineticEneL2g0010101050 = dataL2g0010101050[:,][:,5*0+1]
SelfEnergyL2g0010101050 = dataL2g0010101050[:,][:,5*0+2]
EigenValReL2g0010101050 = dataL2g0010101050[:,][:,5*0+3]
EigenValImL2g0010101050 = dataL2g0010101050[:,][:,5*0+4]

dataL2g0010201010 = np.genfromtxt('./L2/gK005/aK020/S1/N010/HamVals.txt')

MomentumAxL2g0010201010 = dataL2g0010201010[:,][:,5*0+0]
KineticEneL2g0010201010 = dataL2g0010201010[:,][:,5*0+1]
SelfEnergyL2g0010201010 = dataL2g0010201010[:,][:,5*0+2]
EigenValReL2g0010201010 = dataL2g0010201010[:,][:,5*0+3]
EigenValImL2g0010201010 = dataL2g0010201010[:,][:,5*0+4]

dataL2g0010201020 = np.genfromtxt('./L2/gK005/aK020/S1/N020/HamVals.txt')

MomentumAxL2g0010201020 = dataL2g0010201020[:,][:,5*0+0]
KineticEneL2g0010201020 = dataL2g0010201020[:,][:,5*0+1]
SelfEnergyL2g0010201020 = dataL2g0010201020[:,][:,5*0+2]
EigenValReL2g0010201020 = dataL2g0010201020[:,][:,5*0+3]
EigenValImL2g0010201020 = dataL2g0010201020[:,][:,5*0+4]

dataL2g0010201030 = np.genfromtxt('./L2/gK005/aK020/S1/N030/HamVals.txt')

MomentumAxL2g0010201030 = dataL2g0010201030[:,][:,5*0+0]
KineticEneL2g0010201030 = dataL2g0010201030[:,][:,5*0+1]
SelfEnergyL2g0010201030 = dataL2g0010201030[:,][:,5*0+2]
EigenValReL2g0010201030 = dataL2g0010201030[:,][:,5*0+3]
EigenValImL2g0010201030 = dataL2g0010201030[:,][:,5*0+4]

dataL2g0010201040 = np.genfromtxt('./L2/gK005/aK020/S1/N040/HamVals.txt')

MomentumAxL2g0010201040 = dataL2g0010201040[:,][:,5*0+0]
KineticEneL2g0010201040 = dataL2g0010201040[:,][:,5*0+1]
SelfEnergyL2g0010201040 = dataL2g0010201040[:,][:,5*0+2]
EigenValReL2g0010201040 = dataL2g0010201040[:,][:,5*0+3]
EigenValImL2g0010201040 = dataL2g0010201040[:,][:,5*0+4]

dataL2g0010201050 = np.genfromtxt('./L2/gK005/aK020/S1/N050/HamVals.txt')

MomentumAxL2g0010201050 = dataL2g0010201050[:,][:,5*0+0]
KineticEneL2g0010201050 = dataL2g0010201050[:,][:,5*0+1]
SelfEnergyL2g0010201050 = dataL2g0010201050[:,][:,5*0+2]
EigenValReL2g0010201050 = dataL2g0010201050[:,][:,5*0+3]
EigenValImL2g0010201050 = dataL2g0010201050[:,][:,5*0+4]

MaxEigenValImL2g0051010 = np.zeros((4))
MaxEigenValImL2g0051020 = np.zeros((4))
MaxEigenValImL2g0051030 = np.zeros((4))
MaxEigenValImL2g0051040 = np.zeros((4))
MaxEigenValImL2g0051050 = np.zeros((4))
MaxEigenValImL2g0051Inf = np.zeros((4))

MaxEigenValImL2g0051010[0] = np.max(EigenValImL2g0010011010)
MaxEigenValImL2g0051010[1] = np.max(EigenValImL2g0010021010)
MaxEigenValImL2g0051010[2] = np.max(EigenValImL2g0010051010)
MaxEigenValImL2g0051010[3] = np.max(EigenValImL2g0010101010)
#MaxEigenValImL2g0051010[4] = np.max(EigenValImL2g0010201010)

MaxEigenValImL2g0051020[0] = np.max(EigenValImL2g0010011020)
MaxEigenValImL2g0051020[1] = np.max(EigenValImL2g0010021020)
MaxEigenValImL2g0051020[2] = np.max(EigenValImL2g0010051020)
MaxEigenValImL2g0051020[3] = np.max(EigenValImL2g0010101020)
#MaxEigenValImL2g0051020[4] = np.max(EigenValImL2g0010201020)

MaxEigenValImL2g0051030[0] = np.max(EigenValImL2g0010011030)
MaxEigenValImL2g0051030[1] = np.max(EigenValImL2g0010021030)
MaxEigenValImL2g0051030[2] = np.max(EigenValImL2g0010051030)
MaxEigenValImL2g0051030[3] = np.max(EigenValImL2g0010101030)
#MaxEigenValImL2g0051030[4] = np.max(EigenValImL2g0010201030)

MaxEigenValImL2g0051040[0] = np.max(EigenValImL2g0010011040)
MaxEigenValImL2g0051040[1] = np.max(EigenValImL2g0010021040)
MaxEigenValImL2g0051040[2] = np.max(EigenValImL2g0010051040)
MaxEigenValImL2g0051040[3] = np.max(EigenValImL2g0010101040)
#MaxEigenValImL2g0051040[4] = np.max(EigenValImL2g0010201040)

MaxEigenValImL2g0051050[0] = np.max(EigenValImL2g0010011050)
MaxEigenValImL2g0051050[1] = np.max(EigenValImL2g0010021050)
MaxEigenValImL2g0051050[2] = np.max(EigenValImL2g0010051050)
MaxEigenValImL2g0051050[3] = np.max(EigenValImL2g0010101050)
#MaxEigenValImL2g0051050[4] = np.max(EigenValImL2g0010201050)

MaxEigenValImL2g0051Inf[0] = np.polyfit(fiveSizes, [MaxEigenValImL2g0051010[0],MaxEigenValImL2g0051020[0],MaxEigenValImL2g0051030[0],MaxEigenValImL2g0051040[0],MaxEigenValImL2g0051050[0]], 1)[[1]]
MaxEigenValImL2g0051Inf[1] = np.polyfit(fiveSizes, [MaxEigenValImL2g0051010[1],MaxEigenValImL2g0051020[1],MaxEigenValImL2g0051030[1],MaxEigenValImL2g0051040[1],MaxEigenValImL2g0051050[1]], 1)[[1]]
MaxEigenValImL2g0051Inf[2] = np.polyfit(fiveSizes, [MaxEigenValImL2g0051010[2],MaxEigenValImL2g0051020[2],MaxEigenValImL2g0051030[2],MaxEigenValImL2g0051040[2],MaxEigenValImL2g0051050[2]], 1)[[1]]
MaxEigenValImL2g0051Inf[3] = np.polyfit(fiveSizes, [MaxEigenValImL2g0051010[3],MaxEigenValImL2g0051020[3],MaxEigenValImL2g0051030[3],MaxEigenValImL2g0051040[3],MaxEigenValImL2g0051050[3]], 1)[[1]]
#MaxEigenValImL2g0051Inf[4] = np.polyfit(fiveSizes, [MaxEigenValImL2g0051010[4],MaxEigenValImL2g0051020[4],MaxEigenValImL2g0051030[4],MaxEigenValImL2g0051040[4],MaxEigenValImL2g0051050[4]], 1)[[1]]

########################################################################

dataL2g0010011010 = np.genfromtxt('./L2/gK010/aK001/S1/N010/HamVals.txt')

MomentumAxL2g0010011010 = dataL2g0010011010[:,][:,5*0+0]
KineticEneL2g0010011010 = dataL2g0010011010[:,][:,5*0+1]
SelfEnergyL2g0010011010 = dataL2g0010011010[:,][:,5*0+2]
EigenValReL2g0010011010 = dataL2g0010011010[:,][:,5*0+3]
EigenValImL2g0010011010 = dataL2g0010011010[:,][:,5*0+4]

dataL2g0010011020 = np.genfromtxt('./L2/gK010/aK001/S1/N020/HamVals.txt')

MomentumAxL2g0010011020 = dataL2g0010011020[:,][:,5*0+0]
KineticEneL2g0010011020 = dataL2g0010011020[:,][:,5*0+1]
SelfEnergyL2g0010011020 = dataL2g0010011020[:,][:,5*0+2]
EigenValReL2g0010011020 = dataL2g0010011020[:,][:,5*0+3]
EigenValImL2g0010011020 = dataL2g0010011020[:,][:,5*0+4]

dataL2g0010011030 = np.genfromtxt('./L2/gK010/aK001/S1/N030/HamVals.txt')

MomentumAxL2g0010011030 = dataL2g0010011030[:,][:,5*0+0]
KineticEneL2g0010011030 = dataL2g0010011030[:,][:,5*0+1]
SelfEnergyL2g0010011030 = dataL2g0010011030[:,][:,5*0+2]
EigenValReL2g0010011030 = dataL2g0010011030[:,][:,5*0+3]
EigenValImL2g0010011030 = dataL2g0010011030[:,][:,5*0+4]

dataL2g0010011040 = np.genfromtxt('./L2/gK010/aK001/S1/N040/HamVals.txt')

MomentumAxL2g0010011040 = dataL2g0010011040[:,][:,5*0+0]
KineticEneL2g0010011040 = dataL2g0010011040[:,][:,5*0+1]
SelfEnergyL2g0010011040 = dataL2g0010011040[:,][:,5*0+2]
EigenValReL2g0010011040 = dataL2g0010011040[:,][:,5*0+3]
EigenValImL2g0010011040 = dataL2g0010011040[:,][:,5*0+4]

dataL2g0010011050 = np.genfromtxt('./L2/gK010/aK001/S1/N050/HamVals.txt')

MomentumAxL2g0010011050 = dataL2g0010011050[:,][:,5*0+0]
KineticEneL2g0010011050 = dataL2g0010011050[:,][:,5*0+1]
SelfEnergyL2g0010011050 = dataL2g0010011050[:,][:,5*0+2]
EigenValReL2g0010011050 = dataL2g0010011050[:,][:,5*0+3]
EigenValImL2g0010011050 = dataL2g0010011050[:,][:,5*0+4]

dataL2g0010021010 = np.genfromtxt('./L2/gK010/aK002/S1/N010/HamVals.txt')

MomentumAxL2g0010021010 = dataL2g0010021010[:,][:,5*0+0]
KineticEneL2g0010021010 = dataL2g0010021010[:,][:,5*0+1]
SelfEnergyL2g0010021010 = dataL2g0010021010[:,][:,5*0+2]
EigenValReL2g0010021010 = dataL2g0010021010[:,][:,5*0+3]
EigenValImL2g0010021010 = dataL2g0010021010[:,][:,5*0+4]

dataL2g0010021020 = np.genfromtxt('./L2/gK010/aK002/S1/N020/HamVals.txt')

MomentumAxL2g0010021020 = dataL2g0010021020[:,][:,5*0+0]
KineticEneL2g0010021020 = dataL2g0010021020[:,][:,5*0+1]
SelfEnergyL2g0010021020 = dataL2g0010021020[:,][:,5*0+2]
EigenValReL2g0010021020 = dataL2g0010021020[:,][:,5*0+3]
EigenValImL2g0010021020 = dataL2g0010021020[:,][:,5*0+4]

dataL2g0010021030 = np.genfromtxt('./L2/gK010/aK002/S1/N030/HamVals.txt')

MomentumAxL2g0010021030 = dataL2g0010021030[:,][:,5*0+0]
KineticEneL2g0010021030 = dataL2g0010021030[:,][:,5*0+1]
SelfEnergyL2g0010021030 = dataL2g0010021030[:,][:,5*0+2]
EigenValReL2g0010021030 = dataL2g0010021030[:,][:,5*0+3]
EigenValImL2g0010021030 = dataL2g0010021030[:,][:,5*0+4]

dataL2g0010021040 = np.genfromtxt('./L2/gK010/aK002/S1/N040/HamVals.txt')

MomentumAxL2g0010021040 = dataL2g0010021040[:,][:,5*0+0]
KineticEneL2g0010021040 = dataL2g0010021040[:,][:,5*0+1]
SelfEnergyL2g0010021040 = dataL2g0010021040[:,][:,5*0+2]
EigenValReL2g0010021040 = dataL2g0010021040[:,][:,5*0+3]
EigenValImL2g0010021040 = dataL2g0010021040[:,][:,5*0+4]

dataL2g0010021050 = np.genfromtxt('./L2/gK010/aK002/S1/N050/HamVals.txt')

MomentumAxL2g0010021050 = dataL2g0010021050[:,][:,5*0+0]
KineticEneL2g0010021050 = dataL2g0010021050[:,][:,5*0+1]
SelfEnergyL2g0010021050 = dataL2g0010021050[:,][:,5*0+2]
EigenValReL2g0010021050 = dataL2g0010021050[:,][:,5*0+3]
EigenValImL2g0010021050 = dataL2g0010021050[:,][:,5*0+4]

dataL2g0010051010 = np.genfromtxt('./L2/gK010/aK005/S1/N010/HamVals.txt')

MomentumAxL2g0010051010 = dataL2g0010051010[:,][:,5*0+0]
KineticEneL2g0010051010 = dataL2g0010051010[:,][:,5*0+1]
SelfEnergyL2g0010051010 = dataL2g0010051010[:,][:,5*0+2]
EigenValReL2g0010051010 = dataL2g0010051010[:,][:,5*0+3]
EigenValImL2g0010051010 = dataL2g0010051010[:,][:,5*0+4]

dataL2g0010051020 = np.genfromtxt('./L2/gK010/aK005/S1/N020/HamVals.txt')

MomentumAxL2g0010051020 = dataL2g0010051020[:,][:,5*0+0]
KineticEneL2g0010051020 = dataL2g0010051020[:,][:,5*0+1]
SelfEnergyL2g0010051020 = dataL2g0010051020[:,][:,5*0+2]
EigenValReL2g0010051020 = dataL2g0010051020[:,][:,5*0+3]
EigenValImL2g0010051020 = dataL2g0010051020[:,][:,5*0+4]

dataL2g0010051030 = np.genfromtxt('./L2/gK010/aK005/S1/N030/HamVals.txt')

MomentumAxL2g0010051030 = dataL2g0010051030[:,][:,5*0+0]
KineticEneL2g0010051030 = dataL2g0010051030[:,][:,5*0+1]
SelfEnergyL2g0010051030 = dataL2g0010051030[:,][:,5*0+2]
EigenValReL2g0010051030 = dataL2g0010051030[:,][:,5*0+3]
EigenValImL2g0010051030 = dataL2g0010051030[:,][:,5*0+4]

dataL2g0010051040 = np.genfromtxt('./L2/gK010/aK005/S1/N040/HamVals.txt')

MomentumAxL2g0010051040 = dataL2g0010051040[:,][:,5*0+0]
KineticEneL2g0010051040 = dataL2g0010051040[:,][:,5*0+1]
SelfEnergyL2g0010051040 = dataL2g0010051040[:,][:,5*0+2]
EigenValReL2g0010051040 = dataL2g0010051040[:,][:,5*0+3]
EigenValImL2g0010051040 = dataL2g0010051040[:,][:,5*0+4]

dataL2g0010051050 = np.genfromtxt('./L2/gK010/aK005/S1/N050/HamVals.txt')

MomentumAxL2g0010051050 = dataL2g0010051050[:,][:,5*0+0]
KineticEneL2g0010051050 = dataL2g0010051050[:,][:,5*0+1]
SelfEnergyL2g0010051050 = dataL2g0010051050[:,][:,5*0+2]
EigenValReL2g0010051050 = dataL2g0010051050[:,][:,5*0+3]
EigenValImL2g0010051050 = dataL2g0010051050[:,][:,5*0+4]

dataL2g0010101010 = np.genfromtxt('./L2/gK010/aK010/S1/N010/HamVals.txt')

MomentumAxL2g0010101010 = dataL2g0010101010[:,][:,5*0+0]
KineticEneL2g0010101010 = dataL2g0010101010[:,][:,5*0+1]
SelfEnergyL2g0010101010 = dataL2g0010101010[:,][:,5*0+2]
EigenValReL2g0010101010 = dataL2g0010101010[:,][:,5*0+3]
EigenValImL2g0010101010 = dataL2g0010101010[:,][:,5*0+4]

dataL2g0010101020 = np.genfromtxt('./L2/gK010/aK010/S1/N020/HamVals.txt')

MomentumAxL2g0010101020 = dataL2g0010101020[:,][:,5*0+0]
KineticEneL2g0010101020 = dataL2g0010101020[:,][:,5*0+1]
SelfEnergyL2g0010101020 = dataL2g0010101020[:,][:,5*0+2]
EigenValReL2g0010101020 = dataL2g0010101020[:,][:,5*0+3]
EigenValImL2g0010101020 = dataL2g0010101020[:,][:,5*0+4]

dataL2g0010101030 = np.genfromtxt('./L2/gK010/aK010/S1/N030/HamVals.txt')

MomentumAxL2g0010101030 = dataL2g0010101030[:,][:,5*0+0]
KineticEneL2g0010101030 = dataL2g0010101030[:,][:,5*0+1]
SelfEnergyL2g0010101030 = dataL2g0010101030[:,][:,5*0+2]
EigenValReL2g0010101030 = dataL2g0010101030[:,][:,5*0+3]
EigenValImL2g0010101030 = dataL2g0010101030[:,][:,5*0+4]

dataL2g0010101040 = np.genfromtxt('./L2/gK010/aK010/S1/N040/HamVals.txt')

MomentumAxL2g0010101040 = dataL2g0010101040[:,][:,5*0+0]
KineticEneL2g0010101040 = dataL2g0010101040[:,][:,5*0+1]
SelfEnergyL2g0010101040 = dataL2g0010101040[:,][:,5*0+2]
EigenValReL2g0010101040 = dataL2g0010101040[:,][:,5*0+3]
EigenValImL2g0010101040 = dataL2g0010101040[:,][:,5*0+4]

dataL2g0010101050 = np.genfromtxt('./L2/gK010/aK010/S1/N050/HamVals.txt')

MomentumAxL2g0010101050 = dataL2g0010101050[:,][:,5*0+0]
KineticEneL2g0010101050 = dataL2g0010101050[:,][:,5*0+1]
SelfEnergyL2g0010101050 = dataL2g0010101050[:,][:,5*0+2]
EigenValReL2g0010101050 = dataL2g0010101050[:,][:,5*0+3]
EigenValImL2g0010101050 = dataL2g0010101050[:,][:,5*0+4]

dataL2g0010201010 = np.genfromtxt('./L2/gK010/aK020/S1/N010/HamVals.txt')

MomentumAxL2g0010201010 = dataL2g0010201010[:,][:,5*0+0]
KineticEneL2g0010201010 = dataL2g0010201010[:,][:,5*0+1]
SelfEnergyL2g0010201010 = dataL2g0010201010[:,][:,5*0+2]
EigenValReL2g0010201010 = dataL2g0010201010[:,][:,5*0+3]
EigenValImL2g0010201010 = dataL2g0010201010[:,][:,5*0+4]

dataL2g0010201020 = np.genfromtxt('./L2/gK010/aK020/S1/N020/HamVals.txt')

MomentumAxL2g0010201020 = dataL2g0010201020[:,][:,5*0+0]
KineticEneL2g0010201020 = dataL2g0010201020[:,][:,5*0+1]
SelfEnergyL2g0010201020 = dataL2g0010201020[:,][:,5*0+2]
EigenValReL2g0010201020 = dataL2g0010201020[:,][:,5*0+3]
EigenValImL2g0010201020 = dataL2g0010201020[:,][:,5*0+4]

dataL2g0010201030 = np.genfromtxt('./L2/gK010/aK020/S1/N030/HamVals.txt')

MomentumAxL2g0010201030 = dataL2g0010201030[:,][:,5*0+0]
KineticEneL2g0010201030 = dataL2g0010201030[:,][:,5*0+1]
SelfEnergyL2g0010201030 = dataL2g0010201030[:,][:,5*0+2]
EigenValReL2g0010201030 = dataL2g0010201030[:,][:,5*0+3]
EigenValImL2g0010201030 = dataL2g0010201030[:,][:,5*0+4]

dataL2g0010201040 = np.genfromtxt('./L2/gK010/aK020/S1/N040/HamVals.txt')

MomentumAxL2g0010201040 = dataL2g0010201040[:,][:,5*0+0]
KineticEneL2g0010201040 = dataL2g0010201040[:,][:,5*0+1]
SelfEnergyL2g0010201040 = dataL2g0010201040[:,][:,5*0+2]
EigenValReL2g0010201040 = dataL2g0010201040[:,][:,5*0+3]
EigenValImL2g0010201040 = dataL2g0010201040[:,][:,5*0+4]

dataL2g0010201050 = np.genfromtxt('./L2/gK010/aK020/S1/N050/HamVals.txt')

MomentumAxL2g0010201050 = dataL2g0010201050[:,][:,5*0+0]
KineticEneL2g0010201050 = dataL2g0010201050[:,][:,5*0+1]
SelfEnergyL2g0010201050 = dataL2g0010201050[:,][:,5*0+2]
EigenValReL2g0010201050 = dataL2g0010201050[:,][:,5*0+3]
EigenValImL2g0010201050 = dataL2g0010201050[:,][:,5*0+4]

MaxEigenValImL2g0101010 = np.zeros((4))
MaxEigenValImL2g0101020 = np.zeros((4))
MaxEigenValImL2g0101030 = np.zeros((4))
MaxEigenValImL2g0101040 = np.zeros((4))
MaxEigenValImL2g0101050 = np.zeros((4))
MaxEigenValImL2g0101Inf = np.zeros((4))

MaxEigenValImL2g0101010[0] = np.max(EigenValImL2g0010011010)
MaxEigenValImL2g0101010[1] = np.max(EigenValImL2g0010021010)
MaxEigenValImL2g0101010[2] = np.max(EigenValImL2g0010051010)
MaxEigenValImL2g0101010[3] = np.max(EigenValImL2g0010101010)
#MaxEigenValImL2g0101010[4] = np.max(EigenValImL2g0010201010)

MaxEigenValImL2g0101020[0] = np.max(EigenValImL2g0010011020)
MaxEigenValImL2g0101020[1] = np.max(EigenValImL2g0010021020)
MaxEigenValImL2g0101020[2] = np.max(EigenValImL2g0010051020)
MaxEigenValImL2g0101020[3] = np.max(EigenValImL2g0010101020)
#MaxEigenValImL2g0101020[4] = np.max(EigenValImL2g0010201020)

MaxEigenValImL2g0101030[0] = np.max(EigenValImL2g0010011030)
MaxEigenValImL2g0101030[1] = np.max(EigenValImL2g0010021030)
MaxEigenValImL2g0101030[2] = np.max(EigenValImL2g0010051030)
MaxEigenValImL2g0101030[3] = np.max(EigenValImL2g0010101030)
#MaxEigenValImL2g0101030[4] = np.max(EigenValImL2g0010201030)

MaxEigenValImL2g0101040[0] = np.max(EigenValImL2g0010011040)
MaxEigenValImL2g0101040[1] = np.max(EigenValImL2g0010021040)
MaxEigenValImL2g0101040[2] = np.max(EigenValImL2g0010051040)
MaxEigenValImL2g0101040[3] = np.max(EigenValImL2g0010101040)
#MaxEigenValImL2g0101040[4] = np.max(EigenValImL2g0010201040)

MaxEigenValImL2g0101050[0] = np.max(EigenValImL2g0010011050)
MaxEigenValImL2g0101050[1] = np.max(EigenValImL2g0010021050)
MaxEigenValImL2g0101050[2] = np.max(EigenValImL2g0010051050)
MaxEigenValImL2g0101050[3] = np.max(EigenValImL2g0010101050)
#MaxEigenValImL2g0101050[4] = np.max(EigenValImL2g0010201050)

MaxEigenValImL2g0101Inf[0] = np.polyfit(fiveSizes, [MaxEigenValImL2g0101010[0],MaxEigenValImL2g0101020[0],MaxEigenValImL2g0101030[0],MaxEigenValImL2g0101040[0],MaxEigenValImL2g0101050[0]], 1)[[1]]
MaxEigenValImL2g0101Inf[1] = np.polyfit(fiveSizes, [MaxEigenValImL2g0101010[1],MaxEigenValImL2g0101020[1],MaxEigenValImL2g0101030[1],MaxEigenValImL2g0101040[1],MaxEigenValImL2g0101050[1]], 1)[[1]]
MaxEigenValImL2g0101Inf[2] = np.polyfit(fiveSizes, [MaxEigenValImL2g0101010[2],MaxEigenValImL2g0101020[2],MaxEigenValImL2g0101030[2],MaxEigenValImL2g0101040[2],MaxEigenValImL2g0101050[2]], 1)[[1]]
MaxEigenValImL2g0101Inf[3] = np.polyfit(fiveSizes, [MaxEigenValImL2g0101010[3],MaxEigenValImL2g0101020[3],MaxEigenValImL2g0101030[3],MaxEigenValImL2g0101040[3],MaxEigenValImL2g0101050[3]], 1)[[1]]
#MaxEigenValImL2g0101Inf[4] = np.polyfit(fiveSizes, [MaxEigenValImL2g0101010[4],MaxEigenValImL2g0101020[4],MaxEigenValImL2g0101030[4],MaxEigenValImL2g0101040[4],MaxEigenValImL2g0101050[4]], 1)[[1]]

########################################################################
########################################################################

Spreading = np.zeros((4))
Spreading[0] = 0.01
Spreading[1] = 0.02
Spreading[2] = 0.05
Spreading[3] = 0.10

Coupling = np.zeros((4))
Coupling[0] = 0.01
Coupling[1] = 0.02
Coupling[2] = 0.05
Coupling[3] = 0.10

########################################################################
########################################################################

plt.clf()
fig, axs = plt.subplots(1, 2, figsize=(6, 3), sharey=True)
plt.subplots_adjust(left=0.2,bottom=0.2,right=0.85,top=0.8,wspace=0.1,hspace=0.4)

axs[0].semilogy(100*Coupling,[MaxEigenValImL0g0011Inf[0],MaxEigenValImL0g0021Inf[0],MaxEigenValImL0g0051Inf[0],MaxEigenValImL0g0101Inf[0]], marker='o',c=[1.0, 0.0, 0.0],ls='None',label='$a_{\\mathcal{K}}=  1$', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])#,label='100')
axs[0].semilogy(100*Coupling,[MaxEigenValImL0g0011Inf[1],MaxEigenValImL0g0021Inf[1],MaxEigenValImL0g0051Inf[1],MaxEigenValImL0g0101Inf[1]], marker='o',c=[1.0, 0.5, 0.0],ls='None',label='$a_{\\mathcal{K}}=  2$', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])#,label='100')
axs[0].semilogy(100*Coupling,[MaxEigenValImL0g0011Inf[2],MaxEigenValImL0g0021Inf[2],MaxEigenValImL0g0051Inf[2],MaxEigenValImL0g0101Inf[2]], marker='o',c=[0.0, 1.0, 0.0],ls='None',label='$a_{\\mathcal{K}}=  5$', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])#,label='100')
axs[0].semilogy(100*Coupling,[MaxEigenValImL0g0011Inf[3],MaxEigenValImL0g0021Inf[3],MaxEigenValImL0g0051Inf[3],MaxEigenValImL0g0101Inf[3]], marker='o',c=[0.0, 0.0, 1.0],ls='None',label='$a_{\\mathcal{K}}= 10$', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])#,label='100')

#axs[0].semilogy(100*Spreading,MaxEigenValImL0g0011Inf, marker='o',c=[1.0, 0.0, 0.0],ls='None',label='$a_{\\mathcal{K}}= 0.01$', markersize=4, linewidth=1)#,label='100')
#axs[0].semilogy(100*Spreading,MaxEigenValImL0g0021Inf, marker='o',c=[1.0, 0.5, 0.0],ls='None',label='$a_{\\mathcal{K}}= 0.02$', markersize=4, linewidth=1)#,label='100')
#axs[0].semilogy(100*Spreading,MaxEigenValImL0g0051Inf, marker='o',c=[0.0, 1.0, 0.0],ls='None',label='$a_{\\mathcal{K}}= 0.05$', markersize=4, linewidth=1)#,label='100')
#axs[0].semilogy(100*Spreading,MaxEigenValImL0g0101Inf, marker='o',c=[0.0, 0.0, 1.0],ls='None',label='$a_{\\mathcal{K}}= 0.10$', markersize=4, linewidth=1)#,label='100')

print MaxEigenValImL2g0011Inf
print MaxEigenValImL2g0021Inf
print MaxEigenValImL2g0051Inf
print MaxEigenValImL2g0101Inf

#plt.xlim(left  =0)
#plt.ylim(top=0.09,bottom=0)
#plt.xticks([0.01,0.02,0.05,0.10])
#plt.yticks(np.arange(0.984,+1.004, step=0.002))
#plt.show()

axs[0].set_title("$\\ell=0$" ,fontsize=12, fontname='Times New Roman')

axs[0].grid(True)
axs[0].set_xlim(+0.0e+1,+1.2e+1)
axs[0].set_xticks(np.arange(-0.0e+1,+1.21e+1, step=2.e-0))
axs[0].set_ylim(+1e-4,+1.0e-1)
#axs[0].set_yticks(np.arange(-0.e-2,+10.1e-0, step=1.0e-0))

axs[0].legend(bbox_to_anchor=(0.2, +1.3), loc=2, borderaxespad=0., ncol=4, labelspacing=1,handleheight=1, columnspacing=0.1, handletextpad=0.1)
#plt.suptitle('$\\ell=0XXX, g_{\\mathcal{K}}=0.1$', fontsize=20, fontname='Times New Roman')
axs[0].set_xlabel('$g_{\\mathcal{K}}\\times 10^{+2}$', fontsize=12, fontname='Times New Roman')
axs[0].set_ylabel('Max{Im[E]/$E_{\\mathrm{UV}}$}', fontsize=12, fontname='Times New Roman')

axs[1].semilogy(100*Coupling,[MaxEigenValImL2g0011Inf[0],MaxEigenValImL2g0021Inf[0],MaxEigenValImL2g0051Inf[0],MaxEigenValImL2g0101Inf[0]], marker='o',c=[1.0, 0.0, 0.0],ls='None',label='$a_{\\mathcal{K}}= 0.01$', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
axs[1].semilogy(100*Coupling,[MaxEigenValImL2g0011Inf[1],MaxEigenValImL2g0021Inf[1],MaxEigenValImL2g0051Inf[1],MaxEigenValImL2g0101Inf[1]], marker='o',c=[1.0, 0.5, 0.0],ls='None',label='$a_{\\mathcal{K}}= 0.02$', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
axs[1].semilogy(100*Coupling,[MaxEigenValImL2g0011Inf[2],MaxEigenValImL2g0021Inf[2],MaxEigenValImL2g0051Inf[2],MaxEigenValImL2g0101Inf[2]], marker='o',c=[0.0, 1.0, 0.0],ls='None',label='$a_{\\mathcal{K}}= 0.05$', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
axs[1].semilogy(100*Coupling,[MaxEigenValImL2g0011Inf[3],MaxEigenValImL2g0021Inf[3],MaxEigenValImL2g0051Inf[3],MaxEigenValImL2g0101Inf[3]], marker='o',c=[0.0, 0.0, 1.0],ls='None',label='$a_{\\mathcal{K}}= 0.10$', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])

#axs[1].semilogy(100*Coupling,MaxEigenValImL2g0011Inf, marker='o',c=[1.0, 0.0, 0.0],ls='None',label='$a_{\\mathcal{K}}= 0.01$', markersize=4, linewidth=1)#,label='100')
#axs[1].semilogy(100*Coupling,MaxEigenValImL2g0021Inf, marker='o',c=[1.0, 0.5, 0.0],ls='None',label='$a_{\\mathcal{K}}= 0.02$', markersize=4, linewidth=1)#,label='100')
#axs[1].semilogy(100*Coupling,MaxEigenValImL2g0051Inf, marker='o',c=[0.0, 1.0, 0.0],ls='None',label='$a_{\\mathcal{K}}= 0.05$', markersize=4, linewidth=1)#,label='100')
#axs[1].semilogy(100*Coupling,MaxEigenValImL2g0101Inf, marker='o',c=[0.0, 0.0, 1.0],ls='None',label='$a_{\\mathcal{K}}= 0.10$', markersize=4, linewidth=1)#,label='100')

axs[1].set_title("$\\ell=2$" ,fontsize=12, fontname='Times New Roman')

axs[1].grid(True)
axs[1].set_xlim(+0.0e+1,+1.2e+1)
axs[1].set_xticks(np.arange(-0.0e+1,+1.21e+1, step=2.e-0))
#axs[1].set_ylim(+1e-2,+5.0e0)
#axs[1].set_yticks(np.arange(-0.e-2,+9.1e-0, step=1.0e-0))

axs[0].text(-0.6, 0.00002, '(a)', fontsize=12)
axs[1].text(-0.6, 0.00002, '(b)', fontsize=12)

#axs[1,0].legend(bbox_to_anchor=(0.4, +1.2), loc=2, borderaxespad=0., ncol=4, labelspacing=1,handleheight=1, columnspacing=0.1, handletextpad=0.1)
#plt.suptitle('$\\ell=0XXX, g_{\\mathcal{K}}=0.1$', fontsize=20, fontname='Times New Roman')
axs[1].set_xlabel('$g_{\\mathcal{K}}\\times 10^{+2}$', fontsize=12, fontname='Times New Roman')
#axs[1].set_ylabel('Max{Im[E]}$\\times 10^{+2}$', fontsize=12, fontname='Times New Roman')




#plt.show()
fig.savefig('PlotReport.pdf')

