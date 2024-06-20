import math

a = float(input("Valor de a: "))
b = float(input("Valor de b: "))
c = float(input("Valor de c: "))

d = (b**2) - (4 * a * c)

x1 = 0
x2 = 0

if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
elif d == 0:
    x1 = -b / (2 * a)
    x2 = x1
else:
    x1 = x2 = 'No tiene raices reales'
    
print(f"Las raices son: {x1:.2f} y {x2:.2f}")

