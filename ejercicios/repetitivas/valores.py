listaPrecios = []
listaDescuentos = []
listaValores = []

while True:
    precio = float(input("Ingresa el precio del producto: "))
    if precio == 0:
        break
    descuento = float(input("Ingresa el descuento del producto: "))
    listaPrecios.append(precio)
    listaDescuentos.append(descuento)
    valor = precio * (descuento / 100)
    listaValores.append(valor)
    
descuento_total = sum(precio * descuento / 100 for precio, descuento in zip(listaPrecios, listaDescuentos))
descuento_percent = (descuento_total / sum(listaPrecios)) * 100
valorfinal = sum(listaPrecios) - sum((listaPrecios)) * (descuento_percent / 100) 

print("Lista de Precios: ", listaPrecios)
print("Lista de Descuentos: ", listaDescuentos)
print("Lista de Valores: ", listaValores)
print("Porcentaje: ", descuento_total)
print("Porcentaje: ", descuento_percent)
print("Valor final: ", valorfinal)