#Ejercicicio 3: Implementar en un archivo de python la clase cola vista en clase

from ctypes import LittleEndianStructure


class Cola:
    #La cola es una coleccion de datos lineales, FIFO (First in First out)
    def __init__(self):
      self.elementos = []
      
    def agregar(self, item):
        self.elementos.append(item)

    def es_vacia(self)->bool: 
        return self.elementos == []

    def primero(self): # fijarse que no este vacia
        if not self.es_vacia():
            return self.elementos[0]

    def tamanio(self):
        return len(self.elementos)

    def sacar(self):
        if not self.es_vacia():
            return self.elementos.pop(0)
    def __str__(self):
        return ("{}".format(self.elementos))
    
    def imprimir_cola(self) -> None:
        print(self.elementos)

    def reversa (self) -> list:
        n = reversed(self.elementos)
        nuevaLista = list(n)
        self.elementos = nuevaLista
            


p = Cola() # crea una cola (vacia)
print(p.es_vacia()) #True
p.agregar(4) # 
p.agregar('perro')
print(p.elementos) # [4,'perro']
print(p.primero()) # 4
p.agregar(True) # [4,'perro',true]
print(p.tamanio()) # 3
print(p.es_vacia()) #False
p.agregar(8.4) # [4,'perro',true,8.4]
print(p.sacar()) # imprime el 4 y lo saca
print(p.sacar()) # impreme perro y lo saca
print(p.tamanio()) # 2
print(p.imprimir_cola())
print(p.reversa())



# Ejercicio 4: 
# Agregar a la clase cola los siguientes métodos (usando preferentemente los métodos ya utilizados)
#    1. Imprimir cola
#    2. Vaciar la cola.
#    3. Dar vuelta cola
"""
class Cola:
    def __init__(self) -> None:
        self.elementos = []
    
    def imprimir_cola(self) -> None:
        print(self.elementos)
    
    def vaciar_cola(self) -> None:
        self.elementos.clear()
    
    def reversa (self) -> None:
        print(reversed(self.elementos))
        """

# Ejercicio 5:
# Escriba una función que reciba una Cola C1 y mueva sus elementos a una nueva Cola c2, manteniendo el orden de salida de los elementos. Al finalizar la Cola C1 no debe contener elementos.

def trasladar(c1:Cola)->Cola:
    for i in c1:
        

c1 = Cola(2,3,4)
c2 = trasladar(c1)
assert c1.es_vacia == True



