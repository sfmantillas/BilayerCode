import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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

MaxEigenValImL0g0011010 = np.zeros((5))
MaxEigenValImL0g0011020 = np.zeros((5))
MaxEigenValImL0g0011030 = np.zeros((5))
MaxEigenValImL0g0011040 = np.zeros((5))
MaxEigenValImL0g0011050 = np.zeros((5))
MaxEigenValImL0g0011Inf = np.zeros((5))

MaxEigenValImL0g0011010[0] = np.max(EigenValImL0g0010011010)
MaxEigenValImL0g0011010[1] = np.max(EigenValImL0g0010021010)
MaxEigenValImL0g0011010[2] = np.max(EigenValImL0g0010051010)
MaxEigenValImL0g0011010[3] = np.max(EigenValImL0g0010101010)
MaxEigenValImL0g0011010[4] = np.max(EigenValImL0g0010201010)

MaxEigenValImL0g0011020[0] = np.max(EigenValImL0g0010011020)
MaxEigenValImL0g0011020[1] = np.max(EigenValImL0g0010021020)
MaxEigenValImL0g0011020[2] = np.max(EigenValImL0g0010051020)
MaxEigenValImL0g0011020[3] = np.max(EigenValImL0g0010101020)
MaxEigenValImL0g0011020[4] = np.max(EigenValImL0g0010201020)

MaxEigenValImL0g0011030[0] = np.max(EigenValImL0g0010011030)
MaxEigenValImL0g0011030[1] = np.max(EigenValImL0g0010021030)
MaxEigenValImL0g0011030[2] = np.max(EigenValImL0g0010051030)
MaxEigenValImL0g0011030[3] = np.max(EigenValImL0g0010101030)
MaxEigenValImL0g0011030[4] = np.max(EigenValImL0g0010201030)

MaxEigenValImL0g0011040[0] = np.max(EigenValImL0g0010011040)
MaxEigenValImL0g0011040[1] = np.max(EigenValImL0g0010021040)
MaxEigenValImL0g0011040[2] = np.max(EigenValImL0g0010051040)
MaxEigenValImL0g0011040[3] = np.max(EigenValImL0g0010101040)
MaxEigenValImL0g0011040[4] = np.max(EigenValImL0g0010201040)

MaxEigenValImL0g0011050[0] = np.max(EigenValImL0g0010011050)
MaxEigenValImL0g0011050[1] = np.max(EigenValImL0g0010021050)
MaxEigenValImL0g0011050[2] = np.max(EigenValImL0g0010051050)
MaxEigenValImL0g0011050[3] = np.max(EigenValImL0g0010101050)
MaxEigenValImL0g0011050[4] = np.max(EigenValImL0g0010201050)

MaxEigenValImL0g0011Inf[0] = np.polyfit(fiveSizes, [MaxEigenValImL0g0011010[0],MaxEigenValImL0g0011020[0],MaxEigenValImL0g0011030[0],MaxEigenValImL0g0011040[0],MaxEigenValImL0g0011050[0]], 1)[[1]]
MaxEigenValImL0g0011Inf[1] = np.polyfit(fiveSizes, [MaxEigenValImL0g0011010[1],MaxEigenValImL0g0011020[1],MaxEigenValImL0g0011030[1],MaxEigenValImL0g0011040[1],MaxEigenValImL0g0011050[1]], 1)[[1]]
MaxEigenValImL0g0011Inf[2] = np.polyfit(fiveSizes, [MaxEigenValImL0g0011010[2],MaxEigenValImL0g0011020[2],MaxEigenValImL0g0011030[2],MaxEigenValImL0g0011040[2],MaxEigenValImL0g0011050[2]], 1)[[1]]
MaxEigenValImL0g0011Inf[3] = np.polyfit(fiveSizes, [MaxEigenValImL0g0011010[3],MaxEigenValImL0g0011020[3],MaxEigenValImL0g0011030[3],MaxEigenValImL0g0011040[3],MaxEigenValImL0g0011050[3]], 1)[[1]]
MaxEigenValImL0g0011Inf[4] = np.polyfit(fiveSizes, [MaxEigenValImL0g0011010[4],MaxEigenValImL0g0011020[4],MaxEigenValImL0g0011030[4],MaxEigenValImL0g0011040[4],MaxEigenValImL0g0011050[4]], 1)[[1]]

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

MaxEigenValImL0g0021010 = np.zeros((5))
MaxEigenValImL0g0021020 = np.zeros((5))
MaxEigenValImL0g0021030 = np.zeros((5))
MaxEigenValImL0g0021040 = np.zeros((5))
MaxEigenValImL0g0021050 = np.zeros((5))
MaxEigenValImL0g0021Inf = np.zeros((5))

MaxEigenValImL0g0021010[0] = np.max(EigenValImL0g0010011010)
MaxEigenValImL0g0021010[1] = np.max(EigenValImL0g0010021010)
MaxEigenValImL0g0021010[2] = np.max(EigenValImL0g0010051010)
MaxEigenValImL0g0021010[3] = np.max(EigenValImL0g0010101010)
MaxEigenValImL0g0021010[4] = np.max(EigenValImL0g0010201010)

MaxEigenValImL0g0021020[0] = np.max(EigenValImL0g0010011020)
MaxEigenValImL0g0021020[1] = np.max(EigenValImL0g0010021020)
MaxEigenValImL0g0021020[2] = np.max(EigenValImL0g0010051020)
MaxEigenValImL0g0021020[3] = np.max(EigenValImL0g0010101020)
MaxEigenValImL0g0021020[4] = np.max(EigenValImL0g0010201020)

MaxEigenValImL0g0021030[0] = np.max(EigenValImL0g0010011030)
MaxEigenValImL0g0021030[1] = np.max(EigenValImL0g0010021030)
MaxEigenValImL0g0021030[2] = np.max(EigenValImL0g0010051030)
MaxEigenValImL0g0021030[3] = np.max(EigenValImL0g0010101030)
MaxEigenValImL0g0021030[4] = np.max(EigenValImL0g0010201030)

MaxEigenValImL0g0021040[0] = np.max(EigenValImL0g0010011040)
MaxEigenValImL0g0021040[1] = np.max(EigenValImL0g0010021040)
MaxEigenValImL0g0021040[2] = np.max(EigenValImL0g0010051040)
MaxEigenValImL0g0021040[3] = np.max(EigenValImL0g0010101040)
MaxEigenValImL0g0021040[4] = np.max(EigenValImL0g0010201040)

MaxEigenValImL0g0021050[0] = np.max(EigenValImL0g0010011050)
MaxEigenValImL0g0021050[1] = np.max(EigenValImL0g0010021050)
MaxEigenValImL0g0021050[2] = np.max(EigenValImL0g0010051050)
MaxEigenValImL0g0021050[3] = np.max(EigenValImL0g0010101050)
MaxEigenValImL0g0021050[4] = np.max(EigenValImL0g0010201050)

MaxEigenValImL0g0021Inf[0] = np.polyfit(fiveSizes, [MaxEigenValImL0g0021010[0],MaxEigenValImL0g0021020[0],MaxEigenValImL0g0021030[0],MaxEigenValImL0g0021040[0],MaxEigenValImL0g0021050[0]], 1)[[1]]
MaxEigenValImL0g0021Inf[1] = np.polyfit(fiveSizes, [MaxEigenValImL0g0021010[1],MaxEigenValImL0g0021020[1],MaxEigenValImL0g0021030[1],MaxEigenValImL0g0021040[1],MaxEigenValImL0g0021050[1]], 1)[[1]]
MaxEigenValImL0g0021Inf[2] = np.polyfit(fiveSizes, [MaxEigenValImL0g0021010[2],MaxEigenValImL0g0021020[2],MaxEigenValImL0g0021030[2],MaxEigenValImL0g0021040[2],MaxEigenValImL0g0021050[2]], 1)[[1]]
MaxEigenValImL0g0021Inf[3] = np.polyfit(fiveSizes, [MaxEigenValImL0g0021010[3],MaxEigenValImL0g0021020[3],MaxEigenValImL0g0021030[3],MaxEigenValImL0g0021040[3],MaxEigenValImL0g0021050[3]], 1)[[1]]
MaxEigenValImL0g0021Inf[4] = np.polyfit(fiveSizes, [MaxEigenValImL0g0021010[4],MaxEigenValImL0g0021020[4],MaxEigenValImL0g0021030[4],MaxEigenValImL0g0021040[4],MaxEigenValImL0g0021050[4]], 1)[[1]]

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

MaxEigenValImL0g0051010 = np.zeros((5))
MaxEigenValImL0g0051020 = np.zeros((5))
MaxEigenValImL0g0051030 = np.zeros((5))
MaxEigenValImL0g0051040 = np.zeros((5))
MaxEigenValImL0g0051050 = np.zeros((5))
MaxEigenValImL0g0051Inf = np.zeros((5))

MaxEigenValImL0g0051010[0] = np.max(EigenValImL0g0010011010)
MaxEigenValImL0g0051010[1] = np.max(EigenValImL0g0010021010)
MaxEigenValImL0g0051010[2] = np.max(EigenValImL0g0010051010)
MaxEigenValImL0g0051010[3] = np.max(EigenValImL0g0010101010)
MaxEigenValImL0g0051010[4] = np.max(EigenValImL0g0010201010)

MaxEigenValImL0g0051020[0] = np.max(EigenValImL0g0010011020)
MaxEigenValImL0g0051020[1] = np.max(EigenValImL0g0010021020)
MaxEigenValImL0g0051020[2] = np.max(EigenValImL0g0010051020)
MaxEigenValImL0g0051020[3] = np.max(EigenValImL0g0010101020)
MaxEigenValImL0g0051020[4] = np.max(EigenValImL0g0010201020)

MaxEigenValImL0g0051030[0] = np.max(EigenValImL0g0010011030)
MaxEigenValImL0g0051030[1] = np.max(EigenValImL0g0010021030)
MaxEigenValImL0g0051030[2] = np.max(EigenValImL0g0010051030)
MaxEigenValImL0g0051030[3] = np.max(EigenValImL0g0010101030)
MaxEigenValImL0g0051030[4] = np.max(EigenValImL0g0010201030)

MaxEigenValImL0g0051040[0] = np.max(EigenValImL0g0010011040)
MaxEigenValImL0g0051040[1] = np.max(EigenValImL0g0010021040)
MaxEigenValImL0g0051040[2] = np.max(EigenValImL0g0010051040)
MaxEigenValImL0g0051040[3] = np.max(EigenValImL0g0010101040)
MaxEigenValImL0g0051040[4] = np.max(EigenValImL0g0010201040)

MaxEigenValImL0g0051050[0] = np.max(EigenValImL0g0010011050)
MaxEigenValImL0g0051050[1] = np.max(EigenValImL0g0010021050)
MaxEigenValImL0g0051050[2] = np.max(EigenValImL0g0010051050)
MaxEigenValImL0g0051050[3] = np.max(EigenValImL0g0010101050)
MaxEigenValImL0g0051050[4] = np.max(EigenValImL0g0010201050)

MaxEigenValImL0g0051Inf[0] = np.polyfit(fiveSizes, [MaxEigenValImL0g0051010[0],MaxEigenValImL0g0051020[0],MaxEigenValImL0g0051030[0],MaxEigenValImL0g0051040[0],MaxEigenValImL0g0051050[0]], 1)[[1]]
MaxEigenValImL0g0051Inf[1] = np.polyfit(fiveSizes, [MaxEigenValImL0g0051010[1],MaxEigenValImL0g0051020[1],MaxEigenValImL0g0051030[1],MaxEigenValImL0g0051040[1],MaxEigenValImL0g0051050[1]], 1)[[1]]
MaxEigenValImL0g0051Inf[2] = np.polyfit(fiveSizes, [MaxEigenValImL0g0051010[2],MaxEigenValImL0g0051020[2],MaxEigenValImL0g0051030[2],MaxEigenValImL0g0051040[2],MaxEigenValImL0g0051050[2]], 1)[[1]]
MaxEigenValImL0g0051Inf[3] = np.polyfit(fiveSizes, [MaxEigenValImL0g0051010[3],MaxEigenValImL0g0051020[3],MaxEigenValImL0g0051030[3],MaxEigenValImL0g0051040[3],MaxEigenValImL0g0051050[3]], 1)[[1]]
MaxEigenValImL0g0051Inf[4] = np.polyfit(fiveSizes, [MaxEigenValImL0g0051010[4],MaxEigenValImL0g0051020[4],MaxEigenValImL0g0051030[4],MaxEigenValImL0g0051040[4],MaxEigenValImL0g0051050[4]], 1)[[1]]

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

MaxEigenValImL0g0101010 = np.zeros((5))
MaxEigenValImL0g0101020 = np.zeros((5))
MaxEigenValImL0g0101030 = np.zeros((5))
MaxEigenValImL0g0101040 = np.zeros((5))
MaxEigenValImL0g0101050 = np.zeros((5))
MaxEigenValImL0g0101Inf = np.zeros((5))

MaxEigenValImL0g0101010[0] = np.max(EigenValImL0g0010011010)
MaxEigenValImL0g0101010[1] = np.max(EigenValImL0g0010021010)
MaxEigenValImL0g0101010[2] = np.max(EigenValImL0g0010051010)
MaxEigenValImL0g0101010[3] = np.max(EigenValImL0g0010101010)
MaxEigenValImL0g0101010[4] = np.max(EigenValImL0g0010201010)

MaxEigenValImL0g0101020[0] = np.max(EigenValImL0g0010011020)
MaxEigenValImL0g0101020[1] = np.max(EigenValImL0g0010021020)
MaxEigenValImL0g0101020[2] = np.max(EigenValImL0g0010051020)
MaxEigenValImL0g0101020[3] = np.max(EigenValImL0g0010101020)
MaxEigenValImL0g0101020[4] = np.max(EigenValImL0g0010201020)

MaxEigenValImL0g0101030[0] = np.max(EigenValImL0g0010011030)
MaxEigenValImL0g0101030[1] = np.max(EigenValImL0g0010021030)
MaxEigenValImL0g0101030[2] = np.max(EigenValImL0g0010051030)
MaxEigenValImL0g0101030[3] = np.max(EigenValImL0g0010101030)
MaxEigenValImL0g0101030[4] = np.max(EigenValImL0g0010201030)

