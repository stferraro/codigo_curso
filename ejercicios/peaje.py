vehiculos = {'moto': 3.50, 'carro': 12.00, 'camion': 16.00}
vehiculo = input('Quieres registrar un vehiculo coloca 0 para terminar: ')
contadorVehiculos = [0, 0, 0]  # Inicializar contadorVehiculos con valores iniciales de cero
contadorPrecios = [0.0, 0.0, 0.0]  # Inicializar contadorPrecios con valores iniciales de cero

while vehiculo != '0':
    vehiculo = vehiculo.lower()
    if vehiculo in vehiculos:
        if vehiculo == 'moto':
            print('Monto por moto: ' + str(vehiculos[vehiculo]))
            contadorVehiculos[0] += 1
            contadorPrecios[0] += vehiculos[vehiculo]
        elif vehiculo == 'carro':
            print('Monto por carro: ' + str(vehiculos[vehiculo]))
            contadorVehiculos[1] += 1
            contadorPrecios[1] += vehiculos[vehiculo]
        elif vehiculo == 'camion':
            print('Monto por camion: ' + str(vehiculos[vehiculo]))
            contadorVehiculos[2] += 1
            contadorPrecios[2] += vehiculos[vehiculo]
        else:
            print('Opcion no valida')
            vehiculo = input('Quieres registrar un vehiculo coloca 0 para terminar: ')
            continue
    else:
        print('Opcion no valida')
    
    vehiculo = input('Quieres registrar un vehiculo coloca 0 para terminar: ')

print('Hasta luego')
ganancia = sum(contadorPrecios)

print('Monto total: ' + str(contadorPrecios[0] + contadorPrecios[1] + contadorPrecios[2]))
print('Por el peaje pasaron motos: ' + str(contadorVehiculos[0]))
print('Por el peaje pasaron carros: ' + str(contadorVehiculos[1]))
print('Por el peaje pasaron camiones: ' + str(contadorVehiculos[2]))