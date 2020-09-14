#CALCULO DE BLOQUE DIAGONAL

BloqueX = 0
BloqueY = 0

import time 
start_time = time.time() 

import numpy as np
import scipy as scip 
import scipy.special as special
import random as rd
#import matplotlib.pyplot as plt

Parameters = np.genfromtxt('Parameters.txt')

#ThetaBins = input("Enter number of bosons: ")
#ThetaBins = 300#
file1 = open("BloqueHopp00.txt","w")
    
eCharge = Parameters[0]
BiLayer = Parameters[1]
eAngMom = Parameters[2]
ThetaBins = int(Parameters[3]/5)
#eCharge = 1/137


eLength = 1.
#eCutOff = Parameters[2]# + 1.*1.e-1
eEfMass = 1.
eHoppin = 1.
nTan = 2

DeltaThet = np.pi/2./(ThetaBins*5+1)

from sympy import besseli, besselk

def Momentum(m,nTan):
    return np.tan(m * DeltaThet)**nTan / eLength

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
    return k*( 0. + eCharge/4. * (
            besseli(0,0.5*k*eLength)*besselk(0,0.5*k*eLength) +
            besseli(1,0.5*k*eLength)*besselk(1,0.5*k*eLength) ) )

def PotentialHFCutOff(k):
    SelfInteraction = ( 0. + eCharge/4. * (
        besseli(0,0.5*k*eCutOff)*besselk(0,0.5*k*eCutOff) +
        besseli(1,0.5*k*eCutOff)*besselk(1,0.5*k*eCutOff) ) )
    if (abs(SelfInteraction)>1e-10):
        return 0*( 0. + eCharge/4. * (
            besseli(0,0.5*k*eCutOff)*besselk(0,0.5*k*eCutOff) +
            besseli(1,0.5*k*eCutOff)*besselk(1,0.5*k*eCutOff) ) )
    else:
        return 0*( 0. ) + eCharge/2.*0

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

def Function1(mm1,mm2,Phi,nTan,BiLayer):
    return np.sqrt( Momentum(mm1+.0,nTan)/Momentum(mm2,nTan) + Momentum(mm2+.0,nTan)/Momentum(mm1,nTan) - 2.*np.cos(Phi) )

def Function2(mm1,mm2,nTan):
    return np.sqrt( Momentum(mm1,nTan)*Momentum(mm2,nTan) )

def Interaction(bet,mm1,mm2,Phi,nTan):
    return - ( 1/( 4.*np.pi ) *
              ( np.exp( - eLength * Function2(mm1,mm2,nTan)*Function1(mm1,mm2,Phi,nTan) ) -
                np.exp( - eCutOff * Function2(mm1,mm2,nTan)*Function1(mm1,mm2,Phi,nTan) ) ) /
              Function1(mm1,mm2,Phi,nTan) * bet*(bet+np.cos(Phi) )
              )

def FourierTran(bet,mm1,mm2,nTan):
    a = 0.
    b = np.pi
    N = 10000
    x = np.linspace(a+(b-a)/(2*N), b-(b-a)/(2*N), N)
    fx = Interaction(bet,mm1,mm2,x,nTan) * np.cos(x)
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





#MomentumAxis = np.zeros((2*ThetaBins))
#PotentialAxis = np.zeros((2*ThetaBins))
#m1Indices = np.zeros((2*ThetaBins))
#SelfEnergy = np.zeros((2*ThetaBins))
#ScaleFactor = np.zeros((2*ThetaBins))
#Ham = np.zeros((2*ThetaBins,2*ThetaBins))







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
            Ham = float(Momentum(mm1,nTan)**BiLayer/(2*eEfMass) + HartreeFock(Momentum(mm1,nTan)) - HartreeFockCutOff(Momentum(mm1,nTan)))
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
    '''
    for m2 in range(0,ThetaBins):
        mm2 = m2 + 1 + ThetaBins*BloqueY
        if m1==m2:
            Ham = 0.
            #Ham = GenHopping(-1,mm1,mm2,nTan)
        else:
            Ham = GenHopping(-1,mm1,mm2,nTan)
            #Ham[m1,m2+ThetaBins] = 0
            #Ham[m2,m1+ThetaBins] = Ham[m1,m2+ThetaBins]
        file1.write("%s" % (mm1 - 1)),
        file1.write("\t"),
        file1.write("%s" % (mm2 - 1)),
        file1.write("\t"),
        file1.write("%s" % (Ham))
        file1.write('\n'),
    '''