MaxEigenValImL0g0101040[0] = np.max(EigenValImL0g0010011040)
MaxEigenValImL0g0101040[1] = np.max(EigenValImL0g0010021040)
MaxEigenValImL0g0101040[2] = np.max(EigenValImL0g0010051040)
MaxEigenValImL0g0101040[3] = np.max(EigenValImL0g0010101040)
MaxEigenValImL0g0101040[4] = np.max(EigenValImL0g0010201040)

MaxEigenValImL0g0101050[0] = np.max(EigenValImL0g0010011050)
MaxEigenValImL0g0101050[1] = np.max(EigenValImL0g0010021050)
MaxEigenValImL0g0101050[2] = np.max(EigenValImL0g0010051050)
MaxEigenValImL0g0101050[3] = np.max(EigenValImL0g0010101050)
MaxEigenValImL0g0101050[4] = np.max(EigenValImL0g0010201050)

MaxEigenValImL0g0101Inf[0] = np.polyfit(fiveSizes, [MaxEigenValImL0g0101010[0],MaxEigenValImL0g0101020[0],MaxEigenValImL0g0101030[0],MaxEigenValImL0g0101040[0],MaxEigenValImL0g0101050[0]], 1)[[1]]
MaxEigenValImL0g0101Inf[1] = np.polyfit(fiveSizes, [MaxEigenValImL0g0101010[1],MaxEigenValImL0g0101020[1],MaxEigenValImL0g0101030[1],MaxEigenValImL0g0101040[1],MaxEigenValImL0g0101050[1]], 1)[[1]]
MaxEigenValImL0g0101Inf[2] = np.polyfit(fiveSizes, [MaxEigenValImL0g0101010[2],MaxEigenValImL0g0101020[2],MaxEigenValImL0g0101030[2],MaxEigenValImL0g0101040[2],MaxEigenValImL0g0101050[2]], 1)[[1]]
MaxEigenValImL0g0101Inf[3] = np.polyfit(fiveSizes, [MaxEigenValImL0g0101010[3],MaxEigenValImL0g0101020[3],MaxEigenValImL0g0101030[3],MaxEigenValImL0g0101040[3],MaxEigenValImL0g0101050[3]], 1)[[1]]
MaxEigenValImL0g0101Inf[4] = np.polyfit(fiveSizes, [MaxEigenValImL0g0101010[4],MaxEigenValImL0g0101020[4],MaxEigenValImL0g0101030[4],MaxEigenValImL0g0101040[4],MaxEigenValImL0g0101050[4]], 1)[[1]]

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

MaxEigenValImL2g0011010 = np.zeros((5))
MaxEigenValImL2g0011020 = np.zeros((5))
MaxEigenValImL2g0011030 = np.zeros((5))
MaxEigenValImL2g0011040 = np.zeros((5))
MaxEigenValImL2g0011050 = np.zeros((5))
MaxEigenValImL2g0011Inf = np.zeros((5))

MaxEigenValImL2g0011010[0] = np.max(EigenValImL2g0010011010)
MaxEigenValImL2g0011010[1] = np.max(EigenValImL2g0010021010)
MaxEigenValImL2g0011010[2] = np.max(EigenValImL2g0010051010)
MaxEigenValImL2g0011010[3] = np.max(EigenValImL2g0010101010)
MaxEigenValImL2g0011010[4] = np.max(EigenValImL2g0010201010)

MaxEigenValImL2g0011020[0] = np.max(EigenValImL2g0010011020)
MaxEigenValImL2g0011020[1] = np.max(EigenValImL2g0010021020)
MaxEigenValImL2g0011020[2] = np.max(EigenValImL2g0010051020)
MaxEigenValImL2g0011020[3] = np.max(EigenValImL2g0010101020)
MaxEigenValImL2g0011020[4] = np.max(EigenValImL2g0010201020)

MaxEigenValImL2g0011030[0] = np.max(EigenValImL2g0010011030)
MaxEigenValImL2g0011030[1] = np.max(EigenValImL2g0010021030)
MaxEigenValImL2g0011030[2] = np.max(EigenValImL2g0010051030)
MaxEigenValImL2g0011030[3] = np.max(EigenValImL2g0010101030)
MaxEigenValImL2g0011030[4] = np.max(EigenValImL2g0010201030)

MaxEigenValImL2g0011040[0] = np.max(EigenValImL2g0010011040)
MaxEigenValImL2g0011040[1] = np.max(EigenValImL2g0010021040)
MaxEigenValImL2g0011040[2] = np.max(EigenValImL2g0010051040)
MaxEigenValImL2g0011040[3] = np.max(EigenValImL2g0010101040)
MaxEigenValImL2g0011040[4] = np.max(EigenValImL2g0010201040)

MaxEigenValImL2g0011050[0] = np.max(EigenValImL2g0010011050)
MaxEigenValImL2g0011050[1] = np.max(EigenValImL2g0010021050)
MaxEigenValImL2g0011050[2] = np.max(EigenValImL2g0010051050)
MaxEigenValImL2g0011050[3] = np.max(EigenValImL2g0010101050)
MaxEigenValImL2g0011050[4] = np.max(EigenValImL2g0010201050)

MaxEigenValImL2g0011Inf[0] = np.polyfit(fiveSizes, [MaxEigenValImL2g0011010[0],MaxEigenValImL2g0011020[0],MaxEigenValImL2g0011030[0],MaxEigenValImL2g0011040[0],MaxEigenValImL2g0011050[0]], 1)[[1]]
MaxEigenValImL2g0011Inf[1] = np.polyfit(fiveSizes, [MaxEigenValImL2g0011010[1],MaxEigenValImL2g0011020[1],MaxEigenValImL2g0011030[1],MaxEigenValImL2g0011040[1],MaxEigenValImL2g0011050[1]], 1)[[1]]
MaxEigenValImL2g0011Inf[2] = np.polyfit(fiveSizes, [MaxEigenValImL2g0011010[2],MaxEigenValImL2g0011020[2],MaxEigenValImL2g0011030[2],MaxEigenValImL2g0011040[2],MaxEigenValImL2g0011050[2]], 1)[[1]]
MaxEigenValImL2g0011Inf[3] = np.polyfit(fiveSizes, [MaxEigenValImL2g0011010[3],MaxEigenValImL2g0011020[3],MaxEigenValImL2g0011030[3],MaxEigenValImL2g0011040[3],MaxEigenValImL2g0011050[3]], 1)[[1]]
MaxEigenValImL2g0011Inf[4] = np.polyfit(fiveSizes, [MaxEigenValImL2g0011010[4],MaxEigenValImL2g0011020[4],MaxEigenValImL2g0011030[4],MaxEigenValImL2g0011040[4],MaxEigenValImL2g0011050[4]], 1)[[1]]

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

MaxEigenValImL2g0021010 = np.zeros((5))
MaxEigenValImL2g0021020 = np.zeros((5))
MaxEigenValImL2g0021030 = np.zeros((5))
MaxEigenValImL2g0021040 = np.zeros((5))
MaxEigenValImL2g0021050 = np.zeros((5))
MaxEigenValImL2g0021Inf = np.zeros((5))

MaxEigenValImL2g0021010[0] = np.max(EigenValImL2g0010011010)
MaxEigenValImL2g0021010[1] = np.max(EigenValImL2g0010021010)
MaxEigenValImL2g0021010[2] = np.max(EigenValImL2g0010051010)
MaxEigenValImL2g0021010[3] = np.max(EigenValImL2g0010101010)
MaxEigenValImL2g0021010[4] = np.max(EigenValImL2g0010201010)

MaxEigenValImL2g0021020[0] = np.max(EigenValImL2g0010011020)
MaxEigenValImL2g0021020[1] = np.max(EigenValImL2g0010021020)
MaxEigenValImL2g0021020[2] = np.max(EigenValImL2g0010051020)
MaxEigenValImL2g0021020[3] = np.max(EigenValImL2g0010101020)
MaxEigenValImL2g0021020[4] = np.max(EigenValImL2g0010201020)

MaxEigenValImL2g0021030[0] = np.max(EigenValImL2g0010011030)
MaxEigenValImL2g0021030[1] = np.max(EigenValImL2g0010021030)
MaxEigenValImL2g0021030[2] = np.max(EigenValImL2g0010051030)
MaxEigenValImL2g0021030[3] = np.max(EigenValImL2g0010101030)
MaxEigenValImL2g0021030[4] = np.max(EigenValImL2g0010201030)

MaxEigenValImL2g0021040[0] = np.max(EigenValImL2g0010011040)
MaxEigenValImL2g0021040[1] = np.max(EigenValImL2g0010021040)
MaxEigenValImL2g0021040[2] = np.max(EigenValImL2g0010051040)
MaxEigenValImL2g0021040[3] = np.max(EigenValImL2g0010101040)
MaxEigenValImL2g0021040[4] = np.max(EigenValImL2g0010201040)

MaxEigenValImL2g0021050[0] = np.max(EigenValImL2g0010011050)
MaxEigenValImL2g0021050[1] = np.max(EigenValImL2g0010021050)
MaxEigenValImL2g0021050[2] = np.max(EigenValImL2g0010051050)
MaxEigenValImL2g0021050[3] = np.max(EigenValImL2g0010101050)
MaxEigenValImL2g0021050[4] = np.max(EigenValImL2g0010201050)

MaxEigenValImL2g0021Inf[0] = np.polyfit(fiveSizes, [MaxEigenValImL2g0021010[0],MaxEigenValImL2g0021020[0],MaxEigenValImL2g0021030[0],MaxEigenValImL2g0021040[0],MaxEigenValImL2g0021050[0]], 1)[[1]]
MaxEigenValImL2g0021Inf[1] = np.polyfit(fiveSizes, [MaxEigenValImL2g0021010[1],MaxEigenValImL2g0021020[1],MaxEigenValImL2g0021030[1],MaxEigenValImL2g0021040[1],MaxEigenValImL2g0021050[1]], 1)[[1]]
MaxEigenValImL2g0021Inf[2] = np.polyfit(fiveSizes, [MaxEigenValImL2g0021010[2],MaxEigenValImL2g0021020[2],MaxEigenValImL2g0021030[2],MaxEigenValImL2g0021040[2],MaxEigenValImL2g0021050[2]], 1)[[1]]
MaxEigenValImL2g0021Inf[3] = np.polyfit(fiveSizes, [MaxEigenValImL2g0021010[3],MaxEigenValImL2g0021020[3],MaxEigenValImL2g0021030[3],MaxEigenValImL2g0021040[3],MaxEigenValImL2g0021050[3]], 1)[[1]]
MaxEigenValImL2g0021Inf[4] = np.polyfit(fiveSizes, [MaxEigenValImL2g0021010[4],MaxEigenValImL2g0021020[4],MaxEigenValImL2g0021030[4],MaxEigenValImL2g0021040[4],MaxEigenValImL2g0021050[4]], 1)[[1]]

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

MaxEigenValImL2g0051010 = np.zeros((5))
MaxEigenValImL2g0051020 = np.zeros((5))
MaxEigenValImL2g0051030 = np.zeros((5))
MaxEigenValImL2g0051040 = np.zeros((5))
MaxEigenValImL2g0051050 = np.zeros((5))
MaxEigenValImL2g0051Inf = np.zeros((5))

MaxEigenValImL2g0051010[0] = np.max(EigenValImL2g0010011010)
MaxEigenValImL2g0051010[1] = np.max(EigenValImL2g0010021010)
MaxEigenValImL2g0051010[2] = np.max(EigenValImL2g0010051010)
MaxEigenValImL2g0051010[3] = np.max(EigenValImL2g0010101010)
MaxEigenValImL2g0051010[4] = np.max(EigenValImL2g0010201010)

MaxEigenValImL2g0051020[0] = np.max(EigenValImL2g0010011020)
MaxEigenValImL2g0051020[1] = np.max(EigenValImL2g0010021020)
MaxEigenValImL2g0051020[2] = np.max(EigenValImL2g0010051020)
MaxEigenValImL2g0051020[3] = np.max(EigenValImL2g0010101020)
MaxEigenValImL2g0051020[4] = np.max(EigenValImL2g0010201020)

MaxEigenValImL2g0051030[0] = np.max(EigenValImL2g0010011030)
MaxEigenValImL2g0051030[1] = np.max(EigenValImL2g0010021030)
MaxEigenValImL2g0051030[2] = np.max(EigenValImL2g0010051030)
MaxEigenValImL2g0051030[3] = np.max(EigenValImL2g0010101030)
MaxEigenValImL2g0051030[4] = np.max(EigenValImL2g0010201030)

MaxEigenValImL2g0051040[0] = np.max(EigenValImL2g0010011040)
MaxEigenValImL2g0051040[1] = np.max(EigenValImL2g0010021040)
MaxEigenValImL2g0051040[2] = np.max(EigenValImL2g0010051040)
MaxEigenValImL2g0051040[3] = np.max(EigenValImL2g0010101040)
MaxEigenValImL2g0051040[4] = np.max(EigenValImL2g0010201040)

MaxEigenValImL2g0051050[0] = np.max(EigenValImL2g0010011050)
MaxEigenValImL2g0051050[1] = np.max(EigenValImL2g0010021050)
MaxEigenValImL2g0051050[2] = np.max(EigenValImL2g0010051050)
MaxEigenValImL2g0051050[3] = np.max(EigenValImL2g0010101050)
MaxEigenValImL2g0051050[4] = np.max(EigenValImL2g0010201050)

MaxEigenValImL2g0051Inf[0] = np.polyfit(fiveSizes, [MaxEigenValImL2g0051010[0],MaxEigenValImL2g0051020[0],MaxEigenValImL2g0051030[0],MaxEigenValImL2g0051040[0],MaxEigenValImL2g0051050[0]], 1)[[1]]
MaxEigenValImL2g0051Inf[1] = np.polyfit(fiveSizes, [MaxEigenValImL2g0051010[1],MaxEigenValImL2g0051020[1],MaxEigenValImL2g0051030[1],MaxEigenValImL2g0051040[1],MaxEigenValImL2g0051050[1]], 1)[[1]]
MaxEigenValImL2g0051Inf[2] = np.polyfit(fiveSizes, [MaxEigenValImL2g0051010[2],MaxEigenValImL2g0051020[2],MaxEigenValImL2g0051030[2],MaxEigenValImL2g0051040[2],MaxEigenValImL2g0051050[2]], 1)[[1]]
MaxEigenValImL2g0051Inf[3] = np.polyfit(fiveSizes, [MaxEigenValImL2g0051010[3],MaxEigenValImL2g0051020[3],MaxEigenValImL2g0051030[3],MaxEigenValImL2g0051040[3],MaxEigenValImL2g0051050[3]], 1)[[1]]
MaxEigenValImL2g0051Inf[4] = np.polyfit(fiveSizes, [MaxEigenValImL2g0051010[4],MaxEigenValImL2g0051020[4],MaxEigenValImL2g0051030[4],MaxEigenValImL2g0051040[4],MaxEigenValImL2g0051050[4]], 1)[[1]]

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

