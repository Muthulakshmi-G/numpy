import numpy as np
# here we show numpy version and configuration
print(np.__version__)
np.show_config()

#create null vector of size 10
z=np.zeros(10)
print(z)

#create vector with values ranging from 0 to 49
Z=np.arange(0,50)
print(Z)
Z=Z[::-1]#the first element becomes last
print(Z)
#create 3x3 matrix with values ranging from 0 to 8
X=np.arange(9).reshape(3,3)
print(X)

#find indices of non-zero elemnets
nz=np.nonzero([1,2,0,0,4,0,5,5,6,7,9,22,2,0,0,9])
print(nz)

#create identy matrix 3x3
z=np.eye(3)
print(z)


#create 3x3x3 array with radndom values
Z=np.random.random((3,3,3))
print(Z)

#create a 10x10 array with random values &find max and min values
A=np.random.random((10,10))
Amin,Amax=A.min(),A.max()
print(Amin,Amax)



#create a random vector of size 30 and find mean value
Z=np.random.random(30)
m=Z.mean()
print(m)

#create 2d array with 1 border and 0 inside
Z=np.ones((10,10))
Z[1:-1,1:-1]=0
print(Z)

a=np.ones((10,10))
a[3:-3]=5
print(a)

m=np.arange(0,60).reshape(6,10)
m[3:-1]=6
print(m)

#try it.whats is the result?
0*np.nan  #nan
np.nan==np.nan  #False
np.inf>np.nan  #False
np.nan-np.nan  #nan
0.3==3*0.1     #False


#5x5 matrix with values 1,2,3,4 just below the diagonal
X=np.array([1,2,3,4])
d=np.diag(X)
print(d)

a = np.matrix([1,2,3,4])
d = np.diag(a.A1)
print (d)

#normalize a 5x5 random matrix

z=np.random.random((5,5)) #random number 5x5
zmax,zmin=z.max(),z.min() #max,min values from z corresponding to zmax,zmin
z=(z-zmin)/(zmax-zmin) #subtract zmin from zmax ,divides to the (z-zmin)
print(z)


#create custom dtype.is describes a color as 4 unsigned bytes(RGBA)
color=np.dtype([("r",np.ubyte,1),
               ("g",np.ubyte,1),
               ("b",np.ubyte,1),
               ("a",np.ubyte,1)])
print(color)

#real matrix product
a=np.ones((5,3))
print(a)
b=np.ones((3,2))
print(b)
z=np.dot((a),(b))
print(z)

#what is the output of this?
print(sum(range(5),-1))
from numpy import *
print(sum(range(5),-1))
