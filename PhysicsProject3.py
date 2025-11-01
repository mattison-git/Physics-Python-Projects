import numpy as np
import matplotlib.pyplot as plt

e = np.e

height0 = 50000
velocity0 = 0
dt = 0.1

earth_radius = 6380000  
constant_G = 6.674*10**-11
earth_mass = 5.972*10**24

drag_coefficient = 1
cross_sectional_area = 1
mass = 80
air_density_scale_constant = 10000
sea_level_air_density = 1.225

def calculate_gravity(h):
    return constant_G*(earth_mass/(earth_radius+h)**2)

def calculate_air_density(h):
    return sea_level_air_density * e**(-h/air_density_scale_constant)

def calculate_drag_acceleration(v, h, variable_density=True):
    rho = calculate_air_density(h) if variable_density else sea_level_air_density
    k = 0.5 * rho * drag_coefficient * cross_sectional_area
    return k * v**2 / mass

def simulate(free_fall_type):
    height = height0
    velocity = velocity0  
    x_values = []
    y_values = []
    
    while height > 0:
        x_values.append(velocity)
        y_values.append(height)
        
        if free_fall_type == 'i':
            acceleration = 9.8 
        elif free_fall_type == 'ii':
            acceleration = calculate_gravity(height)
        elif free_fall_type == 'iii':
            gravity = calculate_gravity(height)
            drag = -np.sign(velocity) * calculate_drag_acceleration(velocity, height, variable_density=False)
            acceleration = gravity + drag
        elif free_fall_type == 'iv':
            gravity = calculate_gravity(height)
            drag = -np.sign(velocity) * calculate_drag_acceleration(velocity, height, variable_density=True)
            acceleration = gravity + drag 
            
        
        velocity += acceleration * dt
        height -= velocity * dt
    
    return x_values, y_values

v_i, h_i = simulate('i')
v_ii, h_ii = simulate('ii')
v_iii, h_iii = simulate('iii')
v_iv, h_iv = simulate('iv')

fig, axs = plt.subplots(1,4, figsize=(20,5))
axs[0].plot(v_i, h_i)
axs[0].set_title("i) Free fall a=-9.8")
axs[0].set_xlabel("Velocity (m/s)")
axs[0].set_ylabel("Height (m)")
axs[0].invert_yaxis()
axs[0].grid(True)

axs[1].plot(v_ii, h_ii)
axs[1].set_title("ii) Varying g")
axs[1].set_xlabel("Velocity (m/s)")
axs[1].invert_yaxis()
axs[1].grid(True)

axs[2].plot(v_iii, h_iii)
axs[2].set_title("iii) Gravity + Drag constant rho")
axs[2].set_xlabel("Velocity (m/s)")
axs[2].invert_yaxis()
axs[2].grid(True)

axs[3].plot(v_iv, h_iv)
axs[3].set_title("iv) Gravity + Drag variable rho")
axs[3].set_xlabel("Velocity (m/s)")
axs[3].invert_yaxis()
axs[3].grid(True)

plt.tight_layout()
plt.show()
