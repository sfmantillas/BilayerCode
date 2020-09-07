import numpy as np
from numpy import linalg as LA

import scipy as sc
from scipy.interpolate import interp1d
import scipy.integrate as integrate

import matplotlib.pyplot as plt

#Size of steps on radial coordinate
def Delta_Mom(K,N):
    return K/(N+1)

#Parametrization of the momentum in terms of tan(th)**r/sqrt(r)
def Tan_Mom(i,K,N):
    return i*Delta_Mom(K,N)

#Jacobian of the lattice reconfig. to the tangent parametrization
def Jacobi(i,K,N):
    return 1.#Delta_Mom(N)*K**2*np.tan(np.pi/2*i/(N+1))**(2*R-1)/np.cos(np.pi/2*i/(N+1))**2

#Kinetic term of the m-layer system
def Kin_Term(k,Euv,K,N,M):
    return Euv*(k/K)**M

#Norm in the reciprocal lattice
def Norm_Mom(k1,k2,th):
    return k1**2 + k2**2 - 2*k1*k2*np.cos(th)

#Coulomb interaction
def Coulomb(k1,k2,th,Euv,K,G,A):
    num = Euv/K**2*G*np.exp( -A**2*Norm_Mom(k1,k2,th)/K**2 )
    return num

#Hopping/pairing terms
def Hopp_Pair(k1,k2,th,Euv,K,G,A,M,s):
    return -1/(4*np.pi)*( Coulomb(k1,k2,th,K) )*s*( s+np.cos(M*th) )

def SelfEnergy(k,Euv,K,N,M,G,A):
    Factor0 = G*Euv/( 4*np.pi*A**2 )
    Factor1 = 1 - np.exp(-A**2*Norm_Mom(k1,k2,th)/K**2)
    Factor2 = 1 - 2K**2/(A**2*k**2)*Factor1
    return Factor0*Factor2

#Angular momentum channels
def Four_Hopp_Pair(k1,k2,l,Euv,K,G,A,M,s):
    chopps = 10000
    suma = 0.
    x = np.pi/chopps*np.arange(0, chopps)
    y = Hopp_Pair(k1,k2,x,Euv,K,G,A,M,s)*np.cos(l*x)
    #suma = integrate.quad(y, x, even='last')
    suma = integrate.quad(lambda x: Hopp_Pair(k1,k2,x,Euv,K,G,A,M,s)*np.cos(l*x), 0, np.pi)[0]
    return suma

#Import the self-energy from file InteMm.txt
#SelfEnergyData = np.loadtxt(fname = "InteM1.txt")

NNN = 10**1         #Matrix size
EUV = 1.            #UV cutoff energy
KKK = 1.            #UV cutoff momentum
RRR = 2             #Power of the tangent
AAA = 2.            #Coulomb strength
GGG = 1.
LLL = 1             #Angular momentum channel
MMM = 1             #Number of layers

"""
PRINTING OF TERMS TO DO THE BENCH-MARK
print "Hopp"
print Hopp_Pair(Tan_Mom(1,RRR,KKK,NNN),Tan_Mom(2,RRR,KKK,NNN),np.pi/3,KKK,MMM,+1)
print "Four_Hopp"
print Four_Hopp_Pair(Tan_Mom(1,RRR,KKK,NNN),Tan_Mom(2,RRR,KKK,NNN),1,KKK,MMM,+1)
print "Pair"
print Hopp_Pair(Tan_Mom(1,RRR,KKK,NNN),Tan_Mom(2,RRR,KKK,NNN),np.pi/3,KKK,MMM,-1)
print "Four_Pair"
print Four_Hopp_Pair(Tan_Mom(1,RRR,KKK,NNN),Tan_Mom(2,RRR,KKK,NNN),1,KKK,MMM,-1)
print "Jacobi"
print Jacobi(1,RRR,KKK,NNN)
"""

#Radial coordinate slots
MomentumAxis = np.zeros(NNN)
for i in range(0, NNN):
    MomentumAxis[i] = Tan_Mom(i+1,KKK,NNN)

#Self-energy evaluated at MomentumAxis
#SelfEnergy = np.interp(MomentumAxis, SelfEnergyData[:,0], SelfEnergyData[:,1])

#print MomentumAxis
#print SelfEnergy

"""
PLOT OF TE SELF-ENERGY IN LOG MOMENTUM
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
line, = ax.plot(SelfEnergyData[:,0], SelfEnergyData[:,1], color='blue', lw=2,marker="*")
line, = ax.plot(MomentumAxis, SelfEnergy, color='red', marker="*")
plt.xlim(0.001, 10)

ax.set_xscale('log')

plt.show()
"""
#Bogoliubov Hamiltonian
HamiltonMatrix = np.zeros((2*NNN,2*NNN))
for i in range(0,NNN):
    mx = i+1
    for j in range(0,i+1):
        my = j+1
        if i==j:
            #Selection of the kinetic/self-energy terms on the diagonal
            Mom = Tan_Mom(mx,KKK,NNN)
            HamiltonMatrix[i+000][j+000] = Kin_Term(Mom,EUV,KKK,NNN,MMM) + AAA*SelfEnergy(Mom,EUV,KKK,NNN,MMM,GGG,AAA)
            HamiltonMatrix[i+NNN][j+NNN] = -HamiltonMatrix[i][j]
        else:
            #Off-diagonal terms
            #Definition of the momenta for the matrix element i,j
            Mom1 = Tan_Mom(mx,KKK,NNN)
            Mom2 = Tan_Mom(my,KKK,NNN)
            #Hopping terms 
            HamiltonMatrix[i+000][j+000] = Four_Hopp_Pair(Mom1,Mom2,LLL,EUV,KKK,GGG,AAA,MMM,+1)*np.sqrt( Jacobi(mx,KKK,NNN)*Jacobi(my,KKK,NNN) )
            HamiltonMatrix[j+000][i+000] = HamiltonMatrix[i][j]
            HamiltonMatrix[i+NNN][j+NNN] = -HamiltonMatrix[i][j]
            HamiltonMatrix[j+NNN][i+NNN] = -HamiltonMatrix[i][j]
            #Pairing terms
            HamiltonMatrix[i+000][j+NNN] = Four_Hopp_Pair(Mom1,Mom2,LLL,EUV,KKK,GGG,AAA,MMM,-1)*np.sqrt( Jacobi(mx,KKK,NNN)*Jacobi(my,KKK,NNN) )
            HamiltonMatrix[j+000][i+NNN] = +HamiltonMatrix[i+000][j+NNN]
            HamiltonMatrix[i+NNN][j+000] = -HamiltonMatrix[i+000][j+NNN]
            HamiltonMatrix[j+NNN][i+000] = -HamiltonMatrix[i+000][j+NNN]

#PRINTING OF THE FULL-HAMILTONIAN. Not recommended to activate for sizes NNN>4
#print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in HamiltonMatrix]))

#DIAGONALIZATION OF THE HAMILTONIAN
HamiltonEigVals, HamiltonEigVecs = LA.eig( HamiltonMatrix )

#SORTING OF THE EIGENVALUES
idx = np.argsort(HamiltonEigVals)
HamiltonEigVals = HamiltonEigVals[idx]
HamiltonEigVecs = HamiltonEigVecs [:,idx]

"""
PRINTING OF EIGSYSTEM
print "HamiltonEigVals"
print HamiltonEigVals

print "HamiltonEigVecs"
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in HamiltonEigVecs]))

print "First HamiltonEigVals"
print HamiltonEigVals[0]

print "First HamiltonEigVecs"
print HamiltonEigVecs[:,0]
"""

