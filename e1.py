from collections import deque
# Creamos una cola vacía
cola = deque()

# Pedimos al usuario que ingrese números
while True:
    try:
        numero = int(input("Ingrese un número (o un carácter para terminar): "))
        # Verificamos si el número es par y positivo
        if numero % 2 == 0 and numero > 0:
            # Insertamos el número en la cola (en el extremo derecho)
            cola.append(numero)
            print(f"{numero} agregado a la cola.")
        elif numero <= 0:
            print("El número debe ser positivo.")
        else:
            print("El número debe ser par.")
    except ValueError:
        # Si el usuario ingresa un carácter, terminamos el bucle
        print("Terminando el programa.")
        break

# Imprimimos la cola
print("\nNúmeros pares positivos pares en la cola:")
print(cola)