import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# 1. Funciones independientes
def trapecio(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])

def simpson13(f, a, b, n):
    if n % 2 != 0: raise ValueError("n debe ser par")
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return (h / 3) * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])

def simpson38(f, a, b, n):
    if n % 3 != 0: raise ValueError("n debe ser múltiplo de 3")
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    suma = y[0] + y[-1]
    for i in range(1, n):
        if i % 3 == 0: suma += 2 * y[i]
        else: suma += 3 * y[i]
    return (3 * h / 8) * suma

def f(x):
    return np.exp(-x**2)

a, b = 0, 1

# Valor de referencia de alta precisión
ref_val, _ = quad(f, a, b)
print(f"Valor de referencia (SciPy quad): {ref_val:.12f}\n")

# Configuración de pruebas
pruebas_trap_simp13 = [4, 8, 16, 32]
pruebas_simp38 = [3, 6, 12, 24]

resultados = {"Trapecio": ([], []), "Simpson 1/3": ([], []), "Simpson 3/8": ([], [])}

def evaluar_metodo(nombre, metodo, ns):
    print(f"--- {nombre} ---")
    val_ant = None
    for n in ns:
        val = metodo(f, a, b, n)
        err_abs = abs(ref_val - val)
        err_rel = (err_abs / ref_val) * 100
        
        # Estimar error comparando resultados sucesivos
        err_suc = abs(val - val_ant) if val_ant is not None else float('nan')
        val_ant = val
        
        resultados[nombre][0].append(n)
        resultados[nombre][1].append(err_abs)
        
        print(f"n={n:2d} | I={val:.8f} | Err.Abs={err_abs:.2e} | Err.Rel={err_rel:.2e}% | Diferencia Sucesiva={err_suc:.2e}")
    print()

# 2, 3, 4, 5, 6, 7. Ejecución y cálculos
evaluar_metodo("Trapecio", trapecio, pruebas_trap_simp13)
evaluar_metodo("Simpson 1/3", simpson13, pruebas_trap_simp13)
evaluar_metodo("Simpson 3/8", simpson38, pruebas_simp38)

# Gráfico del error absoluto[cite: 3]
plt.figure(figsize=(10, 6))
for nombre, (ns, errores) in resultados.items():
    plt.plot(ns, errores, marker='o', label=nombre)

plt.yscale('log') # Escala logarítmica para visualizar mejor la caída del error
plt.title('Error Absoluto vs Número de Subintervalos (n)')
plt.xlabel('Número de Subintervalos (n)')
plt.ylabel('Error Absoluto (Escala Log)')
plt.legend()
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.show()