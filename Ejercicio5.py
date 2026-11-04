import numpy as np
from scipy.integrate import quad

# Reutilizamos las funciones base
def trapecio(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])

def simpson13(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return (h / 3) * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])

def simpson38(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    suma = y[0] + y[-1]
    for i in range(1, n):
        if i % 3 == 0: suma += 2 * y[i]
        else: suma += 3 * y[i]
    return (3 * h / 8) * suma

# Definimos la función del polinomio de grado 5
def f5(x):
    return 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5

a, b = 0, 0.8
# Calculamos el valor exacto como referencia
val_exacto, _ = quad(f5, a, b)
print(f"Valor exacto de la integral (referencia): {val_exacto:.6f}\n")

# a) Con la regla del Trapecio simple (n=1)
print(f"a) Trapecio (n=1): {trapecio(f5, a, b, 1):.6f}")

# b) Con la regla del Trapecio múltiple (n=2)
print(f"b) Trapecio (n=2): {trapecio(f5, a, b, 2):.6f}")

# c) Regla de Simpson 1/3 simple (n=2)
print(f"c) Simpson 1/3 (n=2): {simpson13(f5, a, b, 2):.6f}")

# d) Regla de Simpson 1/3 múltiple (n=4)
print(f"d) Simpson 1/3 múltiple (n=4): {simpson13(f5, a, b, 4):.6f}")

# e) Regla de Simpson 3/8 (n=3)
print(f"e) Simpson 3/8 (n=3): {simpson38(f5, a, b, 3):.6f}")

# f) Regla combinada (Simpson 3/8 + Simpson 1/3) con n=5
# Dividimos el dominio en 5 subintervalos: usamos Simpson 3/8 para los primeros 3 (x0 a x3)
# y Simpson 1/3 para los últimos 2 (x3 a x5).
h_comb = (b - a) / 5
x_comb = np.linspace(a, b, 6)
I_38 = simpson38(f5, x_comb[0], x_comb[3], 3)
I_13 = simpson13(f5, x_comb[3], x_comb[5], 2)
print(f"f) Combinada S3/8 + S1/3 (n=5): {I_38 + I_13:.6f}")