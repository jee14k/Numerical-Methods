# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 10:32:24 2019

@author: Jeevan
"""

## Bi - Section Method.
# The function is x^3 + 1
import numpy as np
import matplotlib.pyplot as plt
#from scipy.optimize import fsolve

def func(x):
    return x*x*x + 1

# Prints root of func(x)
# with given tolerance 
def bisection(a,b,tol):
    xl = a
    xr = b
    i = 0
    #if (func(xl) * func(xr) >= 0):
    #  print("You have not assumed right a and b\n")
    #    return
    
    while (np.abs(xl-xr) >= 0):
        
        #Find middle point
        c = (xl+xr)/2.0
        prod = func(xl)*func(c)
        #Check if middle point is root
        #if (func(c) == 0.0):
        #  break
        
        # Decide the side to repeat the steps
        if (prod > tol):
            xl = c
            i+=1
        else:
            xr = c
            i+=1
    return c,i

answer = bisection(-5,5,0.0001)
print("The value of root is:     ",answer[0],answer[1])
x = np.linspace(-5,5,100)
plt.plot(x,func(x))
plt.grid()
plt.show()