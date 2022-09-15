#Guía de ejercicios sobre pilas

#Nombre y Apellido = Amado Matias Alexis
#Año lectivo = 2022
# 2do Año

#1. Implementar en un archivo de python la clase pila




class Pila:
    lista = []

    def estaVacia(self)->bool:
        return self.lista == []


    def incluir(self, item)->None:
        return self.lista.append(item)
    
    def items(self) -> list:
        return self.lista


    def extraer(self):
        return self.lista.pop()


    def inspeccionar(self):
        return self.lista[-1]


    def tamano(self):
        return len(self.lista)
    
    def dar_vuelta(self)->None:
        lista2 = []
        while self.tamano(self) > 0:
            lista2.append(self.extraer())
        self.lista = lista2
        return self.lista

        #otra opcion
        #self.lista[::-1]
    
    def imprimir_pila(self) -> None:
        for item in self.lista:
            print(item)
    
    def vaciar_pila(self) -> None:
        while self.tamano > 0:
            self.extraer()
        return self.lista
    


p = Pila()
p.incluir(4)
p.incluir(2)
p.incluir(1)
assert p.inspeccionar() == 1
assert p.items() == [4, 2, 1]
assert p.extraer() == 1
assert p.inspeccionar() == 2

"""
2. Agregar a la clase pila los siguientes métodos (usando preferentemente los métodos ya utilizados)
    1. Dar vuelta pila
    2. Imprimir pila (imprimir elemento a elemento, no “la lista”)
    3. Vaciar pila.
"""

p = Pila()
p.incluir(4)
p.incluir(2)
p.incluir(1)
assert p.inspeccionar() == 1
assert p.items() == [4, 2, 1]
p.dar_vuelta() == [1,2,4]
assert p.items == [1, 2, 4]
assert p.extraer() == 4
assert p.inspeccionar() == 2
p.vaciar_pila() == []
assert p.estaVacia() == True

"""


3. Usando pilas y la función split escribir una función en python que revierta una cadena de palabras
Entrada: "Mi Diario Python"
Salida: "Python Diario Mi"


4. Usando pilas haga una función que diga si una expresión (un string) tiene la misma cantidad de 0's que de 1's


def contar0y1(palabra:string)->bool:


assert contar0y1(“ajsndakjsdn0asd1”) == True
assert contar0y1(“ajsndakjsdn0asd11”) == False


5. Usando pilas haga una función que diga si una expresión (un string) está balanceado de paréntesis.
Para resolverlo leer:
https://runestone.academy/ns/books/published/pythoned/BasicDS/ParentesisSimplesBalanceados.html
def balanceada(expresion:string)->bool:


assert balanceada(“()()()”) == True
assert balanceada(“()()())”) == False


6. Usando pilas escribir una función en python para encontrar la validez de una cadena de paréntesis, '(', ')', '{', '}', '['']. Los paréntesis deben aparecer en el orden correcto, por ejemplo "()" y "()[]{}" son válidos, pero "[)", "({[)]" y "{{{" son inválidos.
Para resolverla leer:
https://runestone.academy/ns/books/published/pythoned/BasicDS/SimbolosBalanceados%28UnCasoGeneral%29.html


def  balanceada_general(expresion:string)->bool:


assert balanceada_general(“[](()[)]”) == False


7. Usando pilas defina una función que diga si una palabra es capicua.


def capicua(palabra:string)->bool:


assert capicua(“Ala”) == True


8. Implementar la clase pila nuevamente de manera que se comporte de la misma manera , utilizando listas, pero donde el tope no esté en la punta de la lista sino al principio de la lista. Es decir


class Pila2:
         def __init__(self):
             self.items = []


         def estaVacia(self):
             return self.items == []


         def incluir(self, item):
        ## Completar aca ##


         def extraer(self):
        ## Completar aca ##


         def inspeccionar(self):
             return self.items[0]


         def tamano(self):
             return len(self.items)


Pista: Fíjense en el código que estoy escribiendo acá que solamente deberían escribir los métodos incluir y extraer para que lo hagan al principio y no al final de la lista. Para un repaso de las funciones de listas que pueden ayudar revise esta pagina.
http://interactivepython.org/runestone/static/pythoned/Introduction/ComencemosConLosDatos.html#tipos-de-datos-de-colecciones-incorporados
"""