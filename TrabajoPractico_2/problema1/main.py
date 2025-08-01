import time
import datetime
from modules.paciente import Paciente
from modules.Heap import MonticuloMin
from modules.Cola import ColaPrioridad
import random

n = 20  # cantidad de ciclos de simulación

cola = ColaPrioridad()
contador_llegada = 1  # Para asignar orden de llegada único

for i in range(n):
    #muestro fecho y hora para cada ciclo de la simulación como si fuera real
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-'*15)
    print('\n', fecha_y_hora, '\n')

    # Se crea un paciente aleatorio y se le asigna orden de llegada
    paciente = Paciente()
    paciente.llegada = contador_llegada
    contador_llegada += 1 # para que cada paciente tenga una hora de llegada única
    cola.agregar(paciente) # lo agrego a la cola de prioridad
    print(f"Llega paciente: {paciente}") #lo muestro 

    # En el 50% de los casos se atiende un paciente de la cola
    # (simulando que se atiende un paciente cada vez que se ejecuta el ciclo)
    if random.random() < 0.5 and not cola.esta_vacia():
        paciente_atendido = cola.eliminar() # el paciente atendido es el de menor riesgo
        # y se lo elimina de la cola
        print('*'*40)
        print('Se atiende el paciente:', paciente_atendido)
        print('*'*40)

    print()
    print('Pacientes que faltan atenderse:', cola.tamanio)
    for idx in range(1, cola.tamanio + 1):
        # empiezo desde q porque en heap binario el primer elemento esta vacio o reservado
        print('\t', cola.cola_prioridad.cola_prioridad[idx]) #muestro pacientes restantes
    print()
    print('-*-'*15)
    time.sleep(1)

# Al final, atender a todos los pacientes restantes
print("\nAtendiendo a todos los pacientes restantes por prioridad:")
while not cola.esta_vacia():
    paciente = cola.eliminar()
    print('Se atiende el paciente:', paciente)

