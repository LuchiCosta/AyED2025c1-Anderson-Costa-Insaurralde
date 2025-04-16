# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código

def burbuja(lista):
    for i in range(len(lista)) #no definimos una variable con len(lista) para ocupar menos memoria
        for j in range(len(lista)-1, 0, -1) #inicio, fin, paso (recorro desde el final hasta el principio, disminuyendo de a 1)
            if lista[j]>lista[j+1]: #si el numero en la posicion j es mayor al siguiente, sucede:
                lista[j], lista[j+1] = lista[j+1], lista[j] #intercambio las posiciones
            
            return lista

def quicksort(lista):
    if len(lista) <= 1: #si la lista tiene un solo elemento o esta vacia, devuelve la lista porque ya esta ordenada
        return lista
    else: 
        pivote = lista[3] #elegimos el elemnto 3 porque somos el grupo 3
        menores = [x for x in lista[1:] if x <= pivote] #Se está construyendo una nueva lista llamada menores que contiene todos los elementos de la lista original (excepto el pivote) que son menores o iguales al pivote.
        mayores = [x for x in lista [1:] if x > pivote]  
        return quicksort(menores) + [pivote] + quicksort(mayores) #devuelvo la lista completa uniendo todas las partes

def residuo_aux(lista, exponente):
    output = [0] * len(lista) #lista donde vamos a guardar los elementos ordenados
    count = [0] * 10 #lista para contar cuantas veces aparece cada dígito 

    for i in lista:
        indice = (i // exponente) % 10 #extrae el digito del exponente y lo cuenta en el contador
        count[indice] += 1
    
    for i in range(1, 10):
        count[i] += count[i-1] #acumulo para saber en que posicion del output va cada numero
    
    i = len(lista) - 1
    while i >= 0: #mientras no se llegue al primer elemento
        indice = (lista[i] // exponente) % 10 #busca la decena
        output[count[indice] - 1] = lista[i] #guardo el elemento en la posicion del output
        count[indice] -= 1 #para que el proximo numero se ponga antes

    for i in range(len(lista)):
        lista[i] = output[i] #copio a la lista inicial
    
def residuo(lista):
    max = max(lista) #busco el maximo para saber cuantos digitos recorremos
    exponente = 1 #empieza en 1
    while max // exponente > 0:
        residuo_aux(lista, exponente) #llamo la auxiliar
        exp*=10 #aumento para pasar de unidades a decenas, despues a centenas, etc



    print("funcion 1")
    
def funcion2():
    print("funcion 2")

