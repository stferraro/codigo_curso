fecha = {}

fecha['dd'] = input('Ingresa el dia: ')
fecha['mm'] = input('Ingresa el mes: ')
fecha['aaaa'] = input('Ingresa el año: ')

print(fecha)

print(f'{fecha.get("dd")}/{fecha.get("mm")}/{fecha.get("aaaa")}')