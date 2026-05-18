
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

fs = 1_000  # Sampling frequency (Hz)
t_sig = np.arange(0, 2, 1/fs)

# Mixed signal: 10Hz (Alpha) + 40Hz (Gamma) + Noise
sig = (np.sin(2*np.pi*10*t_sig) + 
       0.5*np.sin(2*np.pi*40*t_sig) + 
       np.random.normal(0, 1, len(t_sig)))

# Welch's method for PSD
freqs, psd = signal.welch(sig, fs, nperseg=1024)

plt.figure(figsize=(8, 4))
plt.semilogy(freqs, psd, color='darkorange')
plt.xlim(0, 100)
plt.grid(True, alpha=0.3)
plt.title('Power Spectral Density: Identifying Brain Rhythms')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')
plt.show()
