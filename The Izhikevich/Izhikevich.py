# Parameters for Regular Spiking (RS)
a, b, c, d = 0.02, 0.2, -65, 8
v_izh = -65.0
u_izh = b * v_izh
v_trace = []

for _ in t:
    v_izh += (0.04*v_izh**2 + 5*v_izh + 140 - u_izh + I_ext) * dt
    u_izh += a * (b*v_izh - u_izh) * dt
    if v_izh >= 30:
        v_trace.append(30); v_izh = c; u_izh += d
    else:
        v_trace.append(v_izh)

plt.figure(figsize=(8, 4))
plt.plot(t, v_trace, color='darkgreen')
plt.title('Izhikevich Model: Regular Spiking Pattern')
plt.xlabel('Time (ms)'); plt.ylabel('Voltage (mV)')
plt.show()
