import numpy as np

def trapecio_compuesto(f, a, b, n):
    h = (b - a) / n
    t = np.linspace(a, b, n + 1)
    y = f(t)
    integral = (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])
    return integral

# Definimos la función 
def Q(t):
    return 2 + t**2

a, b = 0, 4
val_exacto = 88 / 3

print(f"Valor exacto: {val_exacto:.4f}\n")

for n in [2, 4, 8]:
    val_aprox = trapecio_compuesto(Q, a, b, n)
    error = abs(val_exacto - val_aprox)
    print(f"n = {n:1d} | Aproximación: {val_aprox:.4f} | Error absoluto: {error:.4f}")


#Al aumentar n (y por ende reducir el paso h), la aproximación lineal que hace la regla del trapecio en cada subintervalo se ajusta cada vez mejor a la curva parabólica de Q(t). 
# Como el error del trapecio es proporcional a h^2, reducir el paso a la mitad reduce el error aproximadamente a la cuarta parte.