import math
math.pi
#TECNICATURA DE DESARROLLO DE SOFTWARE
#NOMBRE Y APELLIDO = AMADO MATIAS ALEXIS
#AÑO LECTIVO = 2022
#SEGUNDO AÑO

"""
1.A  Implementar una clase llamada AlumnoMateria con las partes Constructor, operaciones y condiciones.
Constructor: nombre, nota, materia
Operaciones: imprimir datos y mostrar_estado() {libre, regular, promocional}
Condiciones: Nombre y materia tiene que ser texto, nota tiene que ser un entero (entre 0 y 10)
"""

from glob import escape


class AlumnoMateria:
    def __init__(self, nombre, materia, nota): # Agregar parámetros
        """funcion que inicializa una variable AlumnoMateria
        tener en cuenta las condiciones del TAD (texto e int)
        """
        assert nota <= 10 and nota >= 0
        self.nombre = nombre
        self.materia = materia
        self.nota = nota
        

    def __str__(self)->str:
        return f"{self.nombre}, {self.materia}, {self.nota}"

    def mostrar_estado(self)->str: 
        """calcula si esta regular, promocionado, o libre"""
        nota = self.nota

        if nota < 4:
            estado = "libre"
        
        elif nota <= 6:
            estado = "regular"

        else:
            estado = "promocionado"
        return estado  

a = AlumnoMateria ("Juan", "Matematicas", 4)
assert a.__str__() == "Juan, Matematicas, 4"
assert a.mostrar_estado() == "regular"

"""
1.B Implementar la clase registroAlumnoMateria() que guarde varias notas y diga si el alumno está regular, promocional o libre.
 Con las siguientes reglas.
    Constructor: (Nombre, Materia)
    Agregar nota: Agrega una nota al alumno en la materia
    Promedio: Devuelve el promedio de notas que tiene el alumno
    Devolver lista de notas:
    Condición: Devuelve la condición del alumno {Promocional, Regular o libre}
    Reglas: 
      +  si saca menos de 4 de promedio , queda libre
Promocion promedio de 7 y todas las notas 6 o mas.
Sino Regular:
    Condiciones: Nombre y materia tiene que ser texto, nota tiene que ser un entero
"""
class RegistroAlumnoMateria:
    def __init__(self, nombre, materia): # Agregar parámetros
        """funcion que inicializa una variable registroAlumnoMateria"""
        self.nombre = nombre
        self.materia = materia
        self.notas = []

    def __str__(self):
        return f"{self.nombre}, {self.materia}"

    def agregar_nota(self, nota):
        self.nota = nota
        self.notas.append(self.nota)

    def mostrar_notas(self):
        return f"{self.notas}"

    def calcular_promedio(self):
        for i in self.notas:
            suma = suma + i
        return suma/len(self.notas)

    def mostrar_estado(self)->str: 
        """calcula si esta regular, promocionado, o libre"""
        notas2 = []
        for i in self.notas:
            if i >= 6:
                notas2.append(i)
        if self.calcular_promedio < 4:
            estado = "Libre"
        
        elif self.calcular_promedio >= 7 and len(self.notas) == len(notas2):
            estado = "Promocionado"
        
        else:
            estado = "Regular" 

a = RegistroAlumnoMateria ("Nombre", "Materia")
a.agregar_nota(4)
a.agregar_nota(10)

class Punto:
    """Un punto en el espacio bi dimensional:
    - coordenada x
    - coordenada y
    """
    x = 0 # valor en el eje de las x
    y = 0 # valor en el eje de las y

    def __init__(self, x=0, y=0): # si no paso x e y se considera que el punto es (0,0) 
        self.x = x
        self.y = y

    def __eq__(self, otro)->bool:
        """Devolver True si self es igual a otro."""
        return self.x == otro.x and self.y == otro.y
    
    def es_origen(self)->bool:
        """Me dice si el punto corresponde al origen del plano"""
        return self.x == 0 and self.y == 0
    
    def mover(self,dx:int,dy:int)->None: 
        """Mueve el punto dx lugares en x y dy lugares en y"""
        # (1,2) moverlo 2 a la dercha (dx = 2) y uno arriba (dy = 1) -> (1+2,2+1)
        # (1,2) moverlo 2 a la izquierda (dx = -2) y uno abajo (dy = -1) -> (1-2,2-1)
        self.x = self.x + dx
        self.y = self.y + dy

    def distancia(self,otro)->float:
        # calcula la distancia entre 2 puntos
        # pitagoras -> a**2 + b**2 = h**2
        return ((self.x-otro.x)**2 + (self.y-otro.y)**2)**(1/2)

    def __str__(self):
        """Devolver un string con la representación del punto."""
        return f"({self.x}, {self.y})"

    def distancia_origen(self):
        return ((self.x-0)**2 + (self.y-0)**2)**(1/2)
    
    

