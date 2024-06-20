frutas = {}



frutas['Platano'] = 1.50
frutas['Manzana'] = 2.00
frutas['Pera'] = 0.80
frutas['Naranja'] = 0.70

print(frutas)

nombreFruta = input('Ingresa el nombre de la fruta: ')

if nombreFruta in frutas:
    print('La fruta ya existe')
    frutas[nombreFruta] = float(input('Ingresa el precio en bs del kilo de la fruta: '))
else:
    frutas[nombreFruta] = float(input('Ingresa el precio en bs del kilo de la fruta: '))

print(frutas)