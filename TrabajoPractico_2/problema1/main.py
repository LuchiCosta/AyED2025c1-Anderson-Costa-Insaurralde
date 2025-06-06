import time
import datetime
from modules.paciente import Paciente
from modules.Cola_prioridad import ColaPrioridad
import random

n = 5  # cantidad de ciclos de simulación

cola = ColaPrioridad()
contador_llegada = 1  # Para asignar orden de llegada único

for i in range(n):
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-'*15)
    print('\n', fecha_y_hora, '\n')

    # Se crea un paciente aleatorio y se le asigna orden de llegada
    paciente = Paciente()
    paciente.llegada = contador_llegada
    contador_llegada += 1
    cola.agregar(paciente)
    print(f"Llega paciente: {paciente}")

    # En el 50% de los casos se atiende un paciente
    if random.random() < 0.5 and not cola.esta_vacia():
        paciente_atendido = cola.eliminar()
        print('*'*40)
        print('Se atiende el paciente:', paciente_atendido)
        print('*'*40)

    print()
    print('Pacientes que faltan atenderse:', cola.tamanio)
    for idx in range(1, cola.tamanio + 1):
        print('\t', cola.cola_prioridad[idx])
    print()
    print('-*-'*15)
    time.sleep(1)

# Al final, atender a todos los pacientes restantes
print("\nAtendiendo a todos los pacientes restantes por prioridad:")
while not cola.esta_vacia():
    paciente = cola.eliminar()
    print('Se atiende el paciente:', paciente)

