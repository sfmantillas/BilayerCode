import time 
start_time = time.time() 
import numpy as np
import scipy as scip 
import scipy.special as special
import random as rd

Parameters = np.genfromtxt('Parameters.txt')
TodosHopp = np.genfromtxt('TodosHopp.txt')
TodosPair = np.genfromtxt('TodosPair.txt')
file1 = open("OptCond.txt","w") 
ThetaBins = int(Parameters[0]/5)
print 'ThetaBins = ', ThetaBins 
print 'len(TodosHopp.txt) = ',  len(TodosHopp)

eCharge = Parameters[1]
#eCharge = 1/137
eLength = 1.
eCutOff = Parameters[2]# + 1.*1.e-1
eSpeedF = 1.
eHoppin = 1.
nTan = 2

DeltaThet = np.pi/2./(ThetaBins*5+1)

from sympy import besseli, besselk

def Momentum(m,nTan):
    return np.tan(m * DeltaThet)**nTan / eLength

MomentumAxis = np.zeros((2*ThetaBins * 5))
PotentialAxis = np.zeros((2*ThetaBins * 5))
m1Indices = np.zeros((2*ThetaBins * 5))
SelfEnergy = np.zeros((2*ThetaBins * 5))
ScaleFactor = np.zeros((2*ThetaBins * 5))
Ham = np.zeros((2*ThetaBins * 5,2*ThetaBins * 5))
'''
HoppBloque00 = np.genfromtxt('HoppBloque00.txt')
HoppBloque01 = np.genfromtxt('HoppBloque01.txt')
HoppBloque02 = np.genfromtxt('HoppBloque02.txt')
HoppBloque03 = np.genfromtxt('HoppBloque03.txt')
HoppBloque04 = np.genfromtxt('HoppBloque04.txt')
HoppBloque11 = np.genfromtxt('HoppBloque11.txt')
HoppBloque12 = np.genfromtxt('HoppBloque12.txt')
HoppBloque13 = np.genfromtxt('HoppBloque13.txt')
HoppBloque14 = np.genfromtxt('HoppBloque14.txt')
HoppBloque22 = np.genfromtxt('HoppBloque22.txt')
HoppBloque23 = np.genfromtxt('HoppBloque23.txt')
HoppBloque24 = np.genfromtxt('HoppBloque24.txt')
HoppBloque33 = np.genfromtxt('HoppBloque33.txt')
HoppBloque34 = np.genfromtxt('HoppBloque34.txt')
HoppBloque44 = np.genfromtxt('HoppBloque44.txt')

PairBloque00 = np.genfromtxt('PairBloque00.txt')
PairBloque01 = np.genfromtxt('PairBloque01.txt')
PairBloque02 = np.genfromtxt('PairBloque02.txt')
PairBloque03 = np.genfromtxt('PairBloque03.txt')
PairBloque04 = np.genfromtxt('PairBloque04.txt')
PairBloque11 = np.genfromtxt('PairBloque11.txt')
PairBloque12 = np.genfromtxt('PairBloque12.txt')
PairBloque13 = np.genfromtxt('PairBloque13.txt')
PairBloque14 = np.genfromtxt('PairBloque14.txt')
PairBloque22 = np.genfromtxt('PairBloque22.txt')
PairBloque23 = np.genfromtxt('PairBloque23.txt')
PairBloque24 = np.genfromtxt('PairBloque24.txt')
PairBloque33 = np.genfromtxt('PairBloque33.txt')
PairBloque34 = np.genfromtxt('PairBloque34.txt')
PairBloque44 = np.genfromtxt('PairBloque44.txt')
'''

for filas in range(0,len(TodosHopp)):
    m0 = int(TodosHopp[filas,0])
    m1 = int(TodosHopp[filas,1])
    m2 = TodosHopp[filas,2]
    m3 = TodosPair[filas,2]
    Ham[m0,m1] = m2
    Ham[m1,m0] = m2
    Ham[m0+5*ThetaBins,m1+5*ThetaBins] = -Ham[m0,m1]
    Ham[m1+5*ThetaBins,m0+5*ThetaBins] = -Ham[m1,m0]
    #    Ham[mm1,mm2+5*ThetaBins] = PairBloque00[contador,2]
    #    Ham[mm1+5*ThetaBins,mm2] =-Ham[mm1,mm2]
    #print "(m1,m2) = (", TodosHopp[filas,0], ',', TodosHopp[filas,1], ') = ', TodosHopp[filas,2]
    Ham[m0,m1 + 5*ThetaBins] = m3
    Ham[m1,m0 + 5*ThetaBins] = m3
    Ham[m0+5*ThetaBins,m1] = -Ham[m0,m1 + 5*ThetaBins]
    Ham[m1+5*ThetaBins,m0] = -Ham[m1,m0 + 5*ThetaBins]

eigVals, eigVecs = np.linalg.eig( Ham )
eigVecs = eigVecs.transpose()
sort_perm = np.argsort(eigVals)
sort_reve = np.fliplr([sort_perm])[0]
eigVals.sort()     # <-- This sorts the list in place.
eigVecs = eigVecs[sort_perm,:]


'''
print 'Hamiltonian'
for m1 in range(0,2*ThetaBins * 5):
    for m2 in range(0,2*ThetaBins * 5):
        print "%.0e" % Ham[m1,m2],#
        #print Ham[m1,m2],#
        print '\t',
    print ''
print '\n'
'''
ThetaBins = ThetaBins * 5
for m1 in range(0,ThetaBins): 
    mm1 = m1 + 1
    #if ( ThetaBins>20 ):
    #    if (m1%(ThetaBins/20) )==0:
    #        print "\tFila m1 = ", m1
    MomentumAxis[ThetaBins-m1-1] = -Momentum(mm1,nTan)
    m1Indices[ThetaBins-m1-1] = -mm1
    ScaleFactor[m1] = +np.sqrt( nTan * np.tan( mm1*DeltaThet )**(2*nTan-1) ) / np.cos( mm1*DeltaThet ) / eLength
    m1Indices[ThetaBins-m1-1] = -m1-1
for m1 in range(0,ThetaBins): 
    mm1 = m1 + 1
    MomentumAxis[ThetaBins+m1+0] = +Momentum(mm1,nTan)
    m1Indices[ThetaBins+m1+0] = +mm1
    ScaleFactor[ThetaBins+m1] = -np.sqrt( nTan * np.tan( mm1*DeltaThet )**(2*nTan-1) ) / np.cos( mm1*DeltaThet ) / eLength
    #if ( ThetaBins>20 ):
    #    if (m1%(ThetaBins/20) )==0:
    #        print "\tFila m1 = ", ThetaBins+m1
    m1Indices[ThetaBins+m1+0] = +m1+1
    
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

for m1 in range(0,2*ThetaBins):
    file1.write("%s" % (MomentumAxis[m1])),
    file1.write("\t"),
    file1.write("%s" % (eigVals[m1]))
    file1.write("\t"),
    file1.write("%s" % (Conductivity[m1]))
    file1.write("\t"),
    file1.write("%s" % (Conductivity[m1]-1))
    file1.write("\n"),

file1.close() 

print "Fin"

print("--- %s seconds ---" % (time.time() - start_time))

print (time.time() - start_time)  

file2 = open("Time.txt","a") 
file2.write("%s" % ( ThetaBins )),
file2.write("\t"),
file2.write("%s" % ( time.time() - start_time )),
file2.write('\n'),
file2.close() 