MaxEigenValImL2g0101010 = np.zeros((5))
MaxEigenValImL2g0101020 = np.zeros((5))
MaxEigenValImL2g0101030 = np.zeros((5))
MaxEigenValImL2g0101040 = np.zeros((5))
MaxEigenValImL2g0101050 = np.zeros((5))
MaxEigenValImL2g0101Inf = np.zeros((5))

MaxEigenValImL2g0101010[0] = np.max(EigenValImL2g0010011010)
MaxEigenValImL2g0101010[1] = np.max(EigenValImL2g0010021010)
MaxEigenValImL2g0101010[2] = np.max(EigenValImL2g0010051010)
MaxEigenValImL2g0101010[3] = np.max(EigenValImL2g0010101010)
MaxEigenValImL2g0101010[4] = np.max(EigenValImL2g0010201010)

MaxEigenValImL2g0101020[0] = np.max(EigenValImL2g0010011020)
MaxEigenValImL2g0101020[1] = np.max(EigenValImL2g0010021020)
MaxEigenValImL2g0101020[2] = np.max(EigenValImL2g0010051020)
MaxEigenValImL2g0101020[3] = np.max(EigenValImL2g0010101020)
MaxEigenValImL2g0101020[4] = np.max(EigenValImL2g0010201020)

MaxEigenValImL2g0101030[0] = np.max(EigenValImL2g0010011030)
MaxEigenValImL2g0101030[1] = np.max(EigenValImL2g0010021030)
MaxEigenValImL2g0101030[2] = np.max(EigenValImL2g0010051030)
MaxEigenValImL2g0101030[3] = np.max(EigenValImL2g0010101030)
MaxEigenValImL2g0101030[4] = np.max(EigenValImL2g0010201030)

MaxEigenValImL2g0101040[0] = np.max(EigenValImL2g0010011040)
MaxEigenValImL2g0101040[1] = np.max(EigenValImL2g0010021040)
MaxEigenValImL2g0101040[2] = np.max(EigenValImL2g0010051040)
MaxEigenValImL2g0101040[3] = np.max(EigenValImL2g0010101040)
MaxEigenValImL2g0101040[4] = np.max(EigenValImL2g0010201040)

MaxEigenValImL2g0101050[0] = np.max(EigenValImL2g0010011050)
MaxEigenValImL2g0101050[1] = np.max(EigenValImL2g0010021050)
MaxEigenValImL2g0101050[2] = np.max(EigenValImL2g0010051050)
MaxEigenValImL2g0101050[3] = np.max(EigenValImL2g0010101050)
MaxEigenValImL2g0101050[4] = np.max(EigenValImL2g0010201050)

MaxEigenValImL2g0101Inf[0] = np.polyfit(fiveSizes, [MaxEigenValImL2g0101010[0],MaxEigenValImL2g0101020[0],MaxEigenValImL2g0101030[0],MaxEigenValImL2g0101040[0],MaxEigenValImL2g0101050[0]], 1)[[1]]
MaxEigenValImL2g0101Inf[1] = np.polyfit(fiveSizes, [MaxEigenValImL2g0101010[1],MaxEigenValImL2g0101020[1],MaxEigenValImL2g0101030[1],MaxEigenValImL2g0101040[1],MaxEigenValImL2g0101050[1]], 1)[[1]]
MaxEigenValImL2g0101Inf[2] = np.polyfit(fiveSizes, [MaxEigenValImL2g0101010[2],MaxEigenValImL2g0101020[2],MaxEigenValImL2g0101030[2],MaxEigenValImL2g0101040[2],MaxEigenValImL2g0101050[2]], 1)[[1]]
MaxEigenValImL2g0101Inf[3] = np.polyfit(fiveSizes, [MaxEigenValImL2g0101010[3],MaxEigenValImL2g0101020[3],MaxEigenValImL2g0101030[3],MaxEigenValImL2g0101040[3],MaxEigenValImL2g0101050[3]], 1)[[1]]
MaxEigenValImL2g0101Inf[4] = np.polyfit(fiveSizes, [MaxEigenValImL2g0101010[4],MaxEigenValImL2g0101020[4],MaxEigenValImL2g0101030[4],MaxEigenValImL2g0101040[4],MaxEigenValImL2g0101050[4]], 1)[[1]]

########################################################################
########################################################################

Spreading = np.zeros((5))
Spreading[0] = 0.01
Spreading[1] = 0.02
Spreading[2] = 0.05
Spreading[3] = 0.10
Spreading[4] = 0.20

Coupling = np.zeros((4))
Coupling[0] = 0.01
Coupling[1] = 0.02
Coupling[2] = 0.05
Coupling[3] = 0.10

########################################################################
########################################################################

plt.clf()
plt.figure(figsize=(8,8))
plt.subplots_adjust(left=0.12,bottom=0.11,right=0.79,top=0.94)
#plt.plot(MomentumAxL0g20,Renormalization,'o')

plt.plot(Spreading,MaxEigenValImL0g0011010, marker='.',c=[1.0, 0.0, 0.0],ls='-',label='$g_{\\mathcal{K}}= 0.01,N=100$', markersize=1)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0011020, marker='.',c=[1.0, 0.0, 0.0],ls='-',label='$g_{\\mathcal{K}}= 0.01,N=200$', markeredgecolor=[1.0, 1.0, 0.0,1.0], markersize=1)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0011030, marker='.',c=[1.0, 0.0, 0.0],ls='-',label='$g_{\\mathcal{K}}= 0.01,N=300$', markeredgecolor=[0.0, 1.0, 0.0,1.0], markersize=1)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0011040, marker='.',c=[1.0, 0.0, 0.0],ls='-',label='$g_{\\mathcal{K}}= 0.01,N=400$', markeredgecolor=[0.0, 1.0, 1.0,1.0], markersize=1)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0011050, marker='.',c=[1.0, 0.0, 0.0],ls='-',label='$g_{\\mathcal{K}}= 0.01,N=500$', markeredgecolor=[0.0, 0.0, 1.0,1.0], markersize=1)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0011Inf, marker='o',c=[1.0, 0.0, 0.0],ls='-',label='$g_{\\mathcal{K}}= 0.01,N=\\infty$', markeredgecolor=[1.0, 0.0, 1.0,1.0], markersize=2)#,label='100')

plt.plot(Spreading,MaxEigenValImL0g0021010, marker='.',c=[1.0, 1.0, 0.0],ls='-',label='$g_{\\mathcal{K}}= 0.02,N=100$', markersize=1)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0021020, marker='.',c=[1.0, 1.0, 0.0],ls='-',label='$g_{\\mathcal{K}}= 0.02,N=200$', markeredgecolor=[1.0, 1.0, 0.0,1.0], markersize=1)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0021030, marker='.',c=[1.0, 1.0, 0.0],ls='-',label='$g_{\\mathcal{K}}= 0.02,N=300$', markeredgecolor=[0.0, 1.0, 0.0,1.0], markersize=1)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0021040, marker='.',c=[1.0, 1.0, 0.0],ls='-',label='$g_{\\mathcal{K}}= 0.02,N=400$', markeredgecolor=[0.0, 1.0, 1.0,1.0], markersize=1)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0021050, marker='.',c=[1.0, 1.0, 0.0],ls='-',label='$g_{\\mathcal{K}}= 0.02,N=500$', markeredgecolor=[0.0, 0.0, 1.0,1.0], markersize=1)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0021050, marker='o',c=[1.0, 1.0, 0.0],ls='-',label='$g_{\\mathcal{K}}= 0.02,N=\\infty$', markeredgecolor=[1.0, 0.0, 1.0,1.0], markersize=2)#,label='100')

plt.plot(Spreading,MaxEigenValImL0g0051010, marker='.',c=[0.0, 1.0, 0.0],ls='-',label='$g_{\\mathcal{K}}= 0.05,N=100$', markersize=1)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0051020, marker='.',c=[0.0, 1.0, 0.0],ls='-',label='$g_{\\mathcal{K}}= 0.05,N=200$', markeredgecolor=[1.0, 1.0, 0.0,1.0], markersize=1)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0051030, marker='.',c=[0.0, 1.0, 0.0],ls='-',label='$g_{\\mathcal{K}}= 0.05,N=300$', markeredgecolor=[0.0, 1.0, 0.0,1.0], markersize=1)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0051040, marker='.',c=[0.0, 1.0, 0.0],ls='-',label='$g_{\\mathcal{K}}= 0.05,N=400$', markeredgecolor=[0.0, 1.0, 1.0,1.0], markersize=1)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0051050, marker='.',c=[0.0, 1.0, 0.0],ls='-',label='$g_{\\mathcal{K}}= 0.05,N=500$', markeredgecolor=[0.0, 0.0, 1.0,1.0], markersize=1)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0051Inf, marker='o',c=[0.0, 1.0, 0.0],ls='-',label='$g_{\\mathcal{K}}= 0.05,N=\\infty', markeredgecolor=[1.0, 0.0, 1.0,1.0], markersize=2)#,label='100')

plt.plot(Spreading,MaxEigenValImL0g0101010, marker='.',c=[0.0, 1.0, 1.0],ls='-',label='$g_{\\mathcal{K}}= 0.10,N=100$', markersize=1)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0101020, marker='.',c=[0.0, 1.0, 1.0],ls='-',label='$g_{\\mathcal{K}}= 0.10,N=200$', markeredgecolor=[1.0, 1.0, 0.0,1.0], markersize=1)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0101030, marker='.',c=[0.0, 1.0, 1.0],ls='-',label='$g_{\\mathcal{K}}= 0.10,N=300$', markeredgecolor=[0.0, 1.0, 0.0,1.0], markersize=1)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0101040, marker='.',c=[0.0, 1.0, 1.0],ls='-',label='$g_{\\mathcal{K}}= 0.10,N=400$', markeredgecolor=[0.0, 1.0, 1.0,1.0], markersize=1)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0101050, marker='.',c=[0.0, 1.0, 1.0],ls='-',label='$g_{\\mathcal{K}}= 0.10,N=500$', markeredgecolor=[0.0, 0.0, 1.0,1.0], markersize=1)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0101Inf, marker='o',c=[0.0, 1.0, 1.0],ls='-',label='$g_{\\mathcal{K}}= 0.10,N=\\infty', markeredgecolor=[1.0, 0.0, 1.0,1.0], markersize=2)#,label='100')

#plt.xlim(left  =0)
#plt.ylim(bottom=0)
plt.xticks([0.01,0.02,0.05,0.10,0.20])
#plt.yticks(np.arange(0.984,+1.004, step=0.002))
#plt.show()

plt.legend(bbox_to_anchor=(0.90, 1.0), loc=2, borderaxespad=0.)
plt.suptitle('$\\ell=0$' ,fontsize=20, fontname='Times New Roman')

plt.xlabel('$a_{\\mathcal{K}}$')
plt.ylabel('$\\mathrm{Max}\\{\\mathrm{Im}[E]\\}$')

#plt.savefig('PlotsGlobalL0aZZZ.pdf')

##############################################################

plt.clf()
plt.figure(figsize=(8,8))
plt.subplots_adjust(left=0.12,bottom=0.11,right=0.79,top=0.94)
#plt.plot(MomentumAxL0g20,Renormalization,'o')

plt.plot(Coupling,[MaxEigenValImL0g0011010[0],MaxEigenValImL0g0021010[0],MaxEigenValImL0g0051010[0],MaxEigenValImL0g0101010[0]], marker='.',c=[1.0, 0.0, 0.0],ls='-',label='$a_{\\mathcal{K}}= 1,N=100$', markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011020[0],MaxEigenValImL0g0021020[0],MaxEigenValImL0g0051020[0],MaxEigenValImL0g0101020[0]], marker='.',c=[1.0, 0.0, 0.0],ls='-',label='$a_{\\mathcal{K}}= 1,N=200$', markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011030[0],MaxEigenValImL0g0021030[0],MaxEigenValImL0g0051030[0],MaxEigenValImL0g0101030[0]], marker='.',c=[1.0, 0.0, 0.0],ls='-',label='$a_{\\mathcal{K}}= 1,N=300$', markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011040[0],MaxEigenValImL0g0021040[0],MaxEigenValImL0g0051040[0],MaxEigenValImL0g0101040[0]], marker='.',c=[1.0, 0.0, 0.0],ls='-',label='$a_{\\mathcal{K}}= 1,N=400$', markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011050[0],MaxEigenValImL0g0021050[0],MaxEigenValImL0g0051050[0],MaxEigenValImL0g0101050[0]], marker='.',c=[1.0, 0.0, 0.0],ls='-',label='$a_{\\mathcal{K}}= 1,N=500$', markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011Inf[0],MaxEigenValImL0g0021Inf[0],MaxEigenValImL0g0051Inf[0],MaxEigenValImL0g0101Inf[0]], marker='.',c=[1.0, 0.0, 0.0],ls='-',label='$a_{\\mathcal{K}}= 1,N=\\infty$', markersize=3)#,label='100')

