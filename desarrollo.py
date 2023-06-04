import random

class Jugador:
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.vida = 3
        self.arma = None
        self.artefacto = None
        
    def elegir_arma(self):
        self.arma = random.choice(['Escopeta', 'Hechizo', 'Espada'])
        print(f"{self.nombre} eligió {self.arma}.")
    
    def elegir_artefacto(self):
        self.artefacto = random.choice(['Escudo', 'Biblia', 'Chaleco antibalas'])
        print(f"{self.nombre} eligió {self.artefacto}.")

    def defender(self, arma_atacante):
        if self.artefacto == "Escudo" and arma_atacante == "Espada":
            print("¡Defendiste el ataque con éxito!")
        elif self.artefacto == "Biblia" and arma_atacante == "Hechizo":
            print("¡Defendiste el ataque con éxito!")
        elif self.artefacto == "Chaleco antibalas" and arma_atacante == "Escopeta":
            print("¡Defendiste el ataque con éxito!")
        else:
            self.vida -= 1
            print(f"¡Te han quitado una vida! Ahora te quedan {self.vida} vidas.")
    
    def atacar(self, otro_jugador):
        print(f"{self.nombre} ataca con {self.arma}...")
        otro_jugador.defender(self.arma)
        
    def jugar_turno(self, otro_jugador):
        print(f"{self.nombre} está listo para jugar su turno.")
        self.elegir_arma()
        otro_jugador.elegir_artefacto()
        self.atacar(otro_jugador)
        input("Presiona Enter para continuar...")
        
def main():
    nombre1 = input("Jugador 1, introduce tu nombre: ")
    edad1 = int(input("Jugador 1, introduce tu edad: "))
    peso1 = int(input("Jugador 1, introduce tu peso: "))
    jugador1 = Jugador(nombre1, edad1, peso1)
    
    nombre2 = input("Jugador 2, introduce tu nombre: ")
    edad2 = int(input("Jugador 2, introduce tu edad: "))
    peso2 = int(input("Jugador 2, introduce tu peso: "))
    jugador2 = Jugador(nombre2, edad2, peso2)
    
    jugador_actual = jugador1
    otro_jugador = jugador2
    
    while jugador1.vida > 0 and jugador2.vida > 0:
        print("¡Comienza el turno!")
        print("================================================================")
        jugador_actual.jugar_turno(otro_jugador)
        jugador_actual, otro_jugador = otro_jugador, jugador_actual
        
    if jugador1.vida > 0:
        print(f"¡{jugador1.nombre} ha ganado!")
    else:
        print(f"¡{jugador2.nombre} ha ganado!")
        
if __name__ == '__main__':
    main()
