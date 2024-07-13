import math

def area_circulo(radio):
    return math.pi * radio**2

def volumen_cilindro(radio,altura):
    areaCirculo = area_circulo(radio)
    return areaCirculo * altura

radio = float(input("Radio: "))
altura = float(input("Altura: "))

areaCirculo = area_circulo(radio)
print(f'Area: {areaCirculo:.2f}')

volumen = volumen_cilindro(radio,altura)

print(f"Volumen: {volumen:.2f}")

