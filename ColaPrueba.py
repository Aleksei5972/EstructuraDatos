import os
os.system('cls' if os.name == 'nt' else 'clear')

class Cola:
    def __init__(self):
        self.elementos =[]

    def encolar(self, item):
        self.elementos.append(item)

    def recurso(self, item):
        self.elementos.append(item)

    def prioridad(self, item):
        self.elementos.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)
        else:
            raise indexError("Desencolar de una cola vacia")

    def esta_vacia(self):
        return len(self.elementos) == 0

#Uso de la Cola
cola = Cola()
cola.encolar(4)
cola.encolar('Perro')
cola.encolar(True)
print("Elemento desencolado", cola.desencolar())
