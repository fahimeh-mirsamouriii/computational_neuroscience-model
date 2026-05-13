import numpy as np
import matplotlib.pyplot as plt

# Membrane capacitance (microF/cm^2)
C = 1.0
# Maximum conductances (mS/cm^2)
g_Na = 120.0   # Sodium
g_K = 36.0     # Potassium
g_L = 0.3      # Leak
# Reversal potentials (mV)
E_Na = 50.0    # Sodium
E_K = -77.0    # Potassium
E_L = -54.4    # Leak

# Rate functions (Alpha and Beta)
def alpha_m(V): return 0.1 * (V + 40.0) / (1.0 - np.exp(-(V + 40.0) / 10.0))
def beta_m(V):  return 4.0 * np.exp(-(V + 65.0) / 18.0)
def alpha_h(V): return 0.07 * np.exp(-(V + 65.0) / 20.0)
def beta_h(V):  return 1.0 / (1.0 + np.exp(-(V + 35.0) / 10.0))
def alpha_n(V): return 0.01 * (V + 55.0) / (1.0 - np.exp(-(V + 55.0) / 10.0))
def beta_n(V):  return 0.125 * np.exp(-(V + 65.0) / 80.0)

# Simulation settings
T = 50.0           # Total time (ms)
dt = 0.01          # Time step (ms)
t = np.arange(0, T, dt)
V = np.zeros(len(t))
m = np.zeros(len(t))
h = np.zeros(len(t))
n = np.zeros(len(t))

# Initial conditions (resting state)
V[0] = -65.0
m[0] = alpha_m(V[0]) / (alpha_m(V[0]) + beta_m(V[0]))
h[0] = alpha_h(V[0]) / (alpha_h(V[0]) + beta_h(V[0]))
n[0] = alpha_n(V[0]) / (alpha_n(V[0]) + beta_n(V[0]))

# Input current — enough to trigger firing
I_ext = 10.0

# Euler integration loop
for i in range(1, len(t)):
    # Ionic currents
    I_Na = g_Na * (m[i-1]**3) * h[i-1] * (V[i-1] - E_Na)
    I_K = g_K * (n[i-1]**4) * (V[i-1] - E_K)
    I_L = g_L * (V[i-1] - E_L)

    # Update membrane potential
    dVdt = (I_ext - I_Na - I_K - I_L) / C
    V[i] = V[i-1] + dVdt * dt

    # Update gating variables
    m[i] = m[i-1] + (alpha_m(V[i-1]) * (1 - m[i-1]) - beta_m(V[i-1]) * m[i-1]) * dt
    h[i] = h[i-1] + (alpha_h(V[i-1]) * (1 - h[i-1]) - beta_h(V[i-1]) * h[i-1]) * dt
    n[i] = n[i-1] + (alpha_n(V[i-1]) * (1 - n[i-1]) - beta_n(V[i-1]) * n[i-1]) * dt

# Plot results
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t, V, 'b')
plt.title('Hodgkin-Huxley Neuron Model')
plt.ylabel('Membrane Potential (mV)')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(t, m, label='m (Na⁺ activation)')
plt.plot(t, h, label='h (Na⁺ inactivation)')
plt.plot(t, n, label='n (K⁺ activation)')
plt.xlabel('Time (ms)')
plt.ylabel('Gate Probability')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
