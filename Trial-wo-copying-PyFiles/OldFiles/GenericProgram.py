import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec  
import random as rdm
from numpy import linalg as LA

Parameters = np.genfromtxt('Parameters.txt')

Dims = int(Parameters[0])
Seed = Parameters[1]
Rang = Parameters[2]

rdm.seed(Parameters[1])

fileEigVals = open('EigValsAAABBBCCC.txt',"w")

fileEigVecs = open('EigVecsAAABBBCCC.txt',"w")

print Dims

MatrizAleatoria = np.zeros((Dims,Dims))
Contador = []

for mx in range(0,Dims):
    Contador.append(mx)
    for my in range(0,mx):
        MatrizAleatoria[mx][my] = np.random.normal(0, 1)#rdm.uniform(0.,Rang)
        #MatrizAleatoria[mx][my] = rdm.uniform(0.,Rang)
        MatrizAleatoria[my][mx] = MatrizAleatoria[mx][my]
    MatrizAleatoria[mx][mx] = 0

print MatrizAleatoria[mx][my]

eigVals, eigVecs = LA.eig( MatrizAleatoria )
eigVecs = eigVecs.transpose()
sort_perm = np.argsort(eigVals)
sort_reve = np.fliplr([sort_perm])[0]
eigVals.sort()     # <-- This sorts the list in place.
eigVecs = eigVecs[sort_perm,:]

eigValsRe = []
eigValsIm = []
eigValsDf = []

for mx in range(0,Dims):
    eigValsRe.append(np.real(eigVals[mx]))
    eigValsIm.append(np.imag(eigVals[mx]))

for mx in range(1,Dims):
    eigValsDf.append(np.real(eigVals[mx]-np.real(eigVals[mx-1])))

fig = plt.figure(figsize=(5,5), dpi=200)                                                        #Define object figure with given size
gs  = gridspec.GridSpec(1,1)                                                                    #Define the 3x1 grid as frame for the canvas
ax1 = plt.subplot(gs[0])

plt.plot(eigValsRe,'.',c=[4/4., 0/4., 0/4.],label='$\\mathrm{5\\times 10^{-1}}$')
plt.plot(eigValsIm,'.',c=[4/4., 2/4., 0/4.],label='$\\mathrm{5\\times 10^{-1}}$')
plt.plot(eigVals  ,'-',c=[0/4., 2/4., 2/4.],label='$\\mathrm{5\\times 10^{-1}}$')

plt.savefig('EigValsAAABBBCCC.jpg')

plt.clf()

plt.plot(eigValsDf,'.',c=[0/4., 0/4., 4/4.],label='$\\mathrm{5\\times 10^{-1}}$')
plt.savefig('EigValsDDD.jpg')

for mx in range(0,Dims):
    fileEigVals.write("%s" % (eigVals[mx]))
    fileEigVals.write("\n"),

