'''
Coding task 2: make graphs of velocity versus height for a 50km free-fall
a) assuming -9.80 m/2 of acceleration
b) correcting for the variation in 'g' over the 50km altitude
c) ** including quadratic drag force with a constant coefficient
d) **including quadratic drag with a 'density scale height' drag co-efficient
'''

import numpy as np
import matplotlib.pyplot as plt


height = 50000
velocity = 0
dt = 0.1
earth_radius = 6380000  
constant_G = 6.674*10**-11
earth_mass = 5.972*10**24
gravity = constant_G*(earth_mass/(earth_radius+height)**2)

'''
Equation for gravity is g(h) = G(M/(R+H)^2)
'''
def calculate_gravity(height_for_equation):
     return constant_G*(earth_mass/(earth_radius+height_for_equation)**2)

x_values = []
y_values = []

while height > 0:
    x_values.append(velocity)
    y_values.append(height)
    gravity = calculate_gravity(height)
    velocity += gravity * dt
    height -= velocity * dt



plt.plot(x_values, y_values)
plt.title("Graph of Velocity vs. Height")
plt.xlabel("Velocity")
plt.ylabel("Height")
plt.show()

