import matplotlib.pyplot as plt         
import math                                         

import numpy as np


## Create functions and set domain length

x = np.arange(0.0001, 1500.50, 0.01)

pi=math.pi
e=math.e
k=1.38*10**(-23)
t=300
m=.1

y=(1/x)**(3/2)*e**(-1/x)

#y=(2/pi*(m/k*t)**3)**0.5*x**2*e**(-m*x**2/(2*k*t))

print(y)
#y=k1*m*x*(1+k2/(ri*x)**(1/2))
#y =x/(x**(1/2))

#dy = 2*x - 1



## Plot functions and a point where they intersect

plt.plot(x, y)
#plt.plot(x, dy)

plt.plot(1, 1, 'or')



## Config the graph

plt.title('A Cool Graph')

plt.xlabel('X')

plt.ylabel('Y')

#plt.ylim([0, 4])

plt.grid(True)

plt.legend(['y = x^2', 'y = 2x'], loc='upper left')



plt.axis([0,1500,0,0.0005])

## Show the graph

plt.show()
