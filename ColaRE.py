import os
#Antes conocido como alek.py

# Se utiliza el módulo os para limpiar la pantalla según el sistema operativo
os.system('cls' if os.name == 'nt' else 'clear')

# Definición de la clase Cola REcurso limitado
class Cola:
    def __init__(self):
        """Inicializa una nueva cola vacía."""
        self.elementos = []

    def encolar(self, item):
        """Agrega un elemento al final de la cola."""
        self.elementos.append(item)

    def desencolar(self):
        """Elimina y devuelve el cliente que requiere menos recursos."""
        if not self.esta_vacia():
            # Encontrar el cliente con la menor cantidad de recurso
            cliente_min_recursos = min(self.elementos, key=lambda x: x['cantidad_recursos'])
            self.elementos.remove(cliente_min_recursos)
            return cliente_min_recursos
        else:
            raise IndexError("No se puede desencolar de una cola vacía. Fin del programa.")

    def esta_vacia(self):
        """Verifica si la cola está vacía."""
        return len(self.elementos) == 0

    def longitud_cola(self):
        """Devuelve la cantidad de clientes en la cola."""
        return len(self.elementos)

    def mostrar_cola(self):
        """Muestra todos los clientes en la cola."""
        print("Clientes en la cola:")
        for cliente in self.elementos:
            print(f"Nombre: {cliente['nombre']}, Cantidad de recursos: {cliente['cantidad_recursos']}")

    def buscar_cliente(self):
        cliente_buscar = input("Ingrese el nombre del cliente a buscar: ")
        try:
            posicion = [cliente['nombre'] for cliente in self.elementos].index(cliente_buscar)
            print(f"{cliente_buscar} se encuentra en la posición {posicion + 1} en la cola.")
        except ValueError:
            print(f"{cliente_buscar} no se encuentra en la cola.")

    def vaciar_cola(self):
        """Vacía la cola eliminando todos los clientes."""
        self.elementos = []
        print("La cola ha sido vaciada.")

    def agregar_cliente(self):
        nuevo_cliente = input("Ingrese el nombre del nuevo cliente (o '' para salir): ")
        if nuevo_cliente.lower() == '':
            return False
        else:
            cantidad_recursos = int(input(f"Ingrese la cantidad de recursos que necesita {nuevo_cliente}: "))
            self.encolar({'nombre': nuevo_cliente, 'cantidad_recursos': cantidad_recursos})
            return True

    #def recurso_limitado(self):20

# Crear una instancia de la clase Cola
cola = Cola()

# Encolar algunos elementos iniciales en la cola
cola.encolar({'nombre': 'cliente1', 'cantidad_recursos': 5})
cola.encolar({'nombre': 'cliente2', 'cantidad_recursos': 9})
cola.encolar({'nombre': 'cliente3', 'cantidad_recursos': 7})
cola.encolar({'nombre': 'cliente4', 'cantidad_recursos': 3})
cola.encolar({'nombre': 'cliente5', 'cantidad_recursos': 1})

# Mostrar la cola inicial
cola.mostrar_cola()

# Ciclo para realizar operaciones
while True:
    #print(f"Recursos disponibles:")
    print("\nOperaciones:")
    print("1. Agregar cliente")
    print("2. Desencolar y mostrar cliente atendido")
    print("3. Mostrar longitud de la cola")
    print("4. Mostrar todos los clientes en la cola")
    print("5. Buscar un cliente en la cola")
    print("6. Vaciar la cola")
    print("7. Salir")

    opcion = input("Seleccione una opción (1-7): ")

    if opcion == '1':
        cola.agregar_cliente()
    elif opcion == '2':
        cliente_atendido = cola.desencolar()
        print(f"Cliente atendido: {cliente_atendido['nombre']} que necesitaba {cliente_atendido['cantidad_recursos']} recurso(s).")
    elif opcion == '3':
        print("Longitud de la cola:", cola.longitud_cola())
    elif opcion == '4':
        cola.mostrar_cola()
    elif opcion == '5':
        cola.buscar_cliente()
    elif opcion == '6':
        cola.vaciar_cola()
    elif opcion == '7':
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
