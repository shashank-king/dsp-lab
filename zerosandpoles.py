import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Define symbolic variable
n, z = sp.symbols('n z')

# Define the input sequence (modify this sequence as per your requirement)
sequence = (1/2)**n  # Example: Sequence is (1/2)^n

# Compute the Z-transform
Z_transform = sp.summation(sequence * z**(-n), (n, 0, sp.oo))
print("Z-transform:", Z_transform)

# Convert Z-transform to a transfer function form (numerator, denominator)
# Example: Z-transform gives (z/(z - 1/2))
numerator, denominator = sp.fraction(Z_transform)

# Get coefficients of numerator and denominator
num_coeff = sp.Poly(numerator, z).all_coeffs()
den_coeff = sp.Poly(denominator, z).all_coeffs()

# Convert to float for plotting
num_coeff = [float(c) for c in num_coeff]
den_coeff = [float(c) for c in den_coeff]

# Compute zeros, poles using scipy
system = signal.TransferFunction(num_coeff, den_coeff, dt=True)
zeros, poles = system.zeros, system.poles

# Print zeros and poles
print("Zeros:", zeros)
print("Poles:", poles)

# Plot zeros and poles
plt.figure()
plt.scatter(np.real(zeros), np.imag(zeros), s=100, color='blue', label='Zeros')
plt.scatter(np.real(poles), np.imag(poles), s=100, color='red', label='Poles')
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.title('Zeros and Poles of the Z-transform')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.grid()
plt.legend()
plt.show()