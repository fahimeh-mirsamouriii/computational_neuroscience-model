import numpy as np
import matplotlib.pyplot as plt

# Parameters
V_rest, V_th, V_reset = -70.0, -50.0, -80.0
tau_m, g_L = 10.0, 0.1
dt, T = 0.1, 100
t = np.arange(0, T, dt)
v = np.ones(len(t)) * V_rest
I_ext = 2.5 

# Simulation
for i in range(len(t)-1):
    dv = (-(v[i] - V_rest) + I_ext/g_L) * (dt / tau_m)
    v[i+1] = v[i] + dv
    if v[i+1] >= V_th:
        v[i+1] = V_reset

plt.figure(figsize=(8, 4))
plt.plot(t, v, color='navy')
plt.title('LIF Model: Membrane Potential Dynamics')
plt.xlabel('Time (ms)'); plt.ylabel('Voltage (mV)')
plt.grid(True)
plt.show()
