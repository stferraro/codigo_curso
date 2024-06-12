import random

totalGanadas = 0
totalGanadasComputadora = 0
continuar = True
jugada = int (input("Quieres jugar (0/1) --> "))

while continuar :
    
    if jugada == 1 :
        
        print ("Piedra , Papel o Tijera ?")

        print ("1. Piedra")
        print ("2. Papel")
        print ("3. Tijera")

        jugadaComputadora = random.randint(1, 3)
        jugadaPersonal = int(input("Que quieres Piedra, Papel o Tijera --> "))

        if (jugadaComputadora == jugadaPersonal):
    
            print("empate")
            
            if (jugadaComputadora == 1):
            
                print("Personal: Piedra")
                print("Computadora; Piedra")
            
            elif (jugadaComputadora == 2):
                
                print("Personal: Papel")
                print("Computadora: Papel")
            
            elif (jugadaComputadora == 3) :
                
                print ("Personal: Tijera")
                print ("Personal: Tijera")
    
        elif (jugadaComputadora == 1) and (jugadaPersonal == 2) :
    
            print("Ganaste")
            totalGanadas += 1
            print("Personal: Papel" )
            print("Computadora: Piedra")

        elif (jugadaComputadora == 2) and (jugadaPersonal == 1) :
    
            print("Perdiste")
            totalGanadasComputadora += 1
            print("Personal: Piedra")
            print("Computadora: Papel")
    
        elif (jugadaComputadora == 3) and (jugadaPersonal == 1) :
         
            print("Ganaste")
            print("Personal: Piedra")
            print("Computadora: Tijera")
            totalGanadas += 1
    
        elif (jugadaComputadora == 2) and (jugadaPersonal == 3) :
    
            print("Ganaste")
            print("Personal: Tijera")
            print("Computadora: Papel")
    
        elif (jugadaComputadora == 1) and (jugadaPersonal == 3) :
    
            print("perdiste")
            print("Personal: Tijera")
            print("Computadora: Piedra")
            totalGanadasComputadora += 1
            
    
        elif (jugadaComputadora == 3) and (jugadaPersonal == 2) :
            print("perdiste")
            print("Personal: Papel")
            print("Computadora: Tijera")
            totalGanadasComputadora += 1
        
        jugada = int (input("Quieres jugar (0/1) --> "))
    
    elif (jugada != 0) and (jugada != 1) :
        
        print ("error, en la jugada")
        jugada = int (input("Quieres jugar (0/1) --> "))
        continuar = True
        
    else :
        print ("Hasta Luego")
        print ("Tu ganadas: ", totalGanadas)
        print ("Computadora ganadas: ", totalGanadasComputadora)
        continuar = False
