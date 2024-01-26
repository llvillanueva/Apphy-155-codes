# -*- coding: utf-8 -*-
"""
@author: LLV
"""
#Exercise 5.3: Trancendental Equation
#Villanueva, Lloyd L. - 2014-05595

from math import cos

accuracy = 1e-12

f = lambda x: cos(x) - x
r1 = 1
r2 = 2
delta = 1.0

#secant method
while abs(delta)>accuracy:
	r3 = r2 - f(r2)*(r2-r1)/(f(r2) - f(r1)) 
	r1,r2 = r2,r3
	
	delta = r2 - r1
    
print("The solution to the equation cos(x) = x is x=",r2)