from pylab import plot, show, imshow, linspace, gray
from math import pi, sin, sqrt
from cmath import exp
import matplotlib.pyplot as plt

# PART A
#The sepearation of the slits can expressed as d = (pi/alpha)

# PART B
d = 20e-6
alpha = pi/d

q = lambda u: (sin(alpha*u))**2 #

# PART C
w = 10 * d
wavelength = 500e-9
focus = 1
k = 2*pi/wavelength

def I(x):
    f = lambda u,x: sqrt(q(u))*exp(1j*k*u * x/focus)	
    N = 101
    a = -w/2
    b = w/2
    h = (b-a)/N
    s = 0.5*f(a,x) + 0.5*f(b,x)
    for i in range(1,N):
        s += f(a+i*h , x)
        
    return h**2 * (s.real**2 + s.imag**2)

#part D
x = linspace(-0.05,0.05, 500)
intensity = [I(xi) for xi in x]

plt.figure(1)
plt.title("Plot for letter D")
plt.plot(x, intensity)
plt.xlabel("Position (cm)")
plt.ylabel("Intensity")
plt.savefig("C:/Users/Lloyd/Documents/plotD_plot.pdf")
show()

plt.figure(2)
plt.title("Density Plot for letter D")
gray()
plt.imshow([intensity],aspect=60)
plt.savefig("C:/Users/Lloyd/Documents/plotD_dplot.pdf")

#part E1
beta = alpha/2
q = lambda u: ((sin(alpha*u))**2)*((sin(beta*u))**2)

intensityE1 = [I(xi) for xi in x]

plt.figure(3)
plt.title("Plot for letter E1")
plt.plot(x, intensityE1)
plt.xlabel("Position (cm)")
plt.ylabel("Intensity")
plt.savefig("C:/Users/Lloyd/Documents/plotE1_plot.pdf")
show()

plt.figure(4)
plt.title("Density Plot for letter E1")
plt.gray()
plt.imshow([intensityE1],aspect=60)
plt.savefig("C:/Users/Lloyd/Documents/plotE1_dplot.pdf")


#PART E(2)

def Isquare(x):
    T = 1
    f = lambda u,x: T*exp(1j*k*u * x/focus)	
    N = 101
    a = -55e-6
    b = 55e-6
    h = (b-a)/N
    s = 0.5*f(a,x) + 0.5*f(b,x)
    for i in range(1,N):
        u = a+i*h
        if abs(u) >= -40e-6 and abs(u) <= -30e-6:
            T = 1
        elif abs(u) <= 50e-6 and abs(u) >= 30e-6:
            T = 1
        else:
            T = 0
        s += f(u, x)
    return h**2 * (s.real**2 + s.imag**2)

x = linspace(-0.05,0.05, 500)
intensityE2 = [Isquare(xi) for xi in x]

plt.figure(5)
plt.title("Plot for letter E2")
plt.plot(x, intensityE2)
plt.xlabel("Position (cm)")
plt.ylabel("Intensity")
plt.savefig("C:/Users/Lloyd/Documents/plotE2_plot.pdf")
show()

plt.figure(6)
plt.title("Density Plot for letter E2")
plt.gray()
plt.imshow([intensityE2],aspect=60)
plt.savefig("C:/Users/Lloyd/Documents/plotE2_dplot.pdf")