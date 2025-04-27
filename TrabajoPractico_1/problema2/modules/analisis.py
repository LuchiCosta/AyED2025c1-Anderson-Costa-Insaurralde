import time
import matplotlib.pyplot as plt
from claseLista import ListaDobleEnlazada

def medir_tiempos():
    tamanos = [1, 50, 100, 200, 300, 500, 700, 1000]  # De 1 a 1000 elementos
    tiempos_len = []
    tiempos_copiar = []
    tiempos_invertir = []

    for n in tamanos:
        lista = ListaDobleEnlazada()
        for i in range(n):
            lista.agregar_al_final(i)

        inicio = time.time()
        len(lista)
        tiempos_len.append(time.time() - inicio)

        inicio = time.time()
        lista.copiar()
        tiempos_copiar.append(time.time() - inicio)

        inicio = time.time()
        lista.invertir()
        tiempos_invertir.append(time.time() - inicio)

    plt.figure(figsize=(12, 6))
    plt.plot(tamanos, tiempos_len, label="len()", color='violet')
    plt.plot(tamanos, tiempos_copiar, label="copiar()", color='pink')
    plt.plot(tamanos, tiempos_invertir, label="invertir()", color='red')
    plt.xlabel("Tamaño de la lista (N)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Tiempos de ejecución de métodos en Lista Doblemente Enlazada")
    plt.legend()
    plt.grid(True)
    plt.show()
    plt.savefig('figuraDeAnalisis.jpg')

medir_tiempos()

