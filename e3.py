class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            return None

    def mostrar(self):
        return self.items

    def __len__(self):
        return len(self.items)

# Función para eliminar múltiplos de 3 de una cola
def eliminar_multiplos_de_3(cola):
    cola_nueva = Cola()
    while not cola.esta_vacia():
        item = cola.desencolar()
        if item % 3 != 0:  # Si no es múltiplo de 3
            cola_nueva.encolar(item)
    return cola_nueva

# Programa principal
if __name__ == "__main__":
    cola = Cola()

    # Ingresar números por teclado
    while True:
        try:
            numero = int(input("Ingrese un número (o presione Enter para terminar): "))
            cola.encolar(numero)
        except ValueError:
            break  # Terminar la entrada si no es un número

    # Mostrar la cola original
    print("Cola original:", cola.mostrar())

    # Eliminar múltiplos de 3
    cola_sin_multiplos = eliminar_multiplos_de_3(cola)

    # Mostrar la cola sin múltiplos de 3
    print("Cola sin múltiplos de 3:", cola_sin_multiplos.mostrar())