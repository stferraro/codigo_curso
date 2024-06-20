divisas = {}

divisas['dolar'] = '$'
divisas['euro'] = '€'
divisas['Yen'] = '¥'
divisas['Libra'] = '£'

print(divisas)

divisa = input('Ingresa una divisa: ')
if divisa in divisas:
    divisas[divisa] = input('Ingresa el simbolo de la divisa: ')
else:
    print('La divisa no existe')
    divisas[divisa] = input('Ingresa el simbolo de la divisa: ')

print(divisas)