plt.plot(Coupling,[MaxEigenValImL0g0011010[1],MaxEigenValImL0g0021010[1],MaxEigenValImL0g0051010[1],MaxEigenValImL0g0101010[1]], marker='.',c=[1.0, 1.0, 0.0],ls='-',label='$a_{\\mathcal{K}}= 2,N=100$', markeredgecolor=[1.0, 1.0, 0.0,1.0], markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011020[1],MaxEigenValImL0g0021020[1],MaxEigenValImL0g0051020[1],MaxEigenValImL0g0101020[1]], marker='.',c=[1.0, 1.0, 0.0],ls='-',label='$a_{\\mathcal{K}}= 2,N=200$', markeredgecolor=[1.0, 1.0, 0.0,1.0], markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011030[1],MaxEigenValImL0g0021030[1],MaxEigenValImL0g0051030[1],MaxEigenValImL0g0101030[1]], marker='.',c=[1.0, 1.0, 0.0],ls='-',label='$a_{\\mathcal{K}}= 2,N=300$', markeredgecolor=[1.0, 1.0, 0.0,1.0], markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011040[1],MaxEigenValImL0g0021040[1],MaxEigenValImL0g0051040[1],MaxEigenValImL0g0101040[1]], marker='.',c=[1.0, 1.0, 0.0],ls='-',label='$a_{\\mathcal{K}}= 2,N=400$', markeredgecolor=[1.0, 1.0, 0.0,1.0], markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011050[1],MaxEigenValImL0g0021050[1],MaxEigenValImL0g0051050[1],MaxEigenValImL0g0101050[1]], marker='.',c=[1.0, 1.0, 0.0],ls='-',label='$a_{\\mathcal{K}}= 2,N=500$', markeredgecolor=[1.0, 1.0, 0.0,1.0], markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011Inf[1],MaxEigenValImL0g0021Inf[1],MaxEigenValImL0g0051Inf[1],MaxEigenValImL0g0101Inf[1]], marker='.',c=[1.0, 1.0, 0.0],ls='-',label='$a_{\\mathcal{K}}= 2,N=\\infty$', markeredgecolor=[1.0, 1.0, 0.0,1.0], markersize=3)#,label='100')

plt.plot(Coupling,[MaxEigenValImL0g0011010[2],MaxEigenValImL0g0021010[2],MaxEigenValImL0g0051010[2],MaxEigenValImL0g0101010[2]], marker='.',c=[0.0, 1.0, 0.0],ls='-',label='$a_{\\mathcal{K}}= 5,N=100$', markeredgecolor=[0.0, 1.0, 0.0,1.0], markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011020[2],MaxEigenValImL0g0021020[2],MaxEigenValImL0g0051020[2],MaxEigenValImL0g0101020[2]], marker='.',c=[0.0, 1.0, 0.0],ls='-',label='$a_{\\mathcal{K}}= 5,N=200$', markeredgecolor=[0.0, 1.0, 0.0,1.0], markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011030[2],MaxEigenValImL0g0021030[2],MaxEigenValImL0g0051030[2],MaxEigenValImL0g0101030[2]], marker='.',c=[0.0, 1.0, 0.0],ls='-',label='$a_{\\mathcal{K}}= 5,N=300$', markeredgecolor=[0.0, 1.0, 0.0,1.0], markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011040[2],MaxEigenValImL0g0021040[2],MaxEigenValImL0g0051040[2],MaxEigenValImL0g0101040[2]], marker='.',c=[0.0, 1.0, 0.0],ls='-',label='$a_{\\mathcal{K}}= 5,N=400$', markeredgecolor=[0.0, 1.0, 0.0,1.0], markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011050[2],MaxEigenValImL0g0021050[2],MaxEigenValImL0g0051050[2],MaxEigenValImL0g0101050[2]], marker='.',c=[0.0, 1.0, 0.0],ls='-',label='$a_{\\mathcal{K}}= 5,N=500$', markeredgecolor=[0.0, 1.0, 0.0,1.0], markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011Inf[2],MaxEigenValImL0g0021Inf[2],MaxEigenValImL0g0051Inf[2],MaxEigenValImL0g0101Inf[2]], marker='.',c=[0.0, 1.0, 0.0],ls='-',label='$a_{\\mathcal{K}}= 5,N=\\infty$', markeredgecolor=[0.0, 1.0, 0.0,1.0], markersize=3)#,label='100')

plt.plot(Coupling,[MaxEigenValImL0g0011010[3],MaxEigenValImL0g0021010[3],MaxEigenValImL0g0051010[3],MaxEigenValImL0g0101010[3]], marker='.',c=[0.0, 1.0, 1.0],ls='-',label='$a_{\\mathcal{K}}= 10,N=100$', markeredgecolor=[0.0, 1.0, 1.0,1.0], markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011020[3],MaxEigenValImL0g0021020[3],MaxEigenValImL0g0051020[3],MaxEigenValImL0g0101020[3]], marker='.',c=[0.0, 1.0, 1.0],ls='-',label='$a_{\\mathcal{K}}= 10,N=200$', markeredgecolor=[0.0, 1.0, 1.0,1.0], markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011030[3],MaxEigenValImL0g0021030[3],MaxEigenValImL0g0051030[3],MaxEigenValImL0g0101030[3]], marker='.',c=[0.0, 1.0, 1.0],ls='-',label='$a_{\\mathcal{K}}= 10,N=300$', markeredgecolor=[0.0, 1.0, 1.0,1.0], markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011040[3],MaxEigenValImL0g0021040[3],MaxEigenValImL0g0051040[3],MaxEigenValImL0g0101040[3]], marker='.',c=[0.0, 1.0, 1.0],ls='-',label='$a_{\\mathcal{K}}= 10,N=400$', markeredgecolor=[0.0, 1.0, 1.0,1.0], markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011050[3],MaxEigenValImL0g0021050[3],MaxEigenValImL0g0051050[3],MaxEigenValImL0g0101050[3]], marker='.',c=[0.0, 1.0, 1.0],ls='-',label='$a_{\\mathcal{K}}= 10,N=500$', markeredgecolor=[0.0, 1.0, 1.0,1.0], markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011Inf[3],MaxEigenValImL0g0021Inf[3],MaxEigenValImL0g0051Inf[3],MaxEigenValImL0g0101Inf[3]], marker='.',c=[0.0, 1.0, 1.0],ls='-',label='$a_{\\mathcal{K}}= 10,N=\\infty$', markeredgecolor=[0.0, 1.0, 1.0,1.0], markersize=3)#,label='100')

plt.plot(Coupling,[MaxEigenValImL0g0011010[4],MaxEigenValImL0g0021010[4],MaxEigenValImL0g0051010[4],MaxEigenValImL0g0101010[4]], marker='.',c=[0.0, 0.0, 1.0],ls='-',label='$a_{\\mathcal{K}}= 20,N=100$', markeredgecolor=[0.0, 0.0, 1.0,1.0], markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011020[4],MaxEigenValImL0g0021020[4],MaxEigenValImL0g0051020[4],MaxEigenValImL0g0101020[4]], marker='.',c=[0.0, 0.0, 1.0],ls='-',label='$a_{\\mathcal{K}}= 20,N=200$', markeredgecolor=[0.0, 0.0, 1.0,1.0], markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011030[4],MaxEigenValImL0g0021030[4],MaxEigenValImL0g0051030[4],MaxEigenValImL0g0101030[4]], marker='.',c=[0.0, 0.0, 1.0],ls='-',label='$a_{\\mathcal{K}}= 20,N=300$', markeredgecolor=[0.0, 0.0, 1.0,1.0], markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011040[4],MaxEigenValImL0g0021040[4],MaxEigenValImL0g0051040[4],MaxEigenValImL0g0101040[4]], marker='.',c=[0.0, 0.0, 1.0],ls='-',label='$a_{\\mathcal{K}}= 20,N=400$', markeredgecolor=[0.0, 0.0, 1.0,1.0], markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011050[4],MaxEigenValImL0g0021050[4],MaxEigenValImL0g0051050[4],MaxEigenValImL0g0101050[4]], marker='.',c=[0.0, 0.0, 1.0],ls='-',label='$a_{\\mathcal{K}}= 20,N=500$', markeredgecolor=[0.0, 0.0, 1.0,1.0], markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011Inf[4],MaxEigenValImL0g0021Inf[4],MaxEigenValImL0g0051Inf[4],MaxEigenValImL0g0101Inf[4]], marker='.',c=[0.0, 0.0, 1.0],ls='-',label='$a_{\\mathcal{K}}= 20,N=\\infty$', markeredgecolor=[0.0, 0.0, 1.0,1.0], markersize=3)#,label='100')

#plt.xlim(left  =0)
#plt.ylim(bottom=0)
plt.xticks([0.01,0.02,0.05,0.10])
#plt.yticks(np.arange(0.984,+1.004, step=0.002))
#plt.show()

plt.legend(bbox_to_anchor=(1.00, 1.0), loc=2, borderaxespad=0.)
plt.suptitle('$\\ell=0$' ,fontsize=20, fontname='Times New Roman')

plt.xlabel('$g_{\\mathcal{K}}$')
plt.ylabel('$\\mathrm{Max}\\{\\mathrm{Im}[E]\\}$')


#plt.savefig('PlotsGlobalL0gZZZ.pdf')

########################################################################
########################################################################

plt.clf()
plt.figure(figsize=(8,8))
plt.subplots_adjust(left=0.12,bottom=0.11,right=0.79,top=0.94)
#plt.plot(MomentumAxL2g20,Renormalization,'o')

plt.plot(Spreading,MaxEigenValImL2g0011010, marker='.',c=[1.0, 0.0, 0.0],ls='-',label='$g_{\\mathcal{K}}= 0.01,N=100$', markersize=1)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0011020, marker='.',c=[1.0, 0.0, 0.0],ls='-',label='$g_{\\mathcal{K}}= 0.01,N=200$', markeredgecolor=[1.0, 1.0, 0.0,1.0], markersize=1)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0011030, marker='.',c=[1.0, 0.0, 0.0],ls='-',label='$g_{\\mathcal{K}}= 0.01,N=300$', markeredgecolor=[0.0, 1.0, 0.0,1.0], markersize=1)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0011040, marker='.',c=[1.0, 0.0, 0.0],ls='-',label='$g_{\\mathcal{K}}= 0.01,N=400$', markeredgecolor=[0.0, 1.0, 1.0,1.0], markersize=1)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0011050, marker='.',c=[1.0, 0.0, 0.0],ls='-',label='$g_{\\mathcal{K}}= 0.01,N=500$', markeredgecolor=[0.0, 0.0, 1.0,1.0], markersize=1)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0011Inf, marker='o',c=[1.0, 0.0, 0.0],ls='-',label='$g_{\\mathcal{K}}= 0.01,N=\\infty$', markeredgecolor=[1.0, 0.0, 1.0,1.0], markersize=2)#,label='100')

plt.plot(Spreading,MaxEigenValImL2g0021010, marker='.',c=[1.0, 1.0, 0.0],ls='-',label='$g_{\\mathcal{K}}= 0.02,N=100$', markersize=1)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0021020, marker='.',c=[1.0, 1.0, 0.0],ls='-',label='$g_{\\mathcal{K}}= 0.02,N=200$', markeredgecolor=[1.0, 1.0, 0.0,1.0], markersize=1)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0021030, marker='.',c=[1.0, 1.0, 0.0],ls='-',label='$g_{\\mathcal{K}}= 0.02,N=300$', markeredgecolor=[0.0, 1.0, 0.0,1.0], markersize=1)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0021040, marker='.',c=[1.0, 1.0, 0.0],ls='-',label='$g_{\\mathcal{K}}= 0.02,N=400$', markeredgecolor=[0.0, 1.0, 1.0,1.0], markersize=1)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0021050, marker='.',c=[1.0, 1.0, 0.0],ls='-',label='$g_{\\mathcal{K}}= 0.02,N=500$', markeredgecolor=[0.0, 0.0, 1.0,1.0], markersize=1)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0021050, marker='o',c=[1.0, 1.0, 0.0],ls='-',label='$g_{\\mathcal{K}}= 0.02,N=\\infty$', markeredgecolor=[1.0, 0.0, 1.0,1.0], markersize=2)#,label='100')

plt.plot(Spreading,MaxEigenValImL2g0051010, marker='.',c=[0.0, 1.0, 0.0],ls='-',label='$g_{\\mathcal{K}}= 0.05,N=100$', markersize=1)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0051020, marker='.',c=[0.0, 1.0, 0.0],ls='-',label='$g_{\\mathcal{K}}= 0.05,N=200$', markeredgecolor=[1.0, 1.0, 0.0,1.0], markersize=1)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0051030, marker='.',c=[0.0, 1.0, 0.0],ls='-',label='$g_{\\mathcal{K}}= 0.05,N=300$', markeredgecolor=[0.0, 1.0, 0.0,1.0], markersize=1)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0051040, marker='.',c=[0.0, 1.0, 0.0],ls='-',label='$g_{\\mathcal{K}}= 0.05,N=400$', markeredgecolor=[0.0, 1.0, 1.0,1.0], markersize=1)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0051050, marker='.',c=[0.0, 1.0, 0.0],ls='-',label='$g_{\\mathcal{K}}= 0.05,N=500$', markeredgecolor=[0.0, 0.0, 1.0,1.0], markersize=1)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0051Inf, marker='o',c=[0.0, 1.0, 0.0],ls='-',label='$g_{\\mathcal{K}}= 0.05,N=\\infty', markeredgecolor=[1.0, 0.0, 1.0,1.0], markersize=2)#,label='100')

plt.plot(Spreading,MaxEigenValImL2g0101010, marker='.',c=[0.0, 1.0, 1.0],ls='-',label='$g_{\\mathcal{K}}= 0.10,N=100$', markersize=1)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0101020, marker='.',c=[0.0, 1.0, 1.0],ls='-',label='$g_{\\mathcal{K}}= 0.10,N=200$', markeredgecolor=[1.0, 1.0, 0.0,1.0], markersize=1)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0101030, marker='.',c=[0.0, 1.0, 1.0],ls='-',label='$g_{\\mathcal{K}}= 0.10,N=300$', markeredgecolor=[0.0, 1.0, 0.0,1.0], markersize=1)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0101040, marker='.',c=[0.0, 1.0, 1.0],ls='-',label='$g_{\\mathcal{K}}= 0.10,N=400$', markeredgecolor=[0.0, 1.0, 1.0,1.0], markersize=1)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0101050, marker='.',c=[0.0, 1.0, 1.0],ls='-',label='$g_{\\mathcal{K}}= 0.10,N=500$', markeredgecolor=[0.0, 0.0, 1.0,1.0], markersize=1)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0101Inf, marker='o',c=[0.0, 1.0, 1.0],ls='-',label='$g_{\\mathcal{K}}= 0.10,N=\\infty', markeredgecolor=[0.0, 0.0, 1.0,1.0], markersize=2)#,label='100')

#plt.xlim(left  =0)
#plt.ylim(bottom=0)
plt.xticks([0.01,0.02,0.05,0.10,0.20])
#plt.yticks(np.arange(0.984,+1.004, step=0.002))
#plt.show()

plt.legend(bbox_to_anchor=(0.90, 1.0), loc=2, borderaxespad=0.)
plt.suptitle('$\\ell=2$' ,fontsize=20, fontname='Times New Roman')

