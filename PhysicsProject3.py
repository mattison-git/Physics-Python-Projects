import numpy as np
import matplotlib.pyplot as plt


mass = 5
spring_constant = 100
dt = 0.01
time = 10  


x_position = 0.0
velocity = 3.0


times = [0.0]
list_of_x = [x_position]
list_of_velocity = [velocity]


while times[-1] < time:
    acceleration = -(spring_constant/mass) * x_position
    velocity = velocity + acceleration * dt
    x_position = x_position + velocity * dt
    times.append(times[-1] + dt)
    list_of_x.append(x_position)
    list_of_velocity.append(velocity)


plt.figure(figsize=(10,5))
plt.subplot(2,1,1)
plt.plot(times, list_of_x)
plt.ylabel("x (m)")
plt.title("Graph of mass-spring system")

plt.subplot(2,1,2)
plt.plot(times, list_of_velocity)
plt.ylabel("v (m/s)")
plt.xlabel("t (s)")
plt.show()
