# -*- coding: utf-8 -*-
"""
@author: Lloyd
"""

#Exercise 5.2 (Error in integration)
#Villanueva, Lloyd L. - 2014-05595

from math import sqrt, pi, sin

def simpson(f, a, b, n):
    """Approximates the definite integral of f from a to b by the
    composite Simpson's rule, using n subintervals (with n even)"""

    if n % 2:
        raise ValueError("n must be even (received n=%d)" % n)

    h = (b - a) / n
    s = f(a) + f(b)

    for i in range(1, n, 2):
        s += 4 * f(a + i * h)
    for i in range(2, n-1, 2):
        s += 2 * f(a + i * h)

    return s * h / 3

def trapezoidal(f, a, b, N):

    h = (b-a)/N
    s = 0.5*f(a) + 0.5*f(b)
    for k in range(1,N):
        s += f(a+k*h)
    return h*s

print("The analytic answer of the Integral is:")
TV = pi/2
print(TV)
print("")

print("Using Simpson Method to the integration of sqrt(1-x**2) is:")
S1 = simpson(lambda x: sqrt(1-x**2), -1.0, 1.0, 10)
print(S1)
print("Absolute Error:", abs(TV - S1))
print("")

"""
the integral of sqrt(1-x**2)dx turn to (sin(theta))**2 when x = cos x
sqrt(1 - (cos(theta))**2) = sqrt((sin(theta))**2) #identities
will lead to (sin(theta))
also x = cos(theta), taking the differential both sides will lead to dx = -sin(theta)
therefore the integrand become -(sin(theta))**2
but the limits of integration is from lower bound x=-1 to upper bound x=1
if x = cos(theta) it will become lower bound theta = pi to upper bound theta = 0
so interchaging the bounds will give as negative sign and reducing the equation to
(sin(theta))**2 with lower bound of 0 and upper bound of pi
"""

print("Using Simpson Method to the integration and x = cos(theta) is:")
S2 = simpson(lambda theta: (sin(theta))**2, 0, pi, 10)
print(S2)
print("Absolute Error:", abs(TV - S2))
print("")

print("Using Trapezoidal Method the integration of sqrt(1-x**2) is:")
T1 = trapezoidal(lambda x: sqrt(1-x**2), -1.0, 1.0, 10)
print(T1)
print("Absolute Error:", abs(TV - T1))
print("")

print("Using Trapezoidal Method to the integration and x = cos(theta) is:")
T2 = trapezoidal(lambda theta: (sin(theta))**2, 0, pi, 10)
print(T2)
print("Absolute Error:", abs(TV - T2))
print("")


"""
The integrand of sqrt(1-x**2), when used has a big error compare to when x is expressed in trigonometric function, even we use Trapezoidal or Simpsons method.
The possible source of error in integrand of sqrt(1-x**2) is the wrong distribution of weights, wherein the weights is concentrated in the center
which is the correct distribution of the weights must be at the both end because of the steepness of it.
"""