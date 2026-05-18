import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.integrate import odeint


def fhn(v, w, I):
    """FHN model equations"""
    dv = v - (v**3)/3 - w + I
    dw = (v + 0.7 - 0.8*w) / 12.5
    return np.array([dv, dw])

# Phase Plane Grid
v_vals = np.linspace(-2.5, 2.5, 25)
w_vals = np.linspace(-1, 1.5, 25)
V, W = np.meshgrid(v_vals, w_vals)
dV, dW = fhn(V, W, I=0.5)

# Normalize for streamplot
speed = np.sqrt(dV**2 + dW**2)
dV_norm, dW_norm = dV/speed, dW/speed

plt.figure(figsize=(10, 7))

# Vector field
plt.streamplot(V, W, dV, dW, color='lightgray', arrowsize=1.2)

# v-nullcline: dv/dt = 0 → w = v - v³/3 + I
I = 0.5
v_nullcline = v_vals - (v_vals**3)/3 + I
plt.plot(v_vals, v_nullcline, 'r-', lw=2.5, label='v-nullcline (dv/dt=0)')

# w-nullcline: dw/dt = 0 → w = (v + 0.7)/0.8
w_nullcline = (v_vals + 0.7) / 0.8
plt.plot(v_vals, w_nullcline, 'g-', lw=2.5, label='w-nullcline (dw/dt=0)')

# Fixed point (intersection)
from scipy.optimize import fsolve
def fixed_point_eq(x):
    v, w = x
    return [v - v**3/3 - w + I, (v + 0.7 - 0.8*w) / 12.5]
v_fp, w_fp = fsolve(fixed_point_eq, [0, 0.5])
plt.plot(v_fp, w_fp, 'ko', ms=10, label=f'Fixed Point ({v_fp:.2f}, {w_fp:.2f})')

# Limit Cycle (trajectory)
t = np.linspace(0, 200, 5000)
IC = [1.5, 0.5]  # Initial condition
traj = odeint(lambda y, t: fhn(y[0], y[1], I), IC, t)
plt.plot(traj[:, 0], traj[:, 1], 'b-', lw=1.5, alpha=0.8, label='Limit Cycle')

plt.title('FitzHugh-Nagumo: Phase Plane with Nullclines & Limit Cycle', fontsize=12)
plt.xlabel('v (Membrane Voltage)', fontsize=11)
plt.ylabel('w (Recovery Variable)', fontsize=11)
plt.legend(loc='upper left')
plt.xlim(-2.5, 2.5)
plt.ylim(-1, 1.5)
plt.grid(True, alpha=0.3)
plt.show()



# Print peak frequencies
peak_idx = np.argmax(psd[freqs < 100])
print(f"Peak frequency: {freqs[peak_idx]:.1f} Hz")