plt.xlabel('$a_{\\mathcal{K}}$')
plt.ylabel('$\\mathrm{Max}\\{\\mathrm{Im}[E]\\}$')

#plt.savefig('PlotsGlobalL2aZZZ.pdf')

##############################################################

plt.clf()
plt.figure(figsize=(8,8))
plt.subplots_adjust(left=0.12,bottom=0.11,right=0.79,top=0.94)
#plt.plot(MomentumAxL2g20,Renormalization,'o')

plt.plot(Coupling,[MaxEigenValImL2g0011010[0],MaxEigenValImL2g0021010[0],MaxEigenValImL2g0051010[0],MaxEigenValImL2g0101010[0]], marker='.',c=[1.0, 0.0, 0.0],ls='-',label='$a_{\\mathcal{K}}= 1,N=100$', markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011020[0],MaxEigenValImL2g0021020[0],MaxEigenValImL2g0051020[0],MaxEigenValImL2g0101020[0]], marker='.',c=[1.0, 0.0, 0.0],ls='-',label='$a_{\\mathcal{K}}= 1,N=200$', markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011030[0],MaxEigenValImL2g0021030[0],MaxEigenValImL2g0051030[0],MaxEigenValImL2g0101030[0]], marker='.',c=[1.0, 0.0, 0.0],ls='-',label='$a_{\\mathcal{K}}= 1,N=300$', markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011040[0],MaxEigenValImL2g0021040[0],MaxEigenValImL2g0051040[0],MaxEigenValImL2g0101040[0]], marker='.',c=[1.0, 0.0, 0.0],ls='-',label='$a_{\\mathcal{K}}= 1,N=400$', markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011050[0],MaxEigenValImL2g0021050[0],MaxEigenValImL2g0051050[0],MaxEigenValImL2g0101050[0]], marker='.',c=[1.0, 0.0, 0.0],ls='-',label='$a_{\\mathcal{K}}= 1,N=500$', markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011Inf[0],MaxEigenValImL2g0021Inf[0],MaxEigenValImL2g0051Inf[0],MaxEigenValImL2g0101Inf[0]], marker='.',c=[1.0, 0.0, 0.0],ls='-',label='$a_{\\mathcal{K}}= 1,N=\\infty$', markersize=3)#,label='100')

plt.plot(Coupling,[MaxEigenValImL2g0011010[1],MaxEigenValImL2g0021010[1],MaxEigenValImL2g0051010[1],MaxEigenValImL2g0101010[1]], marker='.',c=[1.0, 1.0, 0.0],ls='-',label='$a_{\\mathcal{K}}= 2,N=100$', markeredgecolor=[1.0, 1.0, 0.0,1.0], markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011020[1],MaxEigenValImL2g0021020[1],MaxEigenValImL2g0051020[1],MaxEigenValImL2g0101020[1]], marker='.',c=[1.0, 1.0, 0.0],ls='-',label='$a_{\\mathcal{K}}= 2,N=200$', markeredgecolor=[1.0, 1.0, 0.0,1.0], markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011030[1],MaxEigenValImL2g0021030[1],MaxEigenValImL2g0051030[1],MaxEigenValImL2g0101030[1]], marker='.',c=[1.0, 1.0, 0.0],ls='-',label='$a_{\\mathcal{K}}= 2,N=300$', markeredgecolor=[1.0, 1.0, 0.0,1.0], markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011040[1],MaxEigenValImL2g0021040[1],MaxEigenValImL2g0051040[1],MaxEigenValImL2g0101040[1]], marker='.',c=[1.0, 1.0, 0.0],ls='-',label='$a_{\\mathcal{K}}= 2,N=400$', markeredgecolor=[1.0, 1.0, 0.0,1.0], markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011050[1],MaxEigenValImL2g0021050[1],MaxEigenValImL2g0051050[1],MaxEigenValImL2g0101050[1]], marker='.',c=[1.0, 1.0, 0.0],ls='-',label='$a_{\\mathcal{K}}= 2,N=500$', markeredgecolor=[1.0, 1.0, 0.0,1.0], markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011Inf[1],MaxEigenValImL2g0021Inf[1],MaxEigenValImL2g0051Inf[1],MaxEigenValImL2g0101Inf[1]], marker='.',c=[1.0, 1.0, 0.0],ls='-',label='$a_{\\mathcal{K}}= 2,N=\\infty$', markeredgecolor=[1.0, 1.0, 0.0,1.0], markersize=3)#,label='100')

plt.plot(Coupling,[MaxEigenValImL2g0011010[2],MaxEigenValImL2g0021010[2],MaxEigenValImL2g0051010[2],MaxEigenValImL2g0101010[2]], marker='.',c=[0.0, 1.0, 0.0],ls='-',label='$a_{\\mathcal{K}}= 5,N=100$', markeredgecolor=[0.0, 1.0, 0.0,1.0], markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011020[2],MaxEigenValImL2g0021020[2],MaxEigenValImL2g0051020[2],MaxEigenValImL2g0101020[2]], marker='.',c=[0.0, 1.0, 0.0],ls='-',label='$a_{\\mathcal{K}}= 5,N=200$', markeredgecolor=[0.0, 1.0, 0.0,1.0], markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011030[2],MaxEigenValImL2g0021030[2],MaxEigenValImL2g0051030[2],MaxEigenValImL2g0101030[2]], marker='.',c=[0.0, 1.0, 0.0],ls='-',label='$a_{\\mathcal{K}}= 5,N=300$', markeredgecolor=[0.0, 1.0, 0.0,1.0], markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011040[2],MaxEigenValImL2g0021040[2],MaxEigenValImL2g0051040[2],MaxEigenValImL2g0101040[2]], marker='.',c=[0.0, 1.0, 0.0],ls='-',label='$a_{\\mathcal{K}}= 5,N=400$', markeredgecolor=[0.0, 1.0, 0.0,1.0], markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011050[2],MaxEigenValImL2g0021050[2],MaxEigenValImL2g0051050[2],MaxEigenValImL2g0101050[2]], marker='.',c=[0.0, 1.0, 0.0],ls='-',label='$a_{\\mathcal{K}}= 5,N=500$', markeredgecolor=[0.0, 1.0, 0.0,1.0], markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011Inf[2],MaxEigenValImL2g0021Inf[2],MaxEigenValImL2g0051Inf[2],MaxEigenValImL2g0101Inf[2]], marker='.',c=[0.0, 1.0, 0.0],ls='-',label='$a_{\\mathcal{K}}= 5,N=\\infty$', markeredgecolor=[0.0, 1.0, 0.0,1.0], markersize=3)#,label='100')

plt.plot(Coupling,[MaxEigenValImL2g0011010[3],MaxEigenValImL2g0021010[3],MaxEigenValImL2g0051010[3],MaxEigenValImL2g0101010[3]], marker='.',c=[0.0, 1.0, 1.0],ls='-',label='$a_{\\mathcal{K}}= 10,N=100$', markeredgecolor=[0.0, 1.0, 1.0,1.0], markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011020[3],MaxEigenValImL2g0021020[3],MaxEigenValImL2g0051020[3],MaxEigenValImL2g0101020[3]], marker='.',c=[0.0, 1.0, 1.0],ls='-',label='$a_{\\mathcal{K}}= 10,N=200$', markeredgecolor=[0.0, 1.0, 1.0,1.0], markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011030[3],MaxEigenValImL2g0021030[3],MaxEigenValImL2g0051030[3],MaxEigenValImL2g0101030[3]], marker='.',c=[0.0, 1.0, 1.0],ls='-',label='$a_{\\mathcal{K}}= 10,N=300$', markeredgecolor=[0.0, 1.0, 1.0,1.0], markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011040[3],MaxEigenValImL2g0021040[3],MaxEigenValImL2g0051040[3],MaxEigenValImL2g0101040[3]], marker='.',c=[0.0, 1.0, 1.0],ls='-',label='$a_{\\mathcal{K}}= 10,N=400$', markeredgecolor=[0.0, 1.0, 1.0,1.0], markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011050[3],MaxEigenValImL2g0021050[3],MaxEigenValImL2g0051050[3],MaxEigenValImL2g0101050[3]], marker='.',c=[0.0, 1.0, 1.0],ls='-',label='$a_{\\mathcal{K}}= 10,N=500$', markeredgecolor=[0.0, 1.0, 1.0,1.0], markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011Inf[3],MaxEigenValImL2g0021Inf[3],MaxEigenValImL2g0051Inf[3],MaxEigenValImL2g0101Inf[3]], marker='.',c=[0.0, 1.0, 1.0],ls='-',label='$a_{\\mathcal{K}}= 10,N=\\infty$', markeredgecolor=[0.0, 1.0, 1.0,1.0], markersize=3)#,label='100')

plt.plot(Coupling,[MaxEigenValImL2g0011010[4],MaxEigenValImL2g0021010[4],MaxEigenValImL2g0051010[4],MaxEigenValImL2g0101010[4]], marker='.',c=[0.0, 0.0, 1.0],ls='-',label='$a_{\\mathcal{K}}= 20,N=100$', markeredgecolor=[0.0, 0.0, 1.0,1.0], markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011020[4],MaxEigenValImL2g0021020[4],MaxEigenValImL2g0051020[4],MaxEigenValImL2g0101020[4]], marker='.',c=[0.0, 0.0, 1.0],ls='-',label='$a_{\\mathcal{K}}= 20,N=200$', markeredgecolor=[0.0, 0.0, 1.0,1.0], markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011030[4],MaxEigenValImL2g0021030[4],MaxEigenValImL2g0051030[4],MaxEigenValImL2g0101030[4]], marker='.',c=[0.0, 0.0, 1.0],ls='-',label='$a_{\\mathcal{K}}= 20,N=300$', markeredgecolor=[0.0, 0.0, 1.0,1.0], markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011040[4],MaxEigenValImL2g0021040[4],MaxEigenValImL2g0051040[4],MaxEigenValImL2g0101040[4]], marker='.',c=[0.0, 0.0, 1.0],ls='-',label='$a_{\\mathcal{K}}= 20,N=400$', markeredgecolor=[0.0, 0.0, 1.0,1.0], markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011050[4],MaxEigenValImL2g0021050[4],MaxEigenValImL2g0051050[4],MaxEigenValImL2g0101050[4]], marker='.',c=[0.0, 0.0, 1.0],ls='-',label='$a_{\\mathcal{K}}= 20,N=500$', markeredgecolor=[0.0, 0.0, 1.0,1.0], markersize=3)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011Inf[4],MaxEigenValImL2g0021Inf[4],MaxEigenValImL2g0051Inf[4],MaxEigenValImL2g0101Inf[4]], marker='.',c=[0.0, 0.0, 1.0],ls='-',label='$a_{\\mathcal{K}}= 20,N=\\infty$', markeredgecolor=[0.0, 0.0, 1.0,1.0], markersize=3)#,label='100')

#plt.xlim(left  =0)
#plt.ylim(bottom=0)
plt.xticks([0.01,0.02,0.05,0.10])
#plt.yticks(np.arange(0.984,+1.004, step=0.002))
#plt.show()

plt.legend(bbox_to_anchor=(1.00, 1.0), loc=2, borderaxespad=0.)
plt.suptitle('$\\ell=2$' ,fontsize=20, fontname='Times New Roman')

plt.xlabel('$g_{\\mathcal{K}}$')
plt.ylabel('$\\mathrm{Max}\\{\\mathrm{Im}[E]\\}$')


#plt.savefig('PlotsGlobalL2gZZZ.pdf')

########################################################################
########################################################################

plt.clf()
plt.figure(figsize=(8,8))
plt.subplots_adjust(left=0.12,bottom=0.11,right=0.79,top=0.94)
#plt.plot(MomentumAxL2g20,Renormalization,'o')

plt.plot(Spreading,MaxEigenValImL0g0011010, marker='*',c=[1.0, 0.0, 0.0],ls='-',label='$\\ell=0,N=100$', markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0011020, marker='*',c=[1.0, 0.0, 0.0],ls='-',label='$\\ell=0,N=200$', markeredgecolor=[1.0, 1.0, 0.0,1.0], markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0011030, marker='*',c=[1.0, 0.0, 0.0],ls='-',label='$\\ell=0,N=300$', markeredgecolor=[0.0, 1.0, 0.0,1.0], markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0011040, marker='*',c=[1.0, 0.0, 0.0],ls='-',label='$\\ell=0,N=400$', markeredgecolor=[0.0, 1.0, 1.0,1.0], markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0011050, marker='*',c=[1.0, 0.0, 0.0],ls='-',label='$\\ell=0,N=500$', markeredgecolor=[0.0, 0.0, 1.0,1.0], markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0011Inf, marker='*',c=[1.0, 0.0, 0.0],ls='-',label='$\\ell=0,N=\\infty$', markeredgecolor=[1.0, 0.0, 1.0,1.0], markersize=3)#,label='100')

plt.plot(Spreading,MaxEigenValImL2g0011010, marker='.',c=[1.0, 0.0, 0.0],ls='--',label='$\\ell=2,N=100$', markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0011020, marker='.',c=[1.0, 0.0, 0.0],ls='--',label='$\\ell=2,N=200$', markeredgecolor=[1.0, 1.0, 0.0,1.0], markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0011030, marker='.',c=[1.0, 0.0, 0.0],ls='--',label='$\\ell=2,N=300$', markeredgecolor=[0.0, 1.0, 0.0,1.0], markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0011040, marker='.',c=[1.0, 0.0, 0.0],ls='--',label='$\\ell=2,N=400$', markeredgecolor=[0.0, 1.0, 1.0,1.0], markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0011050, marker='.',c=[1.0, 0.0, 0.0],ls='--',label='$\\ell=2,N=500$', markeredgecolor=[0.0, 0.0, 1.0,1.0], markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0011Inf, marker='.',c=[1.0, 0.0, 0.0],ls='--',label='$\\ell=2,N=\\infty$', markeredgecolor=[1.0, 0.0, 1.0,1.0], markersize=3)#,label='100')

#plt.xlim(left  =0)
#plt.ylim(bottom=0)
plt.xticks([0.01,0.02,0.05,0.10,0.20])
#plt.yticks(np.arange(0.984,+1.004, step=0.002))
#plt.show()

