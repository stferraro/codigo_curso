edad = int(input("Introduce tu edad: "))

costo = 0

while edad < 0 or edad > 100:
    edad = int(input("Error, Introduce  de nuevo la edad: "))

if edad < 4:
    costo = 0
elif edad >= 4 and edad < 18:
    costo = 5
elif edad >= 18 and edad < 100:
    costo = 10

print(f"Tu entrada cuesta {costo}€")