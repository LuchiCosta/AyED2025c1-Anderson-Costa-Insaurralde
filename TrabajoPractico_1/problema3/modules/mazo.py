
from modules.ClaseLista import ListaDobleEnlazada  # Importa la clase ListaDobleEnlazada
from modules.carta import Carta  # Importa la clase Carta

class DequeEmptyError(Exception):
    """El mazo está vacío."""
    pass  # Define una excepción personalizada para cuando el mazo está vacío

class Mazo:
    def __init__(self):
        self.lista= ListaDobleEnlazada()

    def poner_carta_arriba(self,carta):
        self.lista.agregar_al_inicio(carta)

    def sacar_carta_arriba(self,mostrar=False):
        if self.lista.tamanio == 0:
            return None  # No hay cartas
        carta = self.lista.extraer(0)
        return carta
        

    def poner_carta_abajo(self,carta):
        self.lista.agregar_al_final(carta)

    def __len__(self):
        return len(self.lista)


if __name__ == "__main__":    
     mazo = Mazo()
     carta1 = Carta("♣", "3")
     carta2 = Carta("♦", "A")
     carta3 = Carta("♣", "8")

     mazo.poner_carta_arriba(carta1)
     mazo.poner_carta_arriba(carta2)
     mazo.poner_carta_arriba(carta3)


     print(mazo.sacar_carta_arriba()) # Debería imprimir Carta('♦', 'A') (oculta por defecto)
     print(mazo.sacar_carta_arriba(mostrar=True)) # Debería imprimir Carta('♣', '3') (Visible)

     try:
        mazo.sacar_carta_arriba() # Esto debería lanzar DequeEmptyError
     except DequeEmptyError as e:
        print(f"Error: {e}")