plt.legend(bbox_to_anchor=(0.85, 1.0), loc=2, borderaxespad=0.)
plt.suptitle('$g_{\\mathcal{K}}= 0.01$' ,fontsize=20, fontname='Times New Roman')

plt.xlabel('$a_{\\mathcal{K}}$')
plt.ylabel('$\\mathrm{Max}\\{\\mathrm{Im}[E]\\}$')

#plt.savefig('PlotsGlobalg001.pdf')

########################################################################
########################################################################

plt.clf()
plt.figure(figsize=(8,8))
plt.subplots_adjust(left=0.12,bottom=0.11,right=0.79,top=0.94)
#plt.plot(MomentumAxL2g20,Renormalization,'o')

plt.plot(Spreading,MaxEigenValImL0g0021010, marker='*',c=[1.0, 1.0, 0.0],ls='-',label='$\\ell=0,N=100$', markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0021020, marker='*',c=[1.0, 1.0, 0.0],ls='-',label='$\\ell=0,N=200$', markeredgecolor=[1.0, 1.0, 0.0,1.0], markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0021030, marker='*',c=[1.0, 1.0, 0.0],ls='-',label='$\\ell=0,N=300$', markeredgecolor=[0.0, 1.0, 0.0,1.0], markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0021040, marker='*',c=[1.0, 1.0, 0.0],ls='-',label='$\\ell=0,N=400$', markeredgecolor=[0.0, 1.0, 1.0,1.0], markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0021050, marker='*',c=[1.0, 1.0, 0.0],ls='-',label='$\\ell=0,N=500$', markeredgecolor=[0.0, 0.0, 1.0,1.0], markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0021Inf, marker='*',c=[1.0, 1.0, 0.0],ls='-',label='$\\ell=0,N=\\infty$', markeredgecolor=[1.0, 0.0, 1.0,1.0], markersize=3)#,label='100')

plt.plot(Spreading,MaxEigenValImL2g0021010, marker='.',c=[1.0, 1.0, 0.0],ls='--',label='$\\ell=2,N=100$', markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0021020, marker='.',c=[1.0, 1.0, 0.0],ls='--',label='$\\ell=2,N=200$', markeredgecolor=[1.0, 1.0, 0.0,1.0], markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0021030, marker='.',c=[1.0, 1.0, 0.0],ls='--',label='$\\ell=2,N=300$', markeredgecolor=[0.0, 1.0, 0.0,1.0], markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0021040, marker='.',c=[1.0, 1.0, 0.0],ls='--',label='$\\ell=2,N=400$', markeredgecolor=[0.0, 1.0, 1.0,1.0], markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0021050, marker='.',c=[1.0, 1.0, 0.0],ls='--',label='$\\ell=2,N=500$', markeredgecolor=[0.0, 0.0, 1.0,1.0], markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0021050, marker='.',c=[1.0, 1.0, 0.0],ls='--',label='$\\ell=2,N=\\infty$', markeredgecolor=[1.0, 0.0, 1.0,1.0], markersize=3)#,label='100')

#plt.xlim(left  =0)
#plt.ylim(bottom=0)
plt.xticks([0.01,0.02,0.05,0.10,0.20])
#plt.yticks(np.arange(0.984,+1.004, step=0.002))
#plt.show()

plt.legend(bbox_to_anchor=(0.85, 1.0), loc=2, borderaxespad=0.)
plt.suptitle('$g_{\\mathcal{K}}= 0.02$' ,fontsize=20, fontname='Times New Roman')

plt.xlabel('$a_{\\mathcal{K}}$')
plt.ylabel('$\\mathrm{Max}\\{\\mathrm{Im}[E]\\}$')

#plt.savefig('PlotsGlobalg002.pdf')

########################################################################
########################################################################

plt.clf()
plt.figure(figsize=(8,8))
plt.subplots_adjust(left=0.12,bottom=0.11,right=0.79,top=0.94)
#plt.plot(MomentumAxL2g20,Renormalization,'o')

plt.plot(Spreading,MaxEigenValImL0g0051010, marker='*',c=[0.0, 1.0, 0.0],ls='-',label='$\\ell=0,N=100$', markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0051020, marker='*',c=[0.0, 1.0, 0.0],ls='-',label='$\\ell=0,N=200$', markeredgecolor=[1.0, 1.0, 0.0,1.0], markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0051030, marker='*',c=[0.0, 1.0, 0.0],ls='-',label='$\\ell=0,N=300$', markeredgecolor=[0.0, 1.0, 0.0,1.0], markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0051040, marker='*',c=[0.0, 1.0, 0.0],ls='-',label='$\\ell=0,N=400$', markeredgecolor=[0.0, 1.0, 1.0,1.0], markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0051050, marker='*',c=[0.0, 1.0, 0.0],ls='-',label='$\\ell=0,N=500$', markeredgecolor=[0.0, 0.0, 1.0,1.0], markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0051Inf, marker='*',c=[0.0, 1.0, 0.0],ls='-',label='$\\ell=0,N=\\infty$', markeredgecolor=[1.0, 0.0, 1.0,1.0], markersize=3)#,label='100')

plt.plot(Spreading,MaxEigenValImL2g0051010, marker='.',c=[0.0, 1.0, 0.0],ls='--',label='$\\ell=2,N=100$', markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0051020, marker='.',c=[0.0, 1.0, 0.0],ls='--',label='$\\ell=2,N=200$', markeredgecolor=[1.0, 1.0, 0.0,1.0], markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0051030, marker='.',c=[0.0, 1.0, 0.0],ls='--',label='$\\ell=2,N=300$', markeredgecolor=[0.0, 1.0, 0.0,1.0], markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0051040, marker='.',c=[0.0, 1.0, 0.0],ls='--',label='$\\ell=2,N=400$', markeredgecolor=[0.0, 1.0, 1.0,1.0], markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0051050, marker='.',c=[0.0, 1.0, 0.0],ls='--',label='$\\ell=2,N=500$', markeredgecolor=[0.0, 0.0, 1.0,1.0], markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0051Inf, marker='.',c=[0.0, 1.0, 0.0],ls='--',label='$\\ell=2,N=\\infty$', markeredgecolor=[1.0, 0.0, 1.0,1.0], markersize=3)#,label='100')

#plt.xlim(left  =0)
#plt.ylim(bottom=0)
plt.xticks([0.01,0.02,0.05,0.10,0.20])
#plt.yticks(np.arange(0.984,+1.004, step=0.002))
#plt.show()

plt.legend(bbox_to_anchor=(0.85, 1.0), loc=2, borderaxespad=0.)
plt.suptitle('$g_{\\mathcal{K}}= 0.05$' ,fontsize=20, fontname='Times New Roman')

plt.xlabel('$a_{\\mathcal{K}}$')
plt.ylabel('$\\mathrm{Max}\\{\\mathrm{Im}[E]\\}$')

#plt.savefig('PlotsGlobalg005.pdf')

########################################################################
########################################################################

plt.clf()
plt.figure(figsize=(8,8))
plt.subplots_adjust(left=0.12,bottom=0.11,right=0.79,top=0.94)
#plt.plot(MomentumAxL2g20,Renormalization,'o')

plt.plot(Spreading,MaxEigenValImL0g0101010, marker='*',c=[0.0, 1.0, 1.0],ls='-',label='$\\ell=0,N=100$', markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0101020, marker='*',c=[0.0, 1.0, 1.0],ls='-',label='$\\ell=0,N=200$', markeredgecolor=[1.0, 1.0, 0.0,1.0], markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0101030, marker='*',c=[0.0, 1.0, 1.0],ls='-',label='$\\ell=0,N=300$', markeredgecolor=[0.0, 1.0, 0.0,1.0], markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0101040, marker='*',c=[0.0, 1.0, 1.0],ls='-',label='$\\ell=0,N=400$', markeredgecolor=[0.0, 1.0, 1.0,1.0], markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0101050, marker='*',c=[0.0, 1.0, 1.0],ls='-',label='$\\ell=0,N=500$', markeredgecolor=[0.0, 0.0, 1.0,1.0], markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0101Inf, marker='*',c=[0.0, 1.0, 1.0],ls='-',label='$\\ell=0,N=\\infty$', markeredgecolor=[1.0, 0.0, 1.0,1.0], markersize=3)#,label='100')

plt.plot(Spreading,MaxEigenValImL2g0101010, marker='.',c=[0.0, 1.0, 1.0],ls='--',label='$\\ell=2,N=100$', markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0101020, marker='.',c=[0.0, 1.0, 1.0],ls='--',label='$\\ell=2,N=200$', markeredgecolor=[1.0, 1.0, 0.0,1.0], markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0101030, marker='.',c=[0.0, 1.0, 1.0],ls='--',label='$\\ell=2,N=300$', markeredgecolor=[0.0, 1.0, 0.0,1.0], markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0101040, marker='.',c=[0.0, 1.0, 1.0],ls='--',label='$\\ell=2,N=400$', markeredgecolor=[0.0, 1.0, 1.0,1.0], markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0101050, marker='.',c=[0.0, 1.0, 1.0],ls='--',label='$\\ell=2,N=500$', markeredgecolor=[0.0, 0.0, 1.0,1.0], markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0101Inf, marker='.',c=[0.0, 1.0, 1.0],ls='--',label='$\\ell=2,N=\\infty$', markeredgecolor=[1.0, 0.0, 1.0,1.0], markersize=3)#,label='100')

#plt.xlim(left  =0)
#plt.ylim(bottom=0)
plt.xticks([0.01,0.02,0.05,0.10,0.20])
#plt.yticks(np.arange(0.984,+1.004, step=0.002))
#plt.show()

plt.legend(bbox_to_anchor=(0.85, 1.0), loc=2, borderaxespad=0.)
plt.suptitle('$g_{\\mathcal{K}}= 0.10$' ,fontsize=20, fontname='Times New Roman')

plt.xlabel('$a_{\\mathcal{K}}$')
plt.ylabel('$\\mathrm{Max}\\{\\mathrm{Im}[E]\\}$')

#plt.savefig('PlotsGlobalg010.pdf')

########################################################################
########################################################################

plt.clf()
plt.figure(figsize=(8,8))
plt.subplots_adjust(left=0.12,bottom=0.11,right=0.79,top=0.94)
#plt.plot(MomentumAxL2g20,Renormalization,'o')

plt.plot(Coupling,[MaxEigenValImL0g0011010[0],MaxEigenValImL0g0021010[0],MaxEigenValImL0g0051010[0],MaxEigenValImL0g0101010[0]], marker='s',c=[1.0, 0.0, 0.0],ls='-',label='$\\ell=0,N=100$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011020[0],MaxEigenValImL0g0021020[0],MaxEigenValImL0g0051020[0],MaxEigenValImL0g0101020[0]], marker='s',c=[1.0, 1.0, 0.0],ls='-',label='$\\ell=0,N=200$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011030[0],MaxEigenValImL0g0021030[0],MaxEigenValImL0g0051030[0],MaxEigenValImL0g0101030[0]], marker='s',c=[0.0, 1.0, 0.0],ls='-',label='$\\ell=0,N=300$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011040[0],MaxEigenValImL0g0021040[0],MaxEigenValImL0g0051040[0],MaxEigenValImL0g0101040[0]], marker='s',c=[0.0, 1.0, 1.0],ls='-',label='$\\ell=0,N=400$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011050[0],MaxEigenValImL0g0021050[0],MaxEigenValImL0g0051050[0],MaxEigenValImL0g0101050[0]], marker='s',c=[0.0, 0.0, 1.0],ls='-',label='$\\ell=0,N=500$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011Inf[0],MaxEigenValImL0g0021Inf[0],MaxEigenValImL0g0051Inf[0],MaxEigenValImL0g0101Inf[0]], marker='s',c=[1.0, 0.0, 1.0],ls='-',label='$\\ell=0,N=\\infty$', markersize=5)#,label='100')

plt.plot(Coupling,[MaxEigenValImL2g0011010[0],MaxEigenValImL2g0021010[0],MaxEigenValImL2g0051010[0],MaxEigenValImL2g0101010[0]], marker='o',c=[1.0, 0.0, 0.0],ls='--',label='$\\ell=2,N=100$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011020[0],MaxEigenValImL2g0021020[0],MaxEigenValImL2g0051020[0],MaxEigenValImL2g0101020[0]], marker='o',c=[1.0, 1.0, 0.0],ls='--',label='$\\ell=2,N=200$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011030[0],MaxEigenValImL2g0021030[0],MaxEigenValImL2g0051030[0],MaxEigenValImL2g0101030[0]], marker='o',c=[0.0, 1.0, 0.0],ls='--',label='$\\ell=2,N=300$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011040[0],MaxEigenValImL2g0021040[0],MaxEigenValImL2g0051040[0],MaxEigenValImL2g0101040[0]], marker='o',c=[0.0, 1.0, 1.0],ls='--',label='$\\ell=2,N=400$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011050[0],MaxEigenValImL2g0021050[0],MaxEigenValImL2g0051050[0],MaxEigenValImL2g0101050[0]], marker='o',c=[0.0, 0.0, 1.0],ls='--',label='$\\ell=2,N=500$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011Inf[0],MaxEigenValImL2g0021Inf[0],MaxEigenValImL2g0051Inf[0],MaxEigenValImL2g0101Inf[0]], marker='o',c=[1.0, 0.0, 1.0],ls='--',label='$\\ell=2,N=\\infty$', markersize=5)#,label='100')

#plt.xlim(left  =0)
#plt.ylim(bottom=0)
plt.xticks([0.01,0.02,0.05,0.10])
#plt.yticks(np.arange(0.984,+1.004, step=0.002))
#plt.show()

plt.legend(bbox_to_anchor=(1.0, 1.0), loc=2, borderaxespad=0.)
plt.suptitle('$a_{\\mathcal{K}}= 0.01$' ,fontsize=20, fontname='Times New Roman')

plt.xlabel('$g_{\\mathcal{K}}$')
plt.ylabel('$\\mathrm{Max}\\{\\mathrm{Im}[E]\\}$')

#plt.savefig('PlotsGlobala001.pdf')

########################################################################
########################################################################

plt.clf()
plt.figure(figsize=(8,8))
plt.subplots_adjust(left=0.12,bottom=0.11,right=0.79,top=0.94)
#plt.plot(MomentumAxL2g20,Renormalization,'o')

