# 3 Hacer un programa, que tome dos listas,
# las convierta en conjuntos y conteste si tiene
# los mismos elementos.
from typing_extensions import Self


def mismos_elementos(l1:list,l2:list)->bool:
    conjunto1 = set(l1)
    conjunto2 = set(l2)
    if conjunto1 == conjunto2:
        valor = True
    else:
        valor = False
    return valor

assert mismos_elementos([1,2,3,4],[4,4,3,3,2,1]) == True
assert mismos_elementos([1,2,3,4],[4,4,3,3,2]) == False

"""
1.A  Implementar una clase llamada AlumnoMateria con las partes Constructor, operaciones y condiciones.
Constructor: nombre, nota, materia
Operaciones: imprimir datos y mostrar_estado() {libre, regular, promocional}
Condiciones: Nombre y materia tiene que ser texto, nota tiene que ser un entero (entre 0 y 10)
"""

class AlumnoMateria:
    def __init__(self, Nombre, Materia, Nota): # Agregar parámetros
        """funcion que inicializa una variable AlumnoMateria
        tener en cuenta las condiciones del TAD (texto e int)
        """
        assert type(Nombre) == str
        assert type(Materia) == str
        assert type(Nota) == int
       

        self.Nombre = Nombre
        self.Materia = Materia
        self.Nota = Nota

    def __str__(self)->str:
        return f"{self.Nombre}, {self.Materia}, {self.Nota}"

    def mostrar_estado(self)->str: 
        """calcula si esta regular, promocionado, o libre"""
        nota = self.Nota
        if self.Nota < 4:
            estado = "Libre"
        elif self.Nota >= 4 and self.nota < 7:
            estado = "Regular"
        else:

        

a = AlumnoMateria ("Nombre", "Materia", 4)
assert a.__str__() == "Juan, Matemáticas, 4"
assert a.mostrar_estado() == "regular"

"""
1.B Implementar la clase registroAlumnoMateria() que guarde varias notas y diga si el alumno está regular, promocional o libre. Con las siguientes reglas.
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