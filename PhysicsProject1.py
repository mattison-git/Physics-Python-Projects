import numpy as np
import matplotlib.pyplot as plt

e = np.e

height = 50000
velocity = 0
dt = 0.1

earth_radius = 6380000  
constant_G = 6.674*10**-11
earth_mass = 5.972*10**24

def calculate_gravity(h):
     return constant_G*(earth_mass/(earth_radius+h)**2)

sea_level_air_density = 1.225
air_density_scale_constant = 8500

def calculate_air_density(h):
    return sea_level_air_density*e**(-h/air_density_scale_constant)
    
drag_coefficient = 1
cross_sectional_area = 1
mass = 80 

def calculate_drag_acceleration(v, h, variable_density=True):
    rho = calculate_air_density(h) if variable_density else sea_level_air_density
    k = 0.5 * rho * drag_coefficient * cross_sectional_area
    return k * v**2 / mass

x_values = []
y_values = []


variable_density = True

while height > 0:
    x_values.append(velocity)
    y_values.append(height)
    
    gravity = calculate_gravity(height)
    drag_acc = calculate_drag_acceleration(velocity, height, variable_density)
    
    acceleration = gravity - drag_acc
    
    velocity += acceleration * dt
    height -= velocity * dt

plt.plot(x_values, y_values)
plt.title("Graph of Velocity vs. Height")
plt.xlabel("Velocity")
plt.ylabel("Height")
plt.grid(True)
plt.show()