plt.plot(Coupling,[MaxEigenValImL0g0011010[1],MaxEigenValImL0g0021010[1],MaxEigenValImL0g0051010[1],MaxEigenValImL0g0101010[1]], marker='s',c=[1.0, 0.0, 0.0],ls='-',label='$\\ell=0,N=100$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011020[1],MaxEigenValImL0g0021020[1],MaxEigenValImL0g0051020[1],MaxEigenValImL0g0101020[1]], marker='s',c=[1.0, 1.0, 0.0],ls='-',label='$\\ell=0,N=200$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011030[1],MaxEigenValImL0g0021030[1],MaxEigenValImL0g0051030[1],MaxEigenValImL0g0101030[1]], marker='s',c=[0.0, 1.0, 0.0],ls='-',label='$\\ell=0,N=300$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011040[1],MaxEigenValImL0g0021040[1],MaxEigenValImL0g0051040[1],MaxEigenValImL0g0101040[1]], marker='s',c=[0.0, 1.0, 1.0],ls='-',label='$\\ell=0,N=400$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011050[1],MaxEigenValImL0g0021050[1],MaxEigenValImL0g0051050[1],MaxEigenValImL0g0101050[1]], marker='s',c=[0.0, 0.0, 1.0],ls='-',label='$\\ell=0,N=500$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011Inf[1],MaxEigenValImL0g0021Inf[1],MaxEigenValImL0g0051Inf[1],MaxEigenValImL0g0101Inf[1]], marker='s',c=[1.0, 0.0, 1.0],ls='-',label='$\\ell=0,N=\\infty$', markersize=5)#,label='100')

plt.plot(Coupling,[MaxEigenValImL2g0011010[1],MaxEigenValImL2g0021010[1],MaxEigenValImL2g0051010[1],MaxEigenValImL2g0101010[1]], marker='o',c=[1.0, 0.0, 0.0],ls='--',label='$\\ell=2,N=100$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011020[1],MaxEigenValImL2g0021020[1],MaxEigenValImL2g0051020[1],MaxEigenValImL2g0101020[1]], marker='o',c=[1.0, 1.0, 0.0],ls='--',label='$\\ell=2,N=200$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011030[1],MaxEigenValImL2g0021030[1],MaxEigenValImL2g0051030[1],MaxEigenValImL2g0101030[1]], marker='o',c=[0.0, 1.0, 0.0],ls='--',label='$\\ell=2,N=300$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011040[1],MaxEigenValImL2g0021040[1],MaxEigenValImL2g0051040[1],MaxEigenValImL2g0101040[1]], marker='o',c=[0.0, 1.0, 1.0],ls='--',label='$\\ell=2,N=400$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011050[1],MaxEigenValImL2g0021050[1],MaxEigenValImL2g0051050[1],MaxEigenValImL2g0101050[1]], marker='o',c=[0.0, 0.0, 1.0],ls='--',label='$\\ell=2,N=500$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011Inf[1],MaxEigenValImL2g0021Inf[1],MaxEigenValImL2g0051Inf[1],MaxEigenValImL2g0101Inf[1]], marker='o',c=[1.0, 0.0, 1.0],ls='--',label='$\\ell=2,N=\\infty$', markersize=5)#,label='100')

#plt.xlim(left  =0)
#plt.ylim(bottom=0)
plt.xticks([0.01,0.02,0.05,0.10])
#plt.yticks(np.arange(0.984,+1.004, step=0.002))
#plt.show()

plt.legend(bbox_to_anchor=(1.0, 1.0), loc=2, borderaxespad=0.)
plt.suptitle('$a_{\\mathcal{K}}= 0.02$' ,fontsize=20, fontname='Times New Roman')

plt.xlabel('$g_{\\mathcal{K}}$')
plt.ylabel('$\\mathrm{Max}\\{\\mathrm{Im}[E]\\}$')

#plt.savefig('PlotsGlobala002.pdf')

########################################################################
########################################################################

plt.clf()
plt.figure(figsize=(8,8))
plt.subplots_adjust(left=0.12,bottom=0.11,right=0.79,top=0.94)
#plt.plot(MomentumAxL2g20,Renormalization,'o')

plt.plot(Coupling,[MaxEigenValImL0g0011010[2],MaxEigenValImL0g0021010[2],MaxEigenValImL0g0051010[2],MaxEigenValImL0g0101010[2]], marker='s',c=[1.0, 0.0, 0.0],ls='-',label='$\\ell=0,N=100$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011020[2],MaxEigenValImL0g0021020[2],MaxEigenValImL0g0051020[2],MaxEigenValImL0g0101020[2]], marker='s',c=[1.0, 1.0, 0.0],ls='-',label='$\\ell=0,N=200$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011030[2],MaxEigenValImL0g0021030[2],MaxEigenValImL0g0051030[2],MaxEigenValImL0g0101030[2]], marker='s',c=[0.0, 1.0, 0.0],ls='-',label='$\\ell=0,N=300$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011040[2],MaxEigenValImL0g0021040[2],MaxEigenValImL0g0051040[2],MaxEigenValImL0g0101040[2]], marker='s',c=[0.0, 1.0, 1.0],ls='-',label='$\\ell=0,N=400$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011050[2],MaxEigenValImL0g0021050[2],MaxEigenValImL0g0051050[2],MaxEigenValImL0g0101050[2]], marker='s',c=[0.0, 0.0, 1.0],ls='-',label='$\\ell=0,N=500$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011Inf[2],MaxEigenValImL0g0021Inf[2],MaxEigenValImL0g0051Inf[2],MaxEigenValImL0g0101Inf[2]], marker='s',c=[1.0, 0.0, 1.0],ls='-',label='$\\ell=0,N=\\infty$', markersize=5)#,label='100')

plt.plot(Coupling,[MaxEigenValImL2g0011010[2],MaxEigenValImL2g0021010[2],MaxEigenValImL2g0051010[2],MaxEigenValImL2g0101010[2]], marker='o',c=[1.0, 0.0, 0.0],ls='--',label='$\\ell=2,N=100$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011020[2],MaxEigenValImL2g0021020[2],MaxEigenValImL2g0051020[2],MaxEigenValImL2g0101020[2]], marker='o',c=[1.0, 1.0, 0.0],ls='--',label='$\\ell=2,N=200$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011030[2],MaxEigenValImL2g0021030[2],MaxEigenValImL2g0051030[2],MaxEigenValImL2g0101030[2]], marker='o',c=[0.0, 1.0, 0.0],ls='--',label='$\\ell=2,N=300$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011040[2],MaxEigenValImL2g0021040[2],MaxEigenValImL2g0051040[2],MaxEigenValImL2g0101040[2]], marker='o',c=[0.0, 1.0, 1.0],ls='--',label='$\\ell=2,N=400$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011050[2],MaxEigenValImL2g0021050[2],MaxEigenValImL2g0051050[2],MaxEigenValImL2g0101050[2]], marker='o',c=[0.0, 0.0, 1.0],ls='--',label='$\\ell=2,N=500$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011Inf[2],MaxEigenValImL2g0021Inf[2],MaxEigenValImL2g0051Inf[2],MaxEigenValImL2g0101Inf[2]], marker='o',c=[1.0, 0.0, 1.0],ls='--',label='$\\ell=2,N=\\infty$', markersize=5)#,label='100')

#plt.xlim(left  =0)
#plt.ylim(bottom=0)
plt.xticks([0.01,0.02,0.05,0.10])
#plt.yticks(np.arange(0.984,+1.004, step=0.002))
#plt.show()

plt.legend(bbox_to_anchor=(1.0, 1.0), loc=2, borderaxespad=0.)
plt.suptitle('$a_{\\mathcal{K}}= 0.05$' ,fontsize=20, fontname='Times New Roman')

plt.xlabel('$g_{\\mathcal{K}}$')
plt.ylabel('$\\mathrm{Max}\\{\\mathrm{Im}[E]\\}$')

#plt.savefig('PlotsGlobala005.pdf')

########################################################################
########################################################################

plt.clf()
plt.figure(figsize=(8,8))
plt.subplots_adjust(left=0.12,bottom=0.11,right=0.79,top=0.94)
#plt.plot(MomentumAxL2g20,Renormalization,'o')

plt.plot(Coupling,[MaxEigenValImL0g0011010[3],MaxEigenValImL0g0021010[3],MaxEigenValImL0g0051010[3],MaxEigenValImL0g0101010[3]], marker='s',c=[1.0, 0.0, 0.0],ls='-',label='$\\ell=0,N=100$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011020[3],MaxEigenValImL0g0021020[3],MaxEigenValImL0g0051020[3],MaxEigenValImL0g0101020[3]], marker='s',c=[1.0, 1.0, 0.0],ls='-',label='$\\ell=0,N=200$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011030[3],MaxEigenValImL0g0021030[3],MaxEigenValImL0g0051030[3],MaxEigenValImL0g0101030[3]], marker='s',c=[0.0, 1.0, 0.0],ls='-',label='$\\ell=0,N=300$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011040[3],MaxEigenValImL0g0021040[3],MaxEigenValImL0g0051040[3],MaxEigenValImL0g0101040[3]], marker='s',c=[0.0, 1.0, 1.0],ls='-',label='$\\ell=0,N=400$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011050[3],MaxEigenValImL0g0021050[3],MaxEigenValImL0g0051050[3],MaxEigenValImL0g0101050[3]], marker='s',c=[0.0, 0.0, 1.0],ls='-',label='$\\ell=0,N=500$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011Inf[3],MaxEigenValImL0g0021Inf[3],MaxEigenValImL0g0051Inf[3],MaxEigenValImL0g0101Inf[3]], marker='s',c=[1.0, 0.0, 1.0],ls='-',label='$\\ell=0,N=\\infty$', markersize=5)#,label='100')

plt.plot(Coupling,[MaxEigenValImL2g0011010[3],MaxEigenValImL2g0021010[3],MaxEigenValImL2g0051010[3],MaxEigenValImL2g0101010[3]], marker='o',c=[1.0, 0.0, 0.0],ls='--',label='$\\ell=2,N=100$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011020[3],MaxEigenValImL2g0021020[3],MaxEigenValImL2g0051020[3],MaxEigenValImL2g0101020[3]], marker='o',c=[1.0, 1.0, 0.0],ls='--',label='$\\ell=2,N=200$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011030[3],MaxEigenValImL2g0021030[3],MaxEigenValImL2g0051030[3],MaxEigenValImL2g0101030[3]], marker='o',c=[0.0, 1.0, 0.0],ls='--',label='$\\ell=2,N=300$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011040[3],MaxEigenValImL2g0021040[3],MaxEigenValImL2g0051040[3],MaxEigenValImL2g0101040[3]], marker='o',c=[0.0, 1.0, 1.0],ls='--',label='$\\ell=2,N=400$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011050[3],MaxEigenValImL2g0021050[3],MaxEigenValImL2g0051050[3],MaxEigenValImL2g0101050[3]], marker='o',c=[0.0, 0.0, 1.0],ls='--',label='$\\ell=2,N=500$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011Inf[3],MaxEigenValImL2g0021Inf[3],MaxEigenValImL2g0051Inf[3],MaxEigenValImL2g0101Inf[3]], marker='o',c=[1.0, 0.0, 1.0],ls='--',label='$\\ell=2,N=\\infty$', markersize=5)#,label='100')

#plt.xlim(left  =0)
#plt.ylim(bottom=0)
plt.xticks([0.01,0.02,0.05,0.10])
#plt.yticks(np.arange(0.984,+1.004, step=0.002))
#plt.show()

plt.legend(bbox_to_anchor=(1.0, 1.0), loc=2, borderaxespad=0.)
plt.suptitle('$a_{\\mathcal{K}}= 0.10$' ,fontsize=20, fontname='Times New Roman')

plt.xlabel('$g_{\\mathcal{K}}$')
plt.ylabel('$\\mathrm{Max}\\{\\mathrm{Im}[E]\\}$')

#plt.savefig('PlotsGlobala010.pdf')

########################################################################
########################################################################

plt.clf()
plt.figure(figsize=(8,8))
plt.subplots_adjust(left=0.12,bottom=0.11,right=0.79,top=0.94)
#plt.plot(MomentumAxL2g20,Renormalization,'o')

plt.plot(Coupling,[MaxEigenValImL0g0011010[4],MaxEigenValImL0g0021010[4],MaxEigenValImL0g0051010[4],MaxEigenValImL0g0101010[4]], marker='s',c=[1.0, 0.0, 0.0],ls='-',label='$\\ell=0,N=100$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011020[4],MaxEigenValImL0g0021020[4],MaxEigenValImL0g0051020[4],MaxEigenValImL0g0101020[4]], marker='s',c=[1.0, 1.0, 0.0],ls='-',label='$\\ell=0,N=200$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011030[4],MaxEigenValImL0g0021030[4],MaxEigenValImL0g0051030[4],MaxEigenValImL0g0101030[4]], marker='s',c=[0.0, 1.0, 0.0],ls='-',label='$\\ell=0,N=300$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011040[4],MaxEigenValImL0g0021040[4],MaxEigenValImL0g0051040[4],MaxEigenValImL0g0101040[4]], marker='s',c=[0.0, 1.0, 1.0],ls='-',label='$\\ell=0,N=400$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011050[4],MaxEigenValImL0g0021050[4],MaxEigenValImL0g0051050[4],MaxEigenValImL0g0101050[4]], marker='s',c=[0.0, 0.0, 1.0],ls='-',label='$\\ell=0,N=500$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011Inf[4],MaxEigenValImL0g0021Inf[4],MaxEigenValImL0g0051Inf[4],MaxEigenValImL0g0101Inf[4]], marker='s',c=[1.0, 0.0, 1.0],ls='-',label='$\\ell=0,N=\\infty$', markersize=5)#,label='100')

