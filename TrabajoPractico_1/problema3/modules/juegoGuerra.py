# juegoGuerra.py
import random

N_TURNOS = 10000

class Carta:
    valores = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'A':14}

    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo
    
    def _valor_numerico(self):
        return Carta.valores[self.valor]

    def __gt__(self, otra):
        if otra is None:
            return True
        return self._valor_numerico() > otra._valor_numerico()
    
    def __lt__(self, otra):
        if otra is None:
            return False
        return self._valor_numerico() < otra._valor_numerico()

    def __eq__(self, otra):
        if otra is None:
            return False
        return self._valor_numerico() == otra._valor_numerico()

    def __str__(self):
        return f"{self.valor}{self.palo}"

    def __repr__(self):
        return str(self)


class DequeEmptyError(Exception):
    pass


class Mazo:
    def __init__(self):
        self.cartas = []
    
    def poner_carta_arriba(self, carta):
        self.cartas.append(carta)
    
    def poner_carta_abajo(self, carta):
        self.cartas.insert(0, carta)
    
    def sacar_carta_arriba(self, mostrar=False):
        if len(self.cartas) == 0:
            raise DequeEmptyError("El mazo está vacío")
        return self.cartas.pop()
    
    def __len__(self):
        return len(self.cartas)
    
    def __str__(self):
        return ', '.join(str(c) for c in reversed(self.cartas))  # para mostrar de arriba a abajo

    def __repr__(self):
        return str(self)


class JuegoGuerra:
    
    valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A'] 
    palos = ['♠', '♥', '♦', '♣']
    
    def __init__(self, random_seed = 0):
        self._mazo_inicial = Mazo()
        self.mazo_1 = Mazo()
        self.mazo_2 = Mazo()
        self._guerra = False
        self._ganador = ''
        self._empate = False
        self._turno = 0
        self._cartas_en_la_mesa = []
        self._seed = random_seed
    
    @property
    def empate(self):
        return self._empate
        
    @empate.setter
    def empate(self, valor):
        self._empate = valor
        
    @property
    def turnos_jugados(self):
        if self.empate:
            return N_TURNOS
        return self._turno + 1
           
    @property
    def ganador(self):
        return self._ganador
        
    def armar_mazo_inicial(self):
        random.seed(self._seed)
        cartas = [Carta(valor, palo) for valor in JuegoGuerra.valores for palo in JuegoGuerra.palos]
        random.shuffle(cartas)
        for carta in cartas:
            self._mazo_inicial.poner_carta_arriba(carta)
        return self._mazo_inicial
    
    def repartir_cartas(self):
        while len(self._mazo_inicial):
            carta_1 = self._mazo_inicial.sacar_carta_arriba()
            self.mazo_1.poner_carta_arriba(carta_1)
            if len(self._mazo_inicial) == 0:
                break
            carta_2 = self._mazo_inicial.sacar_carta_arriba()
            self.mazo_2.poner_carta_arriba(carta_2) 
        return self.mazo_1, self.mazo_2
    
    def iniciar_juego(self, ver_partida=True):
        self.armar_mazo_inicial()
        self.repartir_cartas()
        self._cartas_en_la_mesa = []
        self._turno = 0
        self._guerra = False
        self._ganador = ''
        self._empate = False

        while len(self.mazo_1) and len(self.mazo_2) and self._turno != N_TURNOS:
            try:
                if self._guerra:
                    for _ in range(3):
                        self._cartas_en_la_mesa.append(self.mazo_1.sacar_carta_arriba())
                        self._cartas_en_la_mesa.append(self.mazo_2.sacar_carta_arriba())
                
                carta_1 = self.mazo_1.sacar_carta_arriba(mostrar=True)
                carta_2 = self.mazo_2.sacar_carta_arriba(mostrar=True)

                # chequeo para evitar None
                if carta_1 is None or carta_2 is None:
                    raise ValueError("Error: carta None sacada del mazo")

                self._cartas_en_la_mesa.append(carta_1)
                self._cartas_en_la_mesa.append(carta_2)
            
            except DequeEmptyError:
                if len(self.mazo_1):
                    self._ganador = 'jugador 1'
                else:
                    self._ganador = 'jugador 2'
                self._guerra = False
                if ver_partida:
                    print(f'***** {self._ganador} gana la partida *****')
                break
            
            else:
                if ver_partida:
                    self.mostrar_juego()
               
                if self._cartas_en_la_mesa[-2] > self._cartas_en_la_mesa[-1]:
                    for carta in self._cartas_en_la_mesa:
                        self.mazo_1.poner_carta_abajo(carta)
                    self._cartas_en_la_mesa = []
                    self._guerra = False
                    if len(self.mazo_2):
                        self._turno += 1
                elif self._cartas_en_la_mesa[-1] > self._cartas_en_la_mesa[-2]:
                    for carta in self._cartas_en_la_mesa:
                        self.mazo_2.poner_carta_abajo(carta)
                    self._cartas_en_la_mesa = []
                    self._guerra = False
                    if len(self.mazo_1):
                        self._turno += 1
                else:
                    self._guerra = True
                    if ver_partida:
                        print('**** Guerra!! ****')
            
            if self._turno == N_TURNOS:
                self.empate = True
                if ver_partida:
                    print('***** Empate *****')
                break
                      
        
        if self._turno != N_TURNOS and not self._ganador:
            if len(self.mazo_1):
                self._ganador = 'jugador 1'
            else:
                self._ganador = 'jugador 2'              
            if ver_partida:
                print(f'***** {self._ganador} gana la partida *****')
                
    def mostrar_juego(self):
        print(f"Turno: {self._turno+1}")
        print('jugador 1:')
        print(self.mazo_1)
        print()
        print('          ', end='')
        for carta in self._cartas_en_la_mesa:
            print(carta, end=' ')
        print('\n')
        print('jugador 2:')
        print(self.mazo_2)
        print()
        print('------------------------------------')
        if self._ganador:
             print(f'***** {self._ganador} gana la partida *****')


if __name__ == "__main__":
    n = random.randint(0, 1000)
    juego = JuegoGuerra(random_seed=n)
    juego.iniciar_juego()
    print(f'Semilla usada: {n}')
