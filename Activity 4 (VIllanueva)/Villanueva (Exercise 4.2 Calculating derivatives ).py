# -*- coding: utf-8 -*-
"""
Exercise 4.2: Calculating derivatives (Exercise 4.3 in Newman)
@author: Lloyd L. Villanueva - 2014-05595
"""

#letter A
def f(x):
    return x*(x+1)

x = 1
delta = 10e-2

df_a = (f(x+delta)-f(x))/delta
exactdf = 2*x + 1

print("Approximation (delta =",delta,"): ", df_a)
print("True value: ", exactdf)
print("They not agree perfecly because 10e-2 is a large approximation of 0")
print("")

#letter B
d = [10e-4, 10e-6, 10e-8, 10e-10, 10e-12, 10e-14]
for i in range(6):
    delta = d[i]
    df_b = (f(x+delta)-f(x))/delta
    print("Approximation (delta =",delta,"): ", df_b)
print("True value: ", exactdf)
print("")
print("the accuracy of the calculation initially gets better as δ gets smaller,but then gets worse again.")
print("This happen because as δ gets smaller, the value of f(x+δ) will approach the value of f(x)")
print("the large errors arises in calculations that involve the subtraction of numbers that are nearly equal")