plt.plot(Coupling,[MaxEigenValImL2g0011010[4],MaxEigenValImL2g0021010[4],MaxEigenValImL2g0051010[4],MaxEigenValImL2g0101010[4]], marker='o',c=[1.0, 0.0, 0.0],ls='--',label='$\\ell=2,N=100$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011020[4],MaxEigenValImL2g0021020[4],MaxEigenValImL2g0051020[4],MaxEigenValImL2g0101020[4]], marker='o',c=[1.0, 1.0, 0.0],ls='--',label='$\\ell=2,N=200$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011030[4],MaxEigenValImL2g0021030[4],MaxEigenValImL2g0051030[4],MaxEigenValImL2g0101030[4]], marker='o',c=[0.0, 1.0, 0.0],ls='--',label='$\\ell=2,N=300$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011040[4],MaxEigenValImL2g0021040[4],MaxEigenValImL2g0051040[4],MaxEigenValImL2g0101040[4]], marker='o',c=[0.0, 1.0, 1.0],ls='--',label='$\\ell=2,N=400$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011050[4],MaxEigenValImL2g0021050[4],MaxEigenValImL2g0051050[4],MaxEigenValImL2g0101050[4]], marker='o',c=[0.0, 0.0, 1.0],ls='--',label='$\\ell=2,N=500$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011Inf[4],MaxEigenValImL2g0021Inf[4],MaxEigenValImL2g0051Inf[4],MaxEigenValImL2g0101Inf[4]], marker='o',c=[1.0, 0.0, 1.0],ls='--',label='$\\ell=2,N=\\infty$', markersize=5)#,label='100')

#plt.xlim(left  =0)
#plt.ylim(bottom=0)
plt.xticks([0.01,0.02,0.05,0.10])
#plt.yticks(np.arange(0.984,+1.004, step=0.002))
#plt.show()

plt.legend(bbox_to_anchor=(1.0, 1.0), loc=2, borderaxespad=0.)
plt.suptitle('$a_{\\mathcal{K}}= 0.20$' ,fontsize=20, fontname='Times New Roman')

plt.xlabel('$g_{\\mathcal{K}}$')
plt.ylabel('$\\mathrm{Max}\\{\\mathrm{Im}[E]\\}$')

#plt.savefig('PlotsGlobala020.pdf')

########################################################################
########################################################################

plt.clf()
plt.figure(figsize=(8,8))
plt.subplots_adjust(left=0.12,bottom=0.11,right=0.79,top=0.94)
#plt.plot(MomentumAxL2g20,Renormalization,'o')

plt.plot(Spreading,MaxEigenValImL0g0101010-MaxEigenValImL0g0101010, marker='*',c=[0.0, 1.0, 1.0],ls='-',label='$\\ell=0,N=100$', markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0101020-MaxEigenValImL0g0101010, marker='*',c=[0.0, 1.0, 1.0],ls='-',label='$\\ell=0,N=200$', markeredgecolor=[1.0, 1.0, 0.0,1.0], markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0101030-MaxEigenValImL0g0101010, marker='*',c=[0.0, 1.0, 1.0],ls='-',label='$\\ell=0,N=300$', markeredgecolor=[0.0, 1.0, 0.0,1.0], markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0101040-MaxEigenValImL0g0101010, marker='*',c=[0.0, 1.0, 1.0],ls='-',label='$\\ell=0,N=400$', markeredgecolor=[0.0, 1.0, 1.0,1.0], markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0101050-MaxEigenValImL0g0101010, marker='*',c=[0.0, 1.0, 1.0],ls='-',label='$\\ell=0,N=500$', markeredgecolor=[0.0, 0.0, 1.0,1.0], markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL0g0101Inf-MaxEigenValImL0g0101010, marker='*',c=[0.0, 1.0, 1.0],ls='-',label='$\\ell=0,N=\\infty$', markeredgecolor=[0.0, 0.0, 1.0,1.0], markersize=3)#,label='100')

plt.plot(Spreading,MaxEigenValImL2g0101010-MaxEigenValImL2g0101010, marker='.',c=[0.0, 1.0, 1.0],ls='--',label='$\\ell=2,N=100$', markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0101020-MaxEigenValImL2g0101010, marker='.',c=[0.0, 1.0, 1.0],ls='--',label='$\\ell=2,N=200$', markeredgecolor=[1.0, 1.0, 0.0,1.0], markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0101030-MaxEigenValImL2g0101010, marker='.',c=[0.0, 1.0, 1.0],ls='--',label='$\\ell=2,N=300$', markeredgecolor=[0.0, 1.0, 0.0,1.0], markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0101040-MaxEigenValImL2g0101010, marker='.',c=[0.0, 1.0, 1.0],ls='--',label='$\\ell=2,N=400$', markeredgecolor=[0.0, 1.0, 1.0,1.0], markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0101050-MaxEigenValImL2g0101010, marker='.',c=[0.0, 1.0, 1.0],ls='--',label='$\\ell=2,N=500$', markeredgecolor=[0.0, 0.0, 1.0,1.0], markersize=3)#,label='100')
plt.plot(Spreading,MaxEigenValImL2g0101Inf-MaxEigenValImL2g0101010, marker='.',c=[0.0, 1.0, 1.0],ls='--',label='$\\ell=2,N=\\infty$', markeredgecolor=[0.0, 0.0, 1.0,1.0], markersize=3)#,label='100')

#plt.xlim(left  =0)
#plt.ylim(bottom=0)
plt.xticks([0.01,0.02,0.05,0.10,0.20])
#plt.yticks(np.arange(0.984,+1.004, step=0.002))
#plt.show()

plt.legend(bbox_to_anchor=(0.85, 1.0), loc=2, borderaxespad=0.)
plt.suptitle('$g_{\\mathcal{K}}= 0.10$' ,fontsize=20, fontname='Times New Roman')

#plt.savefig('ZZZ-PlotsGlobalg010.pdf')

########################################################################
########################################################################

plt.clf()
plt.figure(figsize=(8,8))
plt.subplots_adjust(left=0.12,bottom=0.11,right=0.79,top=0.94)
#plt.plot(MomentumAxL2g20,Renormalization,'o')

plt.plot(Coupling,[MaxEigenValImL0g0011010[0]-MaxEigenValImL0g0011010[0],MaxEigenValImL0g0021010[0]-MaxEigenValImL0g0021010[0],MaxEigenValImL0g0051010[0]-MaxEigenValImL0g0051010[0],MaxEigenValImL0g0101010[0]-MaxEigenValImL0g0101010[0]], marker='*',c=[1.0, 0.0, 0.0],ls='-',label='$\\ell=0,N=100$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011020[0]-MaxEigenValImL0g0011010[0],MaxEigenValImL0g0021020[0]-MaxEigenValImL0g0021010[0],MaxEigenValImL0g0051020[0]-MaxEigenValImL0g0051010[0],MaxEigenValImL0g0101020[0]-MaxEigenValImL0g0101010[0]], marker='*',c=[1.0, 0.0, 0.0],ls='-',label='$\\ell=0,N=200$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011030[0]-MaxEigenValImL0g0011010[0],MaxEigenValImL0g0021030[0]-MaxEigenValImL0g0021010[0],MaxEigenValImL0g0051030[0]-MaxEigenValImL0g0051010[0],MaxEigenValImL0g0101030[0]-MaxEigenValImL0g0101010[0]], marker='*',c=[1.0, 0.0, 0.0],ls='-',label='$\\ell=0,N=300$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011040[0]-MaxEigenValImL0g0011010[0],MaxEigenValImL0g0021040[0]-MaxEigenValImL0g0021010[0],MaxEigenValImL0g0051040[0]-MaxEigenValImL0g0051010[0],MaxEigenValImL0g0101040[0]-MaxEigenValImL0g0101010[0]], marker='*',c=[1.0, 0.0, 0.0],ls='-',label='$\\ell=0,N=400$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL0g0011050[0]-MaxEigenValImL0g0011010[0],MaxEigenValImL0g0021050[0]-MaxEigenValImL0g0021010[0],MaxEigenValImL0g0051050[0]-MaxEigenValImL0g0051010[0],MaxEigenValImL0g0101050[0]-MaxEigenValImL0g0101010[0]], marker='*',c=[1.0, 0.0, 0.0],ls='-',label='$\\ell=0,N=500$', markersize=5)#,label='100')

plt.plot(Coupling,[MaxEigenValImL2g0011010[0]-MaxEigenValImL2g0011010[0],MaxEigenValImL2g0021010[0]-MaxEigenValImL2g0021010[0],MaxEigenValImL2g0051010[0]-MaxEigenValImL2g0051010[0],MaxEigenValImL2g0101010[0]-MaxEigenValImL2g0101010[0]], marker='o',c=[1.0, 0.0, 0.0],ls='--',label='$\\ell=2,N=100$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011020[0]-MaxEigenValImL2g0011010[0],MaxEigenValImL2g0021020[0]-MaxEigenValImL2g0021010[0],MaxEigenValImL2g0051020[0]-MaxEigenValImL2g0051010[0],MaxEigenValImL2g0101020[0]-MaxEigenValImL2g0101010[0]], marker='o',c=[1.0, 0.0, 0.0],ls='--',label='$\\ell=2,N=200$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011030[0]-MaxEigenValImL2g0011010[0],MaxEigenValImL2g0021030[0]-MaxEigenValImL2g0021010[0],MaxEigenValImL2g0051030[0]-MaxEigenValImL2g0051010[0],MaxEigenValImL2g0101030[0]-MaxEigenValImL2g0101010[0]], marker='o',c=[1.0, 0.0, 0.0],ls='--',label='$\\ell=2,N=300$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011040[0]-MaxEigenValImL2g0011010[0],MaxEigenValImL2g0021040[0]-MaxEigenValImL2g0021010[0],MaxEigenValImL2g0051040[0]-MaxEigenValImL2g0051010[0],MaxEigenValImL2g0101040[0]-MaxEigenValImL2g0101010[0]], marker='o',c=[1.0, 0.0, 0.0],ls='--',label='$\\ell=2,N=400$', markersize=5)#,label='100')
plt.plot(Coupling,[MaxEigenValImL2g0011050[0]-MaxEigenValImL2g0011010[0],MaxEigenValImL2g0021050[0]-MaxEigenValImL2g0021010[0],MaxEigenValImL2g0051050[0]-MaxEigenValImL2g0051010[0],MaxEigenValImL2g0101050[0]-MaxEigenValImL2g0101010[0]], marker='o',c=[1.0, 0.0, 0.0],ls='--',label='$\\ell=2,N=500$', markersize=5)#,label='100')

#plt.xlim(left  =0)
#plt.ylim(bottom=0)
plt.xticks([0.01,0.02,0.05,0.10])
#plt.yticks(np.arange(0.984,+1.004, step=0.002))
#plt.show()

plt.legend(bbox_to_anchor=(1.0, 1.0), loc=2, borderaxespad=0.)
plt.suptitle('$a_{\\mathcal{K}}= 0.01$' ,fontsize=20, fontname='Times New Roman')

#plt.savefig('ZZZ-PlotsGlobala001.pdf')

########################################################################
########################################################################

plt.clf()
fig = plt.figure(figsize=(8,8))
#plt.subplots_adjust(left=0.12,bottom=0.11,right=0.79,top=0.94)
ax = fig.add_subplot(111,projection='3d')
#plt.plot(MomentumAxL2g20,Renormalization,'o')

BigCouplings = np.zeros((20))
BigSpreading = np.zeros((20))
BigImagPart0 = np.zeros((20))
BigImagPart2 = np.zeros((20))
i = 0

Couplings001 = np.zeros((5))
Couplings002 = np.zeros((5))
Couplings005 = np.zeros((5))
Couplings010 = np.zeros((5))

Spreading001 = np.zeros((5))
Spreading002 = np.zeros((5))
Spreading005 = np.zeros((5))
Spreading010 = np.zeros((5))
Spreading020 = np.zeros((5))

Couplings001 = [0.01,0.01,0.01,0.01,0.01]
Couplings002 = [0.02,0.02,0.02,0.02,0.02]
Couplings005 = [0.05,0.05,0.05,0.05,0.05]
Couplings010 = [0.10,0.10,0.10,0.10,0.10]

Spreading001 = [0.01,0.02,0.05,0.10,0.20]
Spreading002 = [0.02,0.02,0.02,0.02,0.02]
Spreading005 = [0.05,0.05,0.05,0.05,0.05]
Spreading010 = [0.10,0.10,0.10,0.10,0.10]
Spreading020 = [0.20,0.20,0.20,0.20,0.20]

for x in [0.01,0.02,0.05,0.10]:
    for y in [0.01,0.02,0.05,0.10,0.20]:
        BigCouplings[i] = x
        BigSpreading[i] = y
        i = i+1

x = 0
for y in range(0,5):
    BigImagPart0[5*x+y] = MaxEigenValImL0g0011050[y]
    BigImagPart2[5*x+y] = MaxEigenValImL2g0011050[y]
x = 1
for y in range(0,5):
    BigImagPart0[5*x+y] = MaxEigenValImL0g0021050[y]
    BigImagPart2[5*x+y] = MaxEigenValImL2g0021050[y]
x = 2
for y in range(0,5):
    BigImagPart0[5*x+y] = MaxEigenValImL0g0051050[y]
    BigImagPart2[5*x+y] = MaxEigenValImL2g0051050[y]
x = 3
for y in range(0,5):
    BigImagPart0[5*x+y] = MaxEigenValImL0g0101050[y]
    BigImagPart2[5*x+y] = MaxEigenValImL2g0101050[y]

ax.plot_trisurf(BigCouplings, BigSpreading, BigImagPart0)#, linewidth=0, antialiased=False)
#scatter(BigCouplings,BigSpreading,BigImagPartE,c='black',marker='o')

ax.plot_trisurf(BigCouplings, BigSpreading, BigImagPart2)#, linewidth=0, antialiased=False)

ax.scatter(Couplings001,Spreading001,MaxEigenValImL0g0011Inf,c='red',marker='o')
ax.scatter(Couplings002,Spreading001,MaxEigenValImL0g0021Inf,c='yellow',marker='o')
ax.scatter(Couplings005,Spreading001,MaxEigenValImL0g0051Inf,c='green',marker='o')
ax.scatter(Couplings010,Spreading001,MaxEigenValImL0g0101Inf,c='blue',marker='o')

ax.scatter(Couplings001,Spreading001,MaxEigenValImL2g0011Inf,c='red',marker='*')
ax.scatter(Couplings002,Spreading001,MaxEigenValImL2g0021Inf,c='yellow',marker='*')
ax.scatter(Couplings005,Spreading001,MaxEigenValImL2g0051Inf,c='green',marker='*')
ax.scatter(Couplings010,Spreading001,MaxEigenValImL2g0101Inf,c='blue',marker='*')

ax.set_xlabel('$g_{\\mathcal{K}}$')
ax.set_ylabel('$a_{\\mathcal{K}}$')
ax.set_zlabel('$\\mathrm{Max}\\{\\mathrm{Im}[E]\\}$')

#plt.savefig('ZZZ-3D.pdf')
plt.show()
