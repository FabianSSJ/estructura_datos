# Ejemplo de Serie de Fibonacci usando Recursividad
def fibonacci(n):
    if n == 0:  # Primer Caso Base
        return 0
    elif n == 1:  # Segundo Caso Base
        return 1
    else:  # Caso Recursivo
        return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci de 7:", fibonacci(5))  # Debería imprimir 5