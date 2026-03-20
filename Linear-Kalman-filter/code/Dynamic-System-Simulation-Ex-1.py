## Dynamic System Exercise 1
# This exersice is to simulate a second order Mass Spring Damper system in python, using both contineous and discrete solutions
# The system is defined by the following parameters:
#1. Write a python script to simulate the system shown above in continuous-time using First Order Euler Integration.
#
#Assume the system properties (m = 1, b = 1, k = 10)
#
#Let the system be a unit step force response (f=1) with the initial condition x = 0 m, v = 0 m/s.
#
#Simulate the System for 10 seconds with a time step DT of 0.01 seconds.

import numpy as np
import matplotlib.pyplot as plt

# System parameters
m = 1  # mass (kg)
b = 1  # damping coefficient (N s/m)
k = 10  # spring constant (N/m)

# Simulation parameters
DT = 0.01  # time step (s)
T = 10  # total simulation time (s)
time = np.arange(0, T + DT, DT)  # time vector

# Initialize state variables
x = np.zeros_like(time)  # position (m)
v = np.zeros_like(time)  # velocity (m/s)

# Simulate the system using Euler integration
for i in range(1, len(time)):
    # Calculate the acceleration
    a = (1 - b * v[i-1] - k * x[i-1]) / m  # f = 1 (unit step force)
    
    # Update velocity and position using Euler integration
    v[i] = v[i-1] + a * DT
    x[i] = x[i-1] + v[i-1] * DT

# Plot the results
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(time, x, label='Position (m)')
plt.title('Mass-Spring-Damper System Response')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.grid()
plt.legend()
plt.subplot(2, 1, 2)
plt.plot(time, v, label='Velocity (m/s)', color='orange')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()