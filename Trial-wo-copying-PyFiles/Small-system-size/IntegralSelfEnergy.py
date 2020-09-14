#CALCULO DE BLOQUE DIAGONAL

import time 
start_time = time.time() 

import numpy as np
import scipy as scip 
import scipy.special as special
import random as rd
import matplotlib.pyplot as plt

from sympy import besseli, besselk

Parameters = np.genfromtxt('ParametersABLN.txt') 

eCharge = 1000/100.
eLayers = Parameters[1]
eMomAng = Parameters[2]
ThetaBins = int(Parameters[3]*100)
BloqueX = Parameters[4]
BloqueY = Parameters[5]

eLength = 1.
eSpeedF = 1.
eHoppin = 1.
nTan = 2

#eCharge = 1/137

#eCutOff = Parameters[2]# + 1.*1.e-1

DeltaThet = np.pi/2./(ThetaBins+1)

file1 = open("BloqueHopp.txt","w") 
    
print "You have ", ThetaBins, " bosons. "

def Momentum(m,nTan):
    return np.tan(m * DeltaThet)**nTan / eLength

def Function1(mm1,mm2,Phi,nTan):
    return np.sqrt( Momentum(mm1+.0,nTan)/Momentum(mm2,nTan) + Momentum(mm2+.0,nTan)/Momentum(mm1,nTan) - 2.*np.cos(Phi) )

def Function2(mm1,mm2,nTan):
    return np.sqrt( Momentum(mm1,nTan)*Momentum(mm2,nTan) )

def Interaction(bet,mm1,mm2,Phi,nTan):
    return - ( 1/( 4.*np.pi ) *
              ( np.exp( - eLength * Function2(mm1,mm2,nTan)*Function1(mm1,mm2,Phi,nTan) ) -
                np.exp( - eCutOff * Function2(mm1,mm2,nTan)*Function1(mm1,mm2,Phi,nTan) ) ) /
              Function1(mm1,mm2,Phi,nTan) * bet*(bet+np.cos(eLayers*Phi) )
              )

def HartreeFockCutOff(k):
    SelfInteraction = ( 0. + eCharge/4. * (
        besseli(0,0.5*k*eCutOff)*besselk(0,0.5*k*eCutOff) +
        besseli(1,0.5*k*eCutOff)*besselk(1,0.5*k*eCutOff) ) )
    return k*( 0. + eCharge/4. * (
            besseli(0,0.5*k*eCutOff)*besselk(0,0.5*k*eCutOff) +
            besseli(1,0.5*k*eCutOff)*besselk(1,0.5*k*eCutOff) ) )

def HartreeFock(k):
    SelfInteraction = ( 0. + eCharge/4. * (
        besseli(0,0.5*k*eLength)*besselk(0,0.5*k*eLength) +
        besseli(1,0.5*k*eLength)*besselk(1,0.5*k*eLength) ) )
    return k*( 0. + eCharge/4. * (            besseli(0,0.5*k*eLength)*besselk(0,0.5*k*eLength) +
            besseli(1,0.5*k*eLength)*besselk(1,0.5*k*eLength) ) )

def PotentialHF(k):
    SelfInteraction = ( 0. + eCharge/4. * (
        besseli(0,0.5*k*eLength)*besselk(0,0.5*k*eLength) +
        besseli(1,0.5*k*eLength)*besselk(1,0.5*k*eLength) ) )
    if (abs(SelfInteraction)>1e-10):
        return 1*( 0. + eCharge/4. * (
            besseli(0,0.5*k*eLength)*besselk(0,0.5*k*eLength) +
            besseli(1,0.5*k*eLength)*besselk(1,0.5*k*eLength) ) )
    else:
        return 1*( 0. ) + eCharge/2.

def OriginalPotential(k1,k2,th):
    Norm = np.sqrt(k1**2 + k2**2 - 2*k1*k2*np.cos(th))

def FourierTran(bet,mm1,mm2,nTan):
    a = 0.
    b = np.pi
    N = 10000
    x = np.linspace(a+(b-a)/(2*N), b-(b-a)/(2*N), N)
    fx = Interaction(bet,mm1,mm2,x,nTan) * np.cos(eMomAng*x)
    #fx = ( -1/4*np.pi()) * np.exp(- np.sqrt( Momentum(mm1)**2 + Momentum(mm2)**2 - 2*Momentum(mm1)*Momentum(mm2)*np.cos(Phi) ) ) / np.sqrt( Momentum(mm1)**2 + Momentum(mm2)**2 - 2*Momentum(mm1)*Momentum(mm2)*np.cos(Phi) ) * bet*(bet+np.cos(Phi) ) 
    area = np.sum(fx)*(b-a)/N
    #area = fx
    return area

def PrintArrays(Array,N):
    for m2 in range(0,N):
        print "%.4f" % Array[m2],#
        #print Array[m2],#
        print '\t',
    print '\n'
    return None

def GenHopping(bet,mm1,mm2,nTan):
    return ( eCharge * DeltaThet * FourierTran(bet,mm1,mm2,nTan) * 
            np.sqrt( nTan**2 * np.tan(mm1*DeltaThet)**nTan *np.tan(mm2*DeltaThet)**nTan/(
                np.cos(mm1*DeltaThet)*np.cos(mm2*DeltaThet)*np.sin(mm1*DeltaThet)*np.sin(mm2*DeltaThet)
                ) ) 
            )





