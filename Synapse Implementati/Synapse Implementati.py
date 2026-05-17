tau_s, E_rev, w = 2.0, 0.0, 0.5
g_syn = np.zeros(len(t))
v_post = np.ones(len(t)) * V_rest
t_spike = 20.0 # Hypothetical pre-synaptic spike

for i in range(len(t)-1):
    if t[i] >= t_spike:
        rel_t = t[i] - t_spike
        g_syn[i] = w * (rel_t / tau_s) * np.exp(1 - rel_t / tau_s)
    
    dv_post = (-(v_post[i] - V_rest) - g_syn[i]*(v_post[i] - E_rev)/g_L) * (dt / tau_m)
    v_post[i+1] = v_post[i] + dv_post

plt.figure(figsize=(8, 4))
plt.plot(t, v_post, color='crimson')
plt.title('Post-Synaptic Potential (EPSP)')
plt.xlabel('Time (ms)'); plt.ylabel('Voltage (mV)')
plt.show()
