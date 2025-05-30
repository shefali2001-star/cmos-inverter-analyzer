import numpy as np
import matplotlib.pyplot as plt

# VTC model: idealized CMOS inverter
def vtc(Vin, VDD=1.8, Vth=0.4):
    return VDD / (1 + (Vin / Vth)**4)

# Static power approximation using resistive switch model
def static_power(Vin, Vout, VDD=1.8, Rn=10e3, Rp=10e3):
    In = (VDD - Vout) / Rn
    Ip = Vout / Rp
    return VDD * (In + Ip)

# Data generation
Vin = np.linspace(0, 1.8, 1000)
Vout = vtc(Vin)

# Plot VTC
plt.plot(Vin, Vout)
plt.title("CMOS Inverter VTC")
plt.xlabel("Vin (V)")
plt.ylabel("Vout (V)")
plt.grid(True)
plt.savefig("vtc_curve.png")
plt.close()

# Plot Static Power
P = static_power(Vin, Vout)
plt.plot(Vin, P * 1e3)
plt.title("Static Power vs Vin")
plt.xlabel("Vin (V)")
plt.ylabel("Power (mW)")
plt.grid(True)
plt.savefig("power_vs_input.png")
plt.close()

# Estimate delay (crude slope-based proxy)
dV = np.gradient(Vout, Vin)
inv_slope = np.max(np.abs(dV))
tau = 1 / inv_slope
print(f"Estimated delay (tau): {tau*1e9:.2f} ns")