MomentumAxis = np.zeros((2*ThetaBins))
PotentialAxis = np.zeros((2*ThetaBins))
#m1Indices = np.zeros((2*ThetaBins))
SelfEnergy = np.zeros((2*ThetaBins))
#ScaleFactor = np.zeros((2*ThetaBins))
#Ham = np.zeros((2*ThetaBins,2*ThetaBins))


for m1 in range(0,ThetaBins): 
    if(m1%50==0):
        print "You have ", m1, " bosons. "
    mm1 = m1 + 1 + ThetaBins*BloqueX
    MomentumAxis[ThetaBins-m1-1] = -Momentum(mm1,nTan)
    #m1Indices[ThetaBins-m1-1] = -mm1
    #ScaleFactor[m1] = +np.sqrt( nTan * np.tan( mm1*DeltaThet )**(2*nTan-1) ) / np.cos( mm1*DeltaThet ) / eLength
    #m1Indices[ThetaBins-m1-1] = -m1-1
    PotentialAxis[ThetaBins-m1-1] = - ( 0*Momentum(mm1,nTan) + HartreeFock(Momentum(mm1,nTan)) )
    SelfEnergy[ThetaBins-m1-1] = - ( Momentum(mm1,nTan) + HartreeFock(Momentum(mm1,nTan)) )
    #print "      m1 = ", m1, "       Mom = ", MomentumAxis[ThetaBins-m1-1], "     , Sigma = ", SelfEnergy[ThetaBins-m1-1]
for m1 in range(0,ThetaBins): 
    if(m1%50==0):
        print "You have ", m1, " bosons. "
    mm1 = m1 + 1 + ThetaBins*BloqueX
    MomentumAxis[ThetaBins+m1] = Momentum(mm1,nTan)
    #m1Indices[ThetaBins-m1-1] = -mm1
    #ScaleFactor[m1] = +np.sqrt( nTan * np.tan( mm1*DeltaThet )**(2*nTan-1) ) / np.cos( mm1*DeltaThet ) / eLength
    #m1Indices[ThetaBins-m1-1] = -m1-1
    PotentialAxis[ThetaBins+m1] = ( 0*Momentum(mm1,nTan) + HartreeFock(Momentum(mm1,nTan)) )
    SelfEnergy[ThetaBins+m1] = ( Momentum(mm1,nTan) + HartreeFock(Momentum(mm1,nTan)) )


plt.clf()
plt.figure(figsize=(10,10))
plt.loglog(MomentumAxis,SelfEnergy)
plt.loglog(MomentumAxis,PotentialAxis)
plt.loglog(MomentumAxis,MomentumAxis)
plt.xlim(1e-4,1e+4)
plt.ylim(1e-4,1e+4)
plt.show()

#CONSTRUCCION DE LOS ELEMENTOS DE MATRIZ DEL BLOQUE

"""
for m1 in range(0,ThetaBins): 
    mm1 = m1 + 1 + ThetaBins*BloqueX
    #if ( ThetaBins>20 ):
    #    if (m1%(ThetaBins/20) )==0:
    #        print "\tFila m1 = ", m1
    
    #MomentumAxis[ThetaBins-m1-1] = -Momentum(mm1,nTan)
    #m1Indices[ThetaBins-m1-1] = -mm1
    #ScaleFactor[m1] = +np.sqrt( nTan * np.tan( mm1*DeltaThet )**(2*nTan-1) ) / np.cos( mm1*DeltaThet ) / eLength
    #m1Indices[ThetaBins-m1-1] = -m1-1
    #PotentialAxis[ThetaBins-m1-1] = - ( PotentialHF(Momentum(mm1,nTan)) - PotentialHFCutOff(Momentum(mm1,nTan)) )
    #SelfEnergy[ThetaBins-m1-1] = - ( Momentum(mm1,nTan) + HartreeFock(Momentum(mm1,nTan)) - HartreeFockCutOff(Momentum(mm1,nTan)) )
    
    for m2 in range(0,ThetaBins):
        mm2 = m2 + 1 + ThetaBins*BloqueY
        if mm1==mm2:
            #Ham[m1,m1] = rd.uniform(-30,30)
            #Ham[m1,m1] = HartreeFock(Momentum(mm1))
            #Ham[m1,m1] = GenHopping(1,mm1,mm1)
            Ham = float(Momentum(mm1,nTan) + HartreeFock(Momentum(mm1,nTan)) - HartreeFockCutOff(Momentum(mm1,nTan)))
            #-SelfEnergy[ThetaBins-m1-1]# + GenHopping(1,mm1,mm2,nTan)
        else:
            #Ham[m1,m2] = rd.uniform(-2,2)
            #Ham[m1,m2] = rd.uniform(-2,2)
            Ham = GenHopping(1,mm1,mm2,nTan)
            #print "(m1,m2) = (", m1, ",", m2, "): ", GenHopping(1,mm1,mm2,nTan,eLength), GenHopping(1,mm1,mm2,nTan,eCutOff), GenHopping(1,mm1,mm2,nTan,eLength)- GenHopping(1,mm1,mm2,nTan,eCutOff)
            #Ham[m1,m2] = 0
        file1.write("%s" % (mm1 - 1)),
        file1.write("\t"),
        file1.write("%s" % (mm2 - 1)),
        file1.write("\t"),
        file1.write("%s" % (Ham))
        file1.write('\n'),


print "Fin"

print("--- %s seconds ---" % (time.time() - start_time))

print (time.time() - start_time)  

file2 = open("Time.txt","a") 
file2.write("%s" % ( ThetaBins )),
file2.write("\t"),
file2.write("%s" % ( time.time() - start_time )),
file2.write('\n'),
file2.close() 
"""
