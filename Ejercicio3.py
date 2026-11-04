import numpy as np

def simpson38_compuesto(f, a, b, n):
    # Consigna 3: Validar que n sea múltiplo de 3
    if n % 3 != 0:
        raise ValueError("Error: El método de Simpson 3/8 requiere que n sea múltiplo de 3.")
        
    h = (b - a) / n
    t = np.linspace(a, b, n + 1)
    y = f(t)
    
    suma = y[0] + y[-1]
    
    # Aplicamos los coeficientes: 2 para los múltiplos de 3, y 3 para el resto
    for i in range(1, n):
        if i % 3 == 0:
            suma += 2 * y[i]
        else:
            suma += 3 * y[i]
            
    integral = (3 * h / 8) * suma
    return integral

# Definimos la función del ejercicio
def v(t):
    return 1 + t**2

a, b = 0, 3
val_exacto = 12.0

print(f"Valor exacto: {val_exacto}\n")

# Evaluamos para n = 3, 6, 9
for n in [3, 6, 9]:
    val_aprox = simpson38_compuesto(v, a, b, n)
    error = abs(val_exacto - val_aprox)
    print(f"n = {n} | Aproximación: {val_aprox:.4f} | Error absoluto: {error:.4f}")

# Descomentar la siguiente línea para probar la validación del múltiplo de 3:
# simpson38_compuesto(v, a, b, 4)