def busquedaSecuencial(unaLista, item):
	pos = 0
	encontrado = False
	
	while pos < len(unaLista) and not encontrado:
	    if unaLista[pos] == item:
	        encontrado = True
	    else:
	        pos = pos+1
	
	return encontrado
	
listaPrueba = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(len(listaPrueba))
print(busquedaSecuencial(listaPrueba, 3))
print(busquedaSecuencial(listaPrueba, 13))


#Funcion para realizar una busqueda secuencial
def busquedaSecuencialOrdenada(unaLista, item):
    pos = 0
    encontrado = False
    parar = False
    while pos < len(unaLista) and not encontrado and not parar:
        if unaLista[pos] == item:
            encontrado = True
        else:
            if unaLista[pos] > item:
                parar = True
            else:
                pos = pos+1
	
    return encontrado
	
listaPrueba = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(busquedaSecuencialOrdenada(listaPrueba, 3))
print(busquedaSecuencialOrdenada(listaPrueba, 13))


#Funcion para una busqueda binaria

def busquedaBinaria(unaLista, item):
    primero = 0
    ultimo = len(unaLista)-1
    encontrado = False
	
    while primero<=ultimo and not encontrado:
        puntoMedio = (primero + ultimo)//2
        print(unaLista[puntoMedio])
        if unaLista[puntoMedio] == item:
            encontrado = True
        
        else:
            if item < unaLista[puntoMedio]:
                ultimo = puntoMedio-1
            else:
                primero = puntoMedio+1
	
    return encontrado

listaPrueba = [3, 5, 6, 8, 11, 12, 14, 15, 17, 18]
print(busquedaBinaria(listaPrueba, 12))
print(busquedaBinaria(listaPrueba, 16))
print(busquedaBinaria(listaPrueba, 15))
print(busquedaBinaria(listaPrueba, 13))