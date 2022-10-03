"""
Preguntas
1) Dada la siguiente lista de elementos. [3, 5, 6, 8, 11, 12, 14, 15, 17, 18]

¿Cuántas comparaciones necesitaría hacer para encontrar la clave 12 haciendo búsqueda secuencial?
Necesitaria hacer 12 comparaciones

¿Cuántas comparaciones necesitaría hacer para encontrar la clave 12 haciendo búsqueda binaria?
Necesitaria hacer 3 comparaciones

¿Cuántas comparaciones necesitaría hacer para encontrar la clave 16 haciendo búsqueda secuencial?
Necesitaria hacer 9 comparaciones. No se encuentra la clave 16.

¿Cuántas comparaciones necesitaría hacer para encontrar la clave 16 haciendo búsqueda binaria?
Necesitaria hacer 3 comparaciones. No se encuentra la clave 16.

Haciendo búsqueda binaria ¿Cual es la secuencia de comparaciones utilizadas para encontrar la clave 15?
(es decir, con que números de la lista va comparando el 15 hasta que termina el proceso de búsqueda)
Secuencia: 11,15

Haciendo búsqueda binaria ¿Cual es la secuencia de comparaciones utilizadas para encontrar la clave 13?
Secuencia: 11,15,12,14


2) Lea 5.3.1 y 5.4.1 ¿Cual es el mejor caso, el peor caso y el caso promedio de la busqueda lineal
y de la búsqueda secuencial?
¿Que algoritmo "es mejor" y por qué?

Busqueda lineal
Mejor caso: que el item que deseamos encontrar este al principio de la lista.
Caso promedio: Que el item se encuentre a la mistad de la lista: len(lista)//2
Peor caso: Que el item se encuentre al final de la lista o que no se encuientre en la lista.

Busqueda binaria
Mejor caso: Encontramos es item a la mitad de la lista: len(lista)//2
Caso promedio: 
Peor caso: Encontramos el item en la comparacion de n/2**i


La busqueda binaria es mas eficiente que la busqueda lineal, 
puesto que se va dividiendo la lista omitiendo varios items y
 de esa manera se realiza una busqueda mas rapida, siempre y cuando la lista este ordenada.


3) ¿Como les fue con la lectura del texto? ¿Qué les costo mas? Pudieron leerlo en una sola sentada?
 ¿subrayaron el texto o elaboraron un resumen?
¿Cuanto tiempo les llevó? ¿Hubieron palabras que no entendieran? ¿Las buscaron en internet?

Me costo mas entender la busqueda binaria, sobre todo entender cual seria su caso promedio. 
Tube que leer varias veces. 
Elabore un resumen
Hubo algunas cosas que no entendia, asi que las busque por internet o youtube.
"""

