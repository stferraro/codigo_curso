'''Juego de Piedra Papel Tijera con el uso de funciones'''

import random


def decide_jugar ():
    '''Funcion que decide si el usuario quiere jugar o no'''
    
    jugar = input("¿Quieres jugar? (s/n): ")
    return jugar

def introduce_nombre ():
    '''Funcion que introduce el nombre del usuario'''
    
    
    nombre = input("Introduce tu nombre: ")
    return nombre

def decide_jugada ():
    '''Funcion que decide la jugada del usuario'''
    
    jugada = input("¿Piedra, papel o tijera? ")
    return jugada

def decide_maquina ():
    '''Funcion que decide la jugada de la maquina'''
    
    maquina = random.choice(["piedra", "papel", "tijera"])
    return maquina

def retornar_ganador (jugada, maquina):
    '''Funcion que retorna el ganador'''
    num_ganadas = {'computadora': 0, 'jugador': 0}
    
    if (jugada == maquina):
        return "Empate"
    elif ((jugada == "piedra" and maquina == "tijera") or
          (jugada == "papel" and maquina == "piedra") or
          (jugada == "tijera" and maquina == "papel")):
        num_ganadas['jugador'] += 1
        return num_ganadas
    else:
        num_ganadas['computadora'] += 1
        return num_ganadas
    
def juego ():
    '''Funcion que controla el juego'''
    
    nombre = introduce_nombre ()
    jugar = decide_jugar ()
    ganador = {}
    
    while (jugar == 's'):
        print(f"Hola {nombre}, bienvenido al juego")
        print("Piedra, papel o tijera")
        jugada = decide_jugada ()
        while (jugada not in ["piedra", "papel", "tijera"]):
            print("Jugada invalida")
            jugada = decide_jugada ()
        else:
            maquina = decide_maquina ()
            ganador = retornar_ganador (jugada, maquina)
            print(f"La maquina eligio {maquina}")
            jugar = decide_jugar ()
    else:
        print("Hasta la proxima")
        if ganador.get('jugador') != None and ganador.get('computadora') != None:
            print(f'El usuario ha ganado {ganador.get("jugador")} veces')
            print(f'La maquina ha ganado {ganador.get("computadora")} veces')

if __name__ == "__main__":
    juego ()
    