import random
import time
import matplotlib.pyplot as plt
from modules.funciones import burbuja
from modules.funciones import quicksort
from modules.funciones import residuo

#medicion de tiempos de ejecucion

tamanos = [1, 50, 100, 300, 500, 700, 1000] #rango de entre 1 y 1000 para poder levantar la curva
tiempo_burbuja = []
tiempo_quicksort = [] #creo listas para alamacenar los tiempos de ejecucion en los distintos tamaños
tiempo_residuo = []
tiempo_sorted = []

for i in tamanos:
    datos = [random.randint(10000, 99999) for _ in range(i)] #creo lista de numeros aleatorios, con tamaño i (i recorre la lista tamanos que va variando)

    copia_burbuja = datos.copy() #copia de la lista original
    inicio = time.time() #comienzo a tomar el tiempo   
    burbuja(copia_burbuja) #ejecuto el algoritmo
    fin = time.time() #finalizo el tiempo
    tiempo_burbuja.append(fin - inicio) #guardo los datos en la lista de tiempo

    copia_quicksort = datos.copy() #copia de la lista original
    inicio = time.time() #comienzo a tomar el tiempo   
    quicksort(copia_quicksort) #ejecuto el algoritmo
    fin = time.time() #finalizo el tiempo
    tiempo_quicksort.append(fin - inicio) #guardo los datos en la lista de tiempo

    copia_residuo = datos.copy() #copia de la lista original
    inicio = time.time() #comienzo a tomar el tiempo   
    residuo(copia_residuo) #ejecuto el algoritmo
    fin = time.time() #finalizo el tiempo
    tiempo_residuo.append(fin - inicio) #guardo los datos en la lista de tiempo

    copia_sorted = datos.copy() #copia de la lista original
    inicio = time.time() #comienzo a tomar el tiempo   
    sorted(copia_sorted) #ejecuto el algoritmo
    fin = time.time() #finalizo el tiempo
    tiempo_sorted.append(fin - inicio) #guardo los datos en la lista de tiempo

plt.figure(figsize=(12, 6))
plt.plot(tamanos, tiempo_burbuja, label = 'Burbuja', color = 'blue')
plt.plot(tamanos, tiempo_quicksort, label = 'Quicksort', color = 'green')
plt.plot(tamanos, tiempo_residuo, label = 'Residuo', color = 'red')
plt.plot(tamanos, tiempo_sorted, label = 'Sorted', color = 'black')
plt.xlabel('Tamaño de la lista')
plt.ylabel('Tiempo de ejecución en segundos')
plt.title('Comparación tiempo de algoritmos de ordenamiento')
plt.legend()
plt.grid(True)
plt.show()

#Como se puede observar en la grafica, el algoritmo de ordenamiento burbuja es más lento, porque tiene dos bucles anidados y entonces es 
# un algoritmo con orden de magnitud O(n^2). En cambio el algoritmo de residuo y quicksort son mucho mas rápidos y no tienen bucles anidados,
# por lo que se puede decir que tienen un orden de magnitud O(1)

#Ahora bien, a priori podríamos analizar esto por lo que mencione anteriormente donde el algoritmo burbuja tiene bucles anidados haciendo referencia
# a que va a ser mas lento y va a tener un O grande mayor. En cambio los otros dos algoritmos no. 

#Comparación con sorted

#Sorted es un método de las listas que crea una lista nueva con los elementos modificados, dejando intacta a la original. Puede ser utilizado
# con cualquier tipo de iterable y mantiene el orden relatico de los elementos que tienen el mismo valor despues de ordenar. Devuelve una nueva
# lista ordenada y, la creación de esta nueva lista tiene un pequeño costo en cuanto a rendimiento. Su complejidad es de O(n log n) y se mantiene
# estable. 

#Funcionamiento de sorted(): Primero inspecciona la lista y se fija si ya hay partes ordenadas, si encuentra partes chicas desordenadas utiliza 
# "insertion sort" para ordenarlas, creando bloques ordenados chicos. Seguidamente fusiona estos bloques pequeños y los hace mas grandes, siguiendo 
# reglas de que fusionar y cuando. Continua fusionando los bloques hasta que la lista se convierte en un unico bloque.





