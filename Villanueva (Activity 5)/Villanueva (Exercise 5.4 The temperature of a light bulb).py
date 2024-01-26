# -*- coding: utf-8 -*-
"""
@author: LLV
"""

#Exercise 5.4: The Temperature of a light bulb
#Villanueva, Lloyd L. - 2014-05595


from math import exp, sqrt
from numpy import ones,copy,cos,tan,pi,linspace
import matplotlib.pyplot as plt
from pylab import show

############################################################
#Gauss Quadriture
def gaussxw(N):

    # Initial approximation to roots of the Legendre polynomial
    a = linspace(3,4*N-1,N)/(4*N+2)
    x = cos(pi*a+1/(8*N*N*tan(a)))

    # Find roots using Newton's method
    epsilon = 1e-15
    delta = 1.0
    while delta>epsilon:
        p0 = ones(N,float)
        p1 = copy(x)
        for k in range(1,N):
            p0,p1 = p1,((2*k+1)*x*p1-k*p0)/(k+1)
        dp = (N+1)*(p0-x*p1)/(1-x*x)
        dx = p1/dp
        x -= dx
        delta = max(abs(dx))

    # Calculate the weights
    w = 2*(N+1)*(N+1)/(N*N*(1-x*x)*dp*dp)

    return x,w

def gaussxwab(N,a,b):
    x,w = gaussxw(N)
    return 0.5*(b-a)*x+0.5*(b+a),0.5*(b-a)*w

#################################################################

# PART A

print("Part A")

λ1 = 390e-9
λ2 = 750e-9
c = 299792458
h = 6.62607004e-34
kb = 1.38064852e-23 

def Gauss(T):
    f = lambda x: (15/pi**4)*(x**3/(exp(x)-1))
    N = 100
    a = h*c/(λ2*kb*T)
    b = h*c/(λ1*kb*T)


# Calculate the sample points and weights, then map them
# to the required integration domain
    x,w = gaussxw(N)
    xp = 0.5*(b-a)*x + 0.5*(b+a)
    wp = 0.5*(b-a)*w

# Perform the integration
    s = 0.0
    for k in range(N):
        s += wp[k]*f(xp[k])
    return s

Efficiency = [Gauss(xi) for xi in range(300,10000+1)]

plt.figure(1)
plt.title("Efficiency vs Temperature (T)")
plt.plot(range(300, 10000+1), Efficiency)
plt.xlabel("Temperature (Kelvin)")
plt.ylabel("Efficiency")
plt.savefig("C:/Users/Lloyd/Documents/plot.pdf")
show()

#PART B Golden Ratio Search
print("Part B")

accuracy = 1
z = (1+sqrt(5))/2     # Golden ratio

# Function to calculate the Buckingham potential
f = lambda T: (15/pi**4)*((h*c/(λ1*kb*T))**3/((exp(h*c/(λ2*kb*T))-1)))

# Initial positions of the four points
x1 = 300
x4 = 10000
x2 = x4 - (x4-x1)/z
x3 = x1 + (x4-x1)/z

# Initial values of the function at the four points
f1 = f(x1)
f2 = f(x2)
f3 = f(x3)
f4 = f(x4)

# Main loop of the search process
while x4-x1>accuracy:
    if f2>f3:
        x4,f4 = x3,f3
        x3,f3 = x2,f2
        x2 = x4 - (x4-x1)/z
        f2 = f(x2)
    else:
        x1,f1 = x2,f2
        x2,f2 = x3,f3
        x3 = x1 + (x4-x1)/z
        f3 = f(x3)

# Print the result
print("The maximum Efficiency occur at",int(0.5*(x1+x4)),"Kelvin")


"""
 #Part C
 It is not practical because
 1. You need a lot of energy to reach the Temperature where it will have a maximum efficiency
 2. Reaching that Temperature only give you around 45% efficiency
 3. More energy is converted to HEAT than Light
""" 