#cero = Punto() # (0, 0)
#uno = Punto(1) # (1, 0)
a = Punto(1,2)
print(a)
a.mover(5,3)
print(a)
print(a.es_origen())
b = Punto()
print(b.es_origen())
c = Punto(6,5)
print(c)

"""
2.a A la clase punto vista en la materia agregarle el método Distancia al origen ()siendo el origen el punto (0,0).
 Crear un programa que use este método para imprimir en pantalla la distancia entre al origen de los puntos A, B y C.
"""


A = Punto(2,3)
B = Punto(5,5)
C = Punto(1,5)

A.distancia(B)
assert A.distancia_origen() == 3.605551275463989
assert B.distancia_origen() == 7.0710678118654755
assert C.distancia_origen() == 5.0990195135927845

"""
2.b Utilizando el método de distancia al origen cree una función que 
tome una lista de puntos y devuelva el que se encuentra más alejado del origen.
def mas_lejos(lista:[Punto])->Punto
toma una lista de puntos y devuelve el mas alejado del origen
"""
def mas_lejos(lista:Punto)->Punto:
    candidato = lista.pop(0)
    for i in lista:
        if i.distancia_origen() > candidato.distancia_origen():
            candidato = i
    return candidato


assert mas_lejos([Punto(2,3) , Punto( 5,5 ), Punto(1,5)]) == Punto(5,5)


class Rectangulo():
    """ Esta clase modela un rectángulo en el plano. """

    def __init__(self, base, altura, origen = Punto()):
        """ base (número) es la longitud de su base,
            altura (número) es la longitud de su base,
            origen (Punto) es el punto del plano de su esquina
            inferior izquierda. """
        self.base = base
        self.altura = altura
        self.origen = origen # se encuentra en un punto (asociacion entre rectangulo y punto)

    def trasladar(self, dx = 0, dy = 0):
        self.origen.mover(dx,dy)

    def area(self)-> int:
        return self.base * self.altura

    def __str__(self):
        """ muestra el rectángulo """
        return f"Rectangulo de {self.base} por {self.altura},origen {self.origen}"

    def __eq__(self,otro):
        return self.base == otro.base and self.altura == otro.altura

    def perimetro(self)->int:
        return self.base*2 + self.altura*2


c = Rectangulo (4,4)
print (c)
print("Area",c.area())
print("Perímetro",c.perimetro())
c.trasladar(1,2)
print (c)
p1 =  Punto(2,3)
r = Rectangulo (3,8, p1) 
print(r)
print("Area",r.area())
print("Perímetro",r.perimetro())

"""
3. Crear una clase circulo: 
constructor: punto(x, y), radio; 
operaciones:diametro,  perimetro y area.
"""
#Tomar de ejemplo la clase rectangulo
class Circulo:
    def __init__(self, n, m, radio): # toma un radio , centro
        self.centro = Punto(n,m)
        self.radio = radio
    def diametro ( self ): #radio * 2
        return float(self.radio * 2)

    def perimetro_circulo ( self ): #math.pi () * diametro
        return math.pi * self.diametro()

    def area_circulo (self): #math.pi () * radio
        return math.pi * self.radio**2

    def __eq__(self,otro):
        return self.radio == otro.radio and self.centro == otro.centro
        
    def nover(self,ny,my):
        self.centro.mover(ny,my)

e = Circulo(0,0,4.5)
assert e.diametro() == 9.0
assert e.area_circulo() == 63.61725123519331
assert e.perimetro_circulo() == 28.274333882308138

"""
n estar vacíos. #init
    + Es válido. (los polígonos deben tener más de 2 lados)
    + mover (básicamente es actualizar el atributo origen)
    + __str__ describe el polígono con sus atributos
    + __eq__ define si dos poligonos son iguales (misma cantidad de lados)
 """

class Poligono():
    def __init__(self, lados:int, origen:tuple)->None:
        self.lados = lados
        self.origen = origen
        
    def es_valido(self)->bool:
        return self.lados > 2
    
    def mover (self,n_origen:tuple)->None:
        self.origen = n_origen
    
    def __str__(self)->str:
        return f"Polígono, lados: {self.lados}, origen {self.origen}"
    
    def __eq__(self,otro_pol)->bool:
        return self.lados == otro_pol.lados
        
    
poligono = Poligono (3,(0,0)) # crear un objeto poligono de 3 lados en el punto 0,0
assert poligono.es_valido() == True
assert poligono.origen == (0,0)
poligono.mover((0,1))
assert poligono.origen == (0,1)
assert poligono.__str__() == "Polígono, lados: 3, origen (0, 1)"

poligono2 = Poligono (2,(0,0))
assert poligono2.es_valido() == False

pol3 = Poligono (3,(1,0))
assert poligono == pol3