'''
for m1 in range(0,ThetaBins): 
    mm1 = m1 + 1
    MomentumAxis[ThetaBins+m1+0] = +Momentum(mm1,nTan)
    m1Indices[ThetaBins+m1+0] = +mm1
    ScaleFactor[ThetaBins+m1] = -np.sqrt( nTan * np.tan( mm1*DeltaThet )**(2*nTan-1) ) / np.cos( mm1*DeltaThet ) / eLength
    #if ( ThetaBins>20 ):
    #    if (m1%(ThetaBins/20) )==0:
    #        print "\tFila m1 = ", ThetaBins+m1
    m1Indices[ThetaBins+m1+0] = +m1+1
    PotentialAxis[ThetaBins+m1] = + ( PotentialHF(Momentum(mm1,nTan)) - PotentialHFCutOff(Momentum(mm1,nTan)) )
    SelfEnergy[ThetaBins+m1] = + ( Momentum(mm1,nTan) + HartreeFock(Momentum(mm1,nTan)) - HartreeFockCutOff(Momentum(mm1,nTan)) )
    
    for m2 in range(0,ThetaBins):
        Ham[m1+ThetaBins,m2] =-Ham[m1,m2+ThetaBins]
    for m2 in range(0,ThetaBins):
        Ham[m1+ThetaBins,m2+ThetaBins] =-Ham[m1,m2]
'''

"""
print 'SelfEnergy'
PrintArrays(SelfEnergy,2*ThetaBins)

print 'Hopping m2 = 1'
PrintArrays(SelfEnergyInterm1,2*ThetaBins)
print 'Hopping m2 = 9'
PrintArrays(SelfEnergyInterm9,2*ThetaBins)
print 'Pairing m2 = 1'
PrintArrays(SelfEnergyInterM1,2*ThetaBins)
print 'Pairingm2 = 9'
PrintArrays(SelfEnergyInterM9,2*ThetaBins)
"""

"""
print 'Hamiltonian'
for m1 in range(0,2*ThetaBins):
    for m2 in range(0,2*ThetaBins):
        #print "%.1f" % Ham[m1,m2],#
        print Ham[m1,m2],#
        print '\t',
    print ''
print '\n'
"""

"""
eigVals, eigVecs = np.linalg.eig( Ham )
eigVecs = eigVecs.transpose()
sort_perm = np.argsort(eigVals)
sort_reve = np.fliplr([sort_perm])[0]
eigVals.sort()     # <-- This sorts the list in place.
eigVecs = eigVecs[sort_perm,:]
"""


"""
print 'MomentumAxis'
PrintArrays(MomentumAxis,2*ThetaBins)
print 'eigVals'
PrintArrays(eigVals,2*ThetaBins)
"""

"""
print eigVals
for m1 in range(0,2*ThetaBins):
    print "%.3f" % eigVals[m1],#
    for m2 in range(0,2*ThetaBins):
        print "%.3f" % eigVecs[m1,m2],#
        print '\t',
    print ''
"""

"""
plt.clf()
plt.figure(figsize=(10,10))
#plt.plot(m1Indices,MomentumAxis,'o')
plt.plot(MomentumAxis,MomentumAxis,'o')
plt.plot(MomentumAxis,eigVals,'.')
#plt.xlim(ThetaBins,2*ThetaBins)
#plt.xlim(right =0)
#plt.xlim(MomentumAxis,2*ThetaBins)
#plt.ylim(top   =0)
#plt.show()
plt.savefig('Graphene10-HamA.pdf')
plt.xlim(-2,+2)
plt.ylim(-2,+2)
plt.savefig('Graphene10-HamB.pdf')
"""









