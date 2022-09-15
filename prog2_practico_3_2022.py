from posixpath import split
import random
from re import I
from this import d
"""
Programación 2 2022
Tecnicatura en desarrollo de software
Instituto técnico superior córdoba - Anexo villa el libertador
Prof: Matías Bordone
Estudiantes: (Escriba aqui sus nombres)

Práctico 4: Tuplas, diccionarios y conjuntos
Teórico: https://python-para-impacientes.blogspot.com/2014/01/cadenas-listas-tuplas-diccionarios-y.html
"""
# 1 Definir 3 tuplas e imprimir sus elementos.

#a = ("a","d")
#b = ("b","r","y")
#c = ("c","u")

#assert type(a) == tuple
#assert type(b) == tuple
#assert type(c) == tuple



# 2 Definir una función que tome una lista y devuelva el mayor
# y el menor en una tupla (sin usar la funcion min y max)
#def max_min(l:list)->tuple:
#    max = min = l[0]
#    for i in l:
#        if i >= max:
#            max = i
#        if i <= min:
#            min = i
#    return min,max


#assert max_min([3,-1,6,22]) 
#assert max_min([3,6,22]) 


# 3 Hacer un programa, que tome dos listas,
# las convierta en conjuntos y conteste si tiene
# los mismos elementos.
#def mismos_elementos(l1:list,l2:list)->bool:
#    conjunto1 = set(l1)
#    conjunto2 = set(l2)
#    verificacion = conjunto1 <= conjunto2 and conjunto2 <= conjunto1
#    return verificacion

#assert mismos_elementos([1,2,3,4],[4,4,3,3,2,1]) == True
#assert mismos_elementos([1,2,3,4],[4,4,3,3,2]) == False


# 4 Hacer un programa, que tome dos listas,
# las convierta en conjuntos y
# devuelva los elementos de l1 que no están en l2
#def l1_no_l2(l1:list,l2:list)->set:
#    conjunto1 = set(l1)
#    conjunto2 = set(l2)
#    no_estan = conjunto1 - conjunto2
#    return no_estan

#assert l1_no_l2([1,2,3,4],[4,4,3,3,2,1]) == set() #conjunto vacio
#assert l1_no_l2([1,2,3,4],[4,4,3,3,2]) == {1}


# 5.1 definir un diccionario que almacene los nombres de
# países como clave y como valor la cantidad de habitantes.
# Valores a guardar:


#Brasil 210147125
#Colombia 50372424
#Argentina 44938712
#Perú 32131400
#Venezuela 28670000
#Chile 19107216
#Ecuador 17300000
#Bolivia  11383940
#Paraguay 7152703
#Uruguay 3529140
#Guyana 761000
#Surinam 524000
#Guayana Francesa 187000


#d = {'Brasil':210147125,'Colombia':50372424, 'Argentina':44938712,'Perú':32131400,'Venezuela':28670000,
#'Chile':19107216,'Ecuador':17300000,'Bolivia':11383940,'Paraguay':7152703,'Uruguay':3529140,'Guyana':761000,'Surinam':524000,'Guayana Francesa':187000}
#paises = d


#assert d["Argentina"] == 44938712

# 5.2 Implementar una procedimiento para mostrar cada clave y valor.
# (nota) los procedimientos son como las funciones pero no devuelven un valor
#def mostrar_diccionario(d:dict)->None:
#    for k,v in paises.items():
#        print(k,v)


# 5.3 Implementar una función que tome el diccionario,
# calcule la poblacion total de latinoamerica y
# devuelva el valor (pista, usar un for para
# recorrer el diccionario)
#def calcular_poblacion(d:dict)->int:
#    calculo = 0
#    for v in paises:
#        calculo = calculo + paises[v]
#    return calculo
#assert calcular_poblacion(d) == 426204660

# 6

#Escribir un programa que cree un diccionario de traducción inglés-español.
#El programa debe crear un diccionario con las palabras y sus traducciones.

#Después pedirá una frase en inglés y utilizará el diccionario para
#traducirla palabra a palabra.
#Si una palabra no está en el diccionario debe dejarla sin traducir."""

def agregar_palabra(d:dict , ingles:str, esp:str)-> None:
    d = {ingles:esp}
    return d
    


def traducir(d:dict, frase:str) -> str:
    d = {'the':'el','dog':'perro'}
    palabras = frase.split()
    texto = '' 
    for i in palabras:
        if d.get(i):
            texto = d.get(i)
    return texto


dic = {}
agregar_palabra(dic,"dog","perro")
agregar_palabra(dic,"the","el")
agregar_palabra(dic,"eat","comer")
agregar_palabra(dic,"dinner","cena")

#assert traducir(dic,"the dog eat the dinner late") == "el perro comer el cena late"




"""
palabras = frase.split()
    for i in palabras:
        for k in d:
            if i == k:
                texto = d[k]
    traduccion = tuple(texto)    
    return texto
"""

#https://docs.google.com/document/d/1u3QgcH1M3ixEgiA2D9N8hSTIOdUmE0p-7M2Iv8ocoCM/edit