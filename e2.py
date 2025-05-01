from collections import deque

def sumar_cola(cola):
    """
    Suma los elementos de una cola.

    Args:
        cola: Una cola (deque) de números.

    Returns:
        La suma de los elementos de la cola.
    """
    suma = 0
    for elemento in cola:
        suma += elemento
    return suma

# Solicitar al usuario que ingrese los números
cola = deque()
while True:
    try:
        numero = int(input("Ingresa un número (o presiona Enter para terminar): "))
        cola.append(numero)
    except ValueError:
        break

# Calcular la suma
resultado = sumar_cola(cola)

# Mostrar el resultado
print(f"La suma de los elementos de la cola es: {resultado}")