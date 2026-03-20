# 2.  Write a python script to simulate the system shown above in discrete-time using the Matrix Exponential Discretisation method for a timestep size of 0.1 seconds.
#
# Assume the system properties (m = 1, b = 1, k = 10)
#
# Let the system be a unit step force response (f=1) with the initial condition x = 0 m, v = 0 m/s.

# Simulate the System for 10 seconds.

# (Hint: You can use "from scipy.linalg import expm" and then "E = expm(Y)" to calculate the matrix exponential for matrix Y)

# The system response should look the same as before.

import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import expm

# System parameters
m = 1  # mass (kg)
b = 1  # damping coefficient (N s/m)
k = 10  # spring constant (N/m)

# Simulation parameters
DT = 0.5  # time step (s)
T = 10  # total simulation time (s)
time = np.arange(0, T + DT, DT)  # time vector

# State-space representation
A = np.array([[0, 1], [-k/m, -b/m]])  # system matrix
B = np.array([[0], [1/m]])  # input matrix

# Initialize state variables
x = np.zeros_like(time)  # position (m)
v = np.zeros_like(time)  # velocity (m/s)

# Simulate the system using Matrix Exponential Discretisation
for i in range(1, len(time)):
    # Calculate the matrix exponential for the current time step
    Y = np.block([[A, B], [np.zeros((1, 3))]]) * DT
    E = expm(Y)
    
    # Update state using the discretized system
    state = np.array([[x[i-1]], [v[i-1]], [1]])  # current state with input
    new_state = E @ state  # new state after time step
    
    x[i] = new_state[0, 0]  # update position
    v[i] = new_state[1, 0]  # update velocity

# Plot the results
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(time, x, label='Position (m)')
plt.title('Mass-Spring-Damper System Response (Discrete-Time)')
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
