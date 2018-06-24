from numpy import *

import matplotlib.pyplot as plt

#from matplotlib.pyplot import scatter

a=arange(0,10,0.01,dtype=float)
#print (a)


b=[]



for i in range(len(a)):
    b.insert(i,cos(a[i]))
#print(b)
plt.scatter(a,b)




x=linspace(-10, 10, 100)
print(x)


plt.show()
