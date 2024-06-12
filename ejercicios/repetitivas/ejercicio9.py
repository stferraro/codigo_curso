totalCarro = 0
totalMotos = 0
total = 0
tipo_vehiculo = int(input("¿Que tipo de vehiculo es? (carro/moto) (1/2/0 para terminar): "))
monto = 0

while (tipo_vehiculo != 0):
    
    if (tipo_vehiculo == 1):
        monto = 10.00
        totalCarro = totalCarro + monto
    elif (tipo_vehiculo == 2):
        monto = 3.50
        totalMotos = totalMotos + monto
    else:
        print("Tipo de vehiculo no valido")
    print (f"Monto:   {monto}")
    total = total + monto
    tipo_vehiculo = int(input("¿Que tipo de vehiculo es? (carro/moto) (1/2/0 para terminar): "))
    
print ('monto carros ' + str(totalCarro))
print ('monto motos ' + str(totalMotos))
print ('total ' + str(total))
    