"""
Numerator = np.zeros((2*ThetaBins))
for m1 in range(0,ThetaBins):
    mm1 = m1 + 1
    Numerator[ThetaBins+m1] = ( np.dot(
        np.dot(np.array(eigVecs[ThetaBins+m1+0,:]),np.array(ScaleFactor)),
        np.dot(np.array(eigVecs[ThetaBins+m1+0,:]),np.array(ScaleFactor))) ) / np.sqrt( nTan**2 * np.tan(mm1*DeltaThet)**nTan *np.tan(mm1*DeltaThet)**nTan/(
                np.cos(mm1*DeltaThet)*np.cos(mm1*DeltaThet)*np.sin(mm1*DeltaThet)*np.sin(mm1*DeltaThet)
                ) ) 

Conductivity  = np.ones((2*ThetaBins))
Conductivity0 = np.ones((2*ThetaBins))
ConductivityHF = np.ones((2*ThetaBins))
for m1 in range(0,ThetaBins-1): 
    mm1 = m1 + 1
    Conductivity[ThetaBins+m1]   = (
        (Numerator[ThetaBins+m1]+Numerator[ThetaBins+m1+1]) / 
        ( ( eigVals[ThetaBins+m1+1] + eigVals[ThetaBins+m1+0] )*
          ( eigVals[ThetaBins+m1+1] - eigVals[ThetaBins+m1+0] )/ 
          ( MomentumAxis[ThetaBins+m1+1] - MomentumAxis[ThetaBins+m1+0] )) )# / (1  / np.cos( (mm1+1)*DeltaThet )**2  )
    ConductivityHF[ThetaBins+m1] = ( 
        MomentumAxis[ThetaBins+m1+0]/( PotentialAxis[ThetaBins+m1] * SelfEnergy[ThetaBins+m1] )
        )
    # / ( + np.tan( (mm1+1*DeltaThet ) / np.cos( mm1*DeltaThet )**2 ) )
"""




#print 'DeltaThet'
#print DeltaThet
#print 'MomentumAxis'
#print MomentumAxis

"""
for m2 in range(ThetaBins,2*ThetaBins):
    if np.abs(MomentumAxis[m2])<10.:
        print "%.4f" % MomentumAxis[m2],#
    else:
        blacablaca = MomentumAxis[m2]*.10
        print "%.4f" % blacablaca,#
    print '\t',
print ''
print 'eigVals'
#print eigVals
for m2 in range(ThetaBins,2*ThetaBins):
    if np.abs(eigVals[m2])<10:
        print "%.4f" % eigVals[m2],#
    else:
        blacablaca = eigVals[m2]*.10
        print "%.4f" % blacablaca,#
    print '\t',
print ''
print 'Numerator'
#print Numerator
for m2 in range(ThetaBins,2*ThetaBins):
    if Numerator[m2]<10:
        print "%.4f" % Numerator[m2],#
    else:
        blacablaca = Numerator[m2]*.10
        print "%.4f" % blacablaca,#
    print '\t',
print ''
print 'Conductivity'
#print ConductivitB
for m2 in range(ThetaBins,2*ThetaBins):
    if ConductivitB[m2]<10:
        print "%.4f" % ConductivitB[m2],#
    else:
        blacablaca = ConductivitB[m2]*.10
        print "%.4f" % blacablaca,#
    print '\t',

#print (Numerator[ThetaBins]+Numerator[ThetaBins+1])/2.
"""



"""
for m1 in range(0,2*ThetaBins):
    file1.write("%s" % (eigVals[m1]))
    #file1.write(eigVals[m1])
    for m2 in range(0,2*ThetaBins):
        file1.write('\t')
        file1.write("%s" % (eigVecs[m1,m2])),#
    file1.write('\n')
"""










"""
for m1 in range(0,2*ThetaBins):
    file1.write("%s" % (MomentumAxis[m1])),
    file1.write("\t"),
    file1.write("%s" % (eigVals[m1]))
    file1.write("\t"),
    file1.write("%s" % (SelfEnergy[m1]))
    file1.write("\t"),
    file1.write("%s" % (Conductivity[m1]))
    file1.write("\t"),
    file1.write("%s" % (Conductivity0[m1]))
    file1.write("\t"),
    file1.write("%s" % (ConductivityHF[m1]))
    file1.write('\n'),

file1.close() 
"""
print "Fin"

print("--- %s seconds ---" % (time.time() - start_time))

print (time.time() - start_time)  

file2 = open("Time.txt","a") 
file2.write("%s" % ( ThetaBins )),
file2.write("\t"),
file2.write("%s" % ( time.time() - start_time )),
file2.write('\n'),
file2.close() 
