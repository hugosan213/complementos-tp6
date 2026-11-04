import numpy as np

def simpson13_compuesto(f, a, b, n):
    # Consigna 3: Verificar que el programa rechace valores impares de n
    if n % 2 != 0:
        raise ValueError("Error: El método de Simpson 1/3 requiere un número par de subintervalos (n).")
        
    h = (b - a) / n
    t = np.linspace(a, b, n + 1)
    y = f(t)
    
    # Aplicamos los coeficientes: 1 para los extremos, 4 para los impares, 2 para los pares
    integral = (h / 3) * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])
    return integral

# Definimos la función del ejercicio
def P(t):
    return 1 + t**3

a, b = 0, 2
val_exacto = 6.0

print(f"Valor exacto: {val_exacto}\n")

# Evaluamos para n = 2, 4, 8
for n in [2, 4, 8]:
    val_aprox = simpson13_compuesto(P, a, b, n)
    error = abs(val_exacto - val_aprox)
    print(f"n = {n} | Aproximación: {val_aprox:.4f} | Error absoluto: {error:.4f}")

# Descomentar la siguiente línea para probar el rechazo de n impar:
# simpson13_compuesto(P, a, b, 3)