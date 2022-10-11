
import time
"""
Análisis de algoritmos
Leer obligatoriamente https://runestone.academy/ns/books/published/pythoned/AlgorithmAnalysis/toctree.html
2.1,2.2,2.3


1) Escriba las siguientes definiciones.

notación O-grande: Es un metodo que nos ayuda a describir el comportamuento de nuestro algoritmo

peor caso : Es cuando nuestro algoritmo se comporta muy mal o utiliza demaciados recursos
mejor caso : Es cuando nuestro algoritmo se comporta eficientemente excepcional
caso promedio: El caso promedio es un intermedio de el mejor caso y el caso promedio


logarítmica: cuando el Crecimiento es muy lento o minimo, el tiempo de ejecucion es de log n 2
lineal: El tiempo de ejecucion es proporcional a la cantidad de datos que resiba (n)
log-lineal: Es hibrido (logaritmico y lineal), el tiempo de ejecucion seria de n * log 2 n.
cuadrática: El tiempo de ejecucion es de n**2
exponencial: Es el peor de todos. El tiempo de ejecucion es de 2**n

2)  Indique el desempeño O-grande de los siguientes fragmento de código para ello:
    + interprete la cantidad de acciones en una función
    + Modifique el còdigo para calcular el tiempo de ejecución y haga una gráfica que le permita visualizarlo.	
"""
#a)
def f(n):
   inicio = time.time()
   for i in range(n):
         for j in range(n):
            k = 2 + 2
   fin = time.time()
   return inicio - fin
f(200)

"numero de acciones = n * n * 1 = n**2"




#b)
def f2(n):
   inicio = time.time()
   for i in range(n):
      k = 2 + 2
   fin = time.time()
   return inicio - fin
#c)
f2(200)

"numero de acciones = n * 1 = n"

def f3(n):
   inicio = time.time()
   i = n
   while i > 0:
   	k = 2 + 2 
      i = i // 2
   fin = time.time()
   return inicio - fin

"En caso de que n valga 5"
"""
1ra iteración i=5; 
2da iteración i=2; 
3ra iteración i=1; 
4ta iteración i=0; 
"""


f3(5)


"""
d)
"""
def f4(n):
   inicio = time.time()
   for i in range(n):
      for j in range(n):
         for k in range(n):
            k = 2 + 2
   fin = time.time()


"numero de acciones = n * n * n * 1 = n**3 "


f(100)

"""
f)
"""
def f6(n):
   inicio = time.time()
   for i in range(n):
      k = 2 + 2
   for j in range(n):
      k = 2 + 2
   for k in range(n):
      k = 2 + 2
   fin = time.time()

"numero de acciones = n * 1 + n * 1 + n * 1 = 3n"

"""

3) ¿Como les fue con la lectura del texto?¿Qué les costo mas?
Me costo entender el concepto de Notacion O-grande y de como implementarlo. 

 Pudieron leerlo en una sola sentada? ¿subrayaron el texto o elaboraron un resumen?
Elavore un resumen, lo lei varias veces

¿Cuanto tiempo les llevó? ¿Hubieron palabras que no entendieran? ¿Las buscaron en internet?
Me llevo 3 dias realizar las actividades. Tuve que buscar en youtube alguna explicacion mas facil de entender sobre Notacion O-grande.
"""



