import random

totalGanadas = [0,0] # el indice 0 es para el usuario y el indice 1 para la computadora
jugada = [1,2,3] 
partido = int(input("Quieres jugar (0/1) --> "))



while partido == 1 :
    jugadaPersonal = int(input("Jugada (1:Piedra, 2:Papel, 3:Tijera) --> "))
    jugadaComputadora = random.choice(jugada)
    while jugadaPersonal < 1 or jugadaPersonal > 3 :
        print("Jugada no valida")
        jugadaPersonal = int(input("Jugada (1:Piedra, 2:Papel, 3:Tijera) --> "))

    if (jugadaComputadora == 1 and jugadaPersonal == 2) or (jugadaComputadora == 2 and jugadaPersonal == 3) or (jugadaComputadora == 3 and jugadaPersonal == 1) :
        totalGanadas[0] += 1
        print("Ganas")
    elif (jugadaComputadora == 1 and jugadaPersonal == 3) or (jugadaComputadora == 2 and jugadaPersonal == 1) or (jugadaComputadora == 3 and jugadaPersonal == 2) :
        totalGanadas[1] += 1
        print("Pierdes")
    else :
        print("Empate")
        
    partido = int(input("Quieres jugar (0/1) --> "))
    
    while partido != 0 and partido != 1:
        print("Jugada no válida")
        partido = int(input("¿Quieres jugar (0/1) --> "))
            
if partido == 0:
    print("Juego terminado")
    print('Puntaje Personal: ', totalGanadas[0])
    print('Puntaje Computadora: ', totalGanadas[1])
else:
    print("Jugada no válida")