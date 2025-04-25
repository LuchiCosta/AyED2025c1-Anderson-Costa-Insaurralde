# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código

def burbuja(lista):
    for i in range(len(lista) - 1): #no definimos una variable con len(lista) para ocupar menos memoria
        for j in range(0, len(lista) - i - 1): #inicio, fin, paso (recorro desde el final hasta el principio, disminuyendo de a 1)
            if lista[j]>lista[j+1]: #si el numero en la posicion j es mayor al siguiente, sucede:
                lista[j], lista[j+1] = lista[j+1], lista[j] #intercambio las posiciones
            
    return lista

def quicksort(lista):
    if len(lista) <= 1: #si la lista tiene un solo elemento o esta vacia, devuelve la lista porque ya esta ordenada
        return lista
    else: 
        pivote = lista[0] #elegimos el elemnto 0 porque si
        menores = [x for x in lista[1:] if x <= pivote] #Se está construyendo una nueva lista llamada menores que contiene todos los elementos de la lista original (excepto el pivote) que son menores o iguales al pivote.
        mayores = [x for x in lista [1:] if x > pivote]  
        return quicksort(menores) + [pivote] + quicksort(mayores) #devuelvo la lista completa uniendo todas las partes

def residuo(lista):
    maximo = max(lista) #busco el maximo para saber cuantos digitos recorremos
    exponente = 1 #empieza en 1
    while maximo // exponente > 0:
        conteo = [0] * 10 #conteo de 10 elementos
        salida = [0] * len(lista) #esta lista guarda elementos de la lista original almacenados

        for i in range(len(lista)):
            indice = lista[i] // exponente #divido el numero en la posicion i por el exponente
            conteo[indice % 10] += 1 #digito en la posicion y luego incremento el contador
        
        for i in range(1, 10):
            conteo[i] += conteo[i - 1] #acumulo valores en la lista de conteo
        
        i = len(lista) - 1 #recorro la lista desde el final hacia el inicio
        while i >= 0:
            indice = lista[i] // exponente #digito en la posicion i
            salida[conteo[indice % 10] - 1] = lista[i] #coloco el numero en la posicion correcta
            conteo[indice % 10] -= 1 #contador para el digito actual
            i -= 1 #muevo al siguiente elemento en la lista original
        
        lista = salida
        exponente *= 10 #paso a la siguiente posicion de digito

    return salida



    # print("funcion 1")
    
# def funcion2():
    # print("funcion 2")

