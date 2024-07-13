def calcular_total_con_iva(precio, iva):
    total = precio + (precio * iva) / 100
    if iva == 0:
        total = precio + (precio * 21) / 100
    return total

precio = float(input("Ingresa el precio del producto: "))
iva = float(input("Ingresa el porcentaje de IVA: "))

total = calcular_total_con_iva(precio, iva)

print(f"Total: , {total:.2f}")

