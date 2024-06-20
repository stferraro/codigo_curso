edad = int(input("Edad: "))

if edad < 4:
    print("No hay entrada")
elif edad >= 4 and edad < 18:
    print("Entrada de $10")
elif edad >= 18 and edad < 65:
    print("Entrada de $15")
else:
    print("Entrada de $25")