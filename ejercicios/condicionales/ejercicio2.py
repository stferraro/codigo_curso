puntuacion = float(input("Introduce tu puntuacion: "))

if puntuacion == 0.0:
    print('inaceptable')
    dinero = puntuacion * 2400
elif puntuacion == 0.4:
    print('aceptable')
    dinero = puntuacion * 2400
elif puntuacion >= 0.6:
    print('meritorio')
    dinero = puntuacion * 2400
else:
    print('puntuacion no valida')






puntuacion = float(input("Introduce tu puntuacion: "))

match puntuacion:
    
    case 0.0:
        
        print('inaceptable')
        dinero = puntuacion * 2400
        print(f'paga {dinero:.2f}')
    
    case 0.4:
        
        print('aceptable')
        dinero = puntuacion * 2400
        print(f'paga {dinero:.2f}')
        
    case 0.6:
        
        print('meritorio')
        dinero = puntuacion * 2400
        print(f'paga {dinero:.2f}')
        
    case _:
        
        print('puntuacion no valida')