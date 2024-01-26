# -*- coding: utf-8 -*-
"""
Exercise 4.3: The Lagrange point (Exercise 6.16 in Newman)
@author: Lloyd L. Villanueva - 2014-05595
"""
accuracy = 1e-12

G = 6.674e-11
M = 5.974e24
m = 7.348e22
R = 3.844e8
omega = 2.662e-6

f = lambda r: G*M/r**2 - G*m/(R-r)**2 - omega**2*r

r1 = 1
r2 = 2
delta = 1.0
while abs(delta)>accuracy:
	r3 = r2 - f(r2)*(r2-r1)/(f(r2) - f(r1)) 
	r1,r2 = r2,r3
	
	delta = r2 - r1

print(r2,"meters")
