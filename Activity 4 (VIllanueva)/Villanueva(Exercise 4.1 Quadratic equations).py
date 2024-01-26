# -*- coding: utf-8 -*-
"""
Exercise 4.1: Quadratic equations (Exercise 4.2 in Newman)
@author: Lloyd L. Villanueva - 2014-05595
"""

from math import sqrt

print('Please give numbers for: {0}x**2 + {1}x + {2} = 0'.format('a','b','c'))

a = float(input("Coefficient of x^2: "))
b = float(input("Coefficient of x: "))
c = float(input("Constant: "))
# this formula is for letter A
x1_1 = (-b + sqrt(b**2-4*a*c))/2/a #with truncated error because of subraction (diff in sign)
x1_2 = (-b - sqrt(b**2-4*a*c))/2/a #correct value
#this formula is for letter B, A and B has different result in root
x2_1 = 2*c / (-b - sqrt(b**2 - 4*a*c)) #correct value
x2_2 = 2*c / (-b + sqrt(b**2 - 4*a*c)) #with truncated error because of subraction (diff in sign)

#for letter c, the formula that does not involve subtraction in the process has the correct value of roots
x1c = x2_1
x2c = x1_2

print("The solution to", a,"x**2 +", b,"x +",c," = 0")
print("With method A:")
print("x1 = ",x1_1)
print("x2 = ",x1_2)
print("")
print("With method B:")
print("x1 = ",x2_1)
print("x2 = ",x2_2)
print("")
print("Solution C:")
print("x1 = ",x1c)
print("x2 = ",x2c)
