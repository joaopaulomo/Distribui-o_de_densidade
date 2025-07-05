

import numpy as np
import matplotlib.pyplot as plt

G = 6.674e-11
phi = 1e7
alpha = 1e-8
tau = 1.0
rho0 = 13000
r0 = 1e3
R = 6.371e6
dr = 1e4

r_values = [r0]
rho_values = [rho0]
M_values = [0]

r = r0
rho = rho0
M = 0

while r < R and rho > 0:
    dM = 4 * np.pi * r**2 * rho * dr
    M += dM
    drho = (-G * M * rho / (r**2 * phi) + alpha * rho * tau) * dr
    rho += drho
    r += dr
    r_values.append(r)
    rho_values.append(rho)
    M_values.append(M)

r_values = np.array(r_values) / 1e3
rho_values = np.array(rho_values)
M_values = np.array(M_values)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(r_values, rho_values, color='darkblue', label='Densidade ρ(r)')
plt.axhline(5514, color='gray', linestyle='--', label='ρ média da Terra')
plt.xlabel('Raio (km)')
plt.ylabel('Densidade (kg/m³)')
plt.title('Perfil de Densidade - Método de Euler')
plt.grid(True)
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(r_values, M_values / 1e24, color='darkgreen', label='Massa M(r)')
plt.axhline(5.972, color='gray', linestyle='--', label='Massa total da Terra (10²⁴ kg)')
plt.xlabel('Raio (km)')
plt.ylabel('Massa acumulada (10²⁴ kg)')
plt.title('Massa acumulada dentro da Terra')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
