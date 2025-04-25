import random
from modules import burbuja
from modules import quicksort
from modules import residuo

lista = [random.randint(10000, 99999) for _ in range(1000)] #creo lista con 1000 numeros aleatorios de 5 cifras

#puse 1000 numeros porque despues pide que probemos con listas de tamaño entre 1 y 1000

lista_burbuja = lista.copy()
lista_quick = lista.copy()
lista_radix = lista.copy() #creo listas para cada algoritmo asi no modifico la inicial


