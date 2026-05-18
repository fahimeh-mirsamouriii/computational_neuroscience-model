import numpy as np
import matplotlib.pyplot as plt

# 1. Simulation parameters and time steps
dt = 0.1 # Time step (ms)
t_max = 100.0 # Total simulation time (ms)
t = np.arange(0, t_max, dt) # Time vector

# 2. Post-synaptic neuron biophysical parameters
V_rest = -70.0 # Membrane resting potential (mV)
tau_m = 20.0 # Membrane time constant (ms)
g_L = 10.0 # Leak conductance (nS)

# 3. Synaptic parameters
tau_s = 2.0 # Synaptic time constant (ms)
E_rev = 0.0 # Reversal potential for excitatory synapse (mV)
w = 0.5 # Synaptic weight / maximum conductance
t_spike = 20.0 # Time of the pre-synaptic spike (ms)

# 4. Initialize arrays
g_syn = np.zeros(len(t))
v_post = np.ones(len(t)) * V_rest

# 5. Main simulation loop (Forward Euler method)
for i in range(len(t)-1):
    # Calculate synaptic conductance using the Alpha function after the spike
    if t[i] >= t_spike:
        rel_t = t[i] - t_spike
        g_syn[i] = w * (rel_t / tau_s) * np.exp(1 - rel_t / tau_s)
    
    # Membrane voltage differential equation
    dv_post = (-(v_post[i] - V_rest) - g_syn[i] * (v_post[i] - E_rev) / g_L) * (dt / tau_m)
    v_post[i+1] = v_post[i] + dv_post

# 6. Plot the EPSP result
plt.figure(figsize=(8, 4))
plt.plot(t, v_post, color='crimson', linewidth=2, label='Post-synaptic Membrane Potential')
plt.axvline(x=t_spike, color='gray', linestyle='--', label='Pre-synaptic Spike')
plt.title('Post-Synaptic Potential (EPSP) Simulation')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (mV)')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)
plt.show()
