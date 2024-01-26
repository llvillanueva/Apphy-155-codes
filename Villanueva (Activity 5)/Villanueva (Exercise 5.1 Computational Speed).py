# -*- coding: utf-8 -*-
"""
@author: LLV
"""

#Exercise 5.1: Computational speed
#Villanueva, Lloyd L. - 2014-05595

import time
from numpy import array
from numpy import empty

a = empty(10000000, int)
b = empty(10000000, int)
c = empty(10000000, int)

print("Arrays of Numbers from 1 to 10 Million")
Numbers = array(range(1, 10000001))
print(Numbers)
print("")

#While Loop
print("While loop")
swloop = time.time()
i = 0
while abs(i) < 10000000:
    b[i] = (Numbers[i])**2
    i += 1
ewloop = time.time ()
twloop = ewloop - swloop
print("It takes", twloop,"seconds to square a number from 1 to 10 million in While Loop")
print("")

#For Loop
print("For loop")
sfloop = time.time()
for i in range(0,10000000):
    a[i] = Numbers[i]**2
efloop = time.time ()
tfloop = efloop - sfloop
print("It takes",tfloop," seconds to square a number from 1 to 10 million in For Loop")
print("")

#Vectorization
print("Vectorization")
SV = time.time()
c = Numbers**2
EV = time.time()
TV = EV - SV
print("It takes", TV, "seconds to square a number from 1 to 10 million using vectorization" )

print("")
print("Vectorization takes the least time, next is the for loop, and while has the longest time to execute")