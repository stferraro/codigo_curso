import random

a = random.randint(1, 100)

numero = int(input("Introduce un numero: "))

while numero != a:
    if numero > a:
        print("Coloca un numero mas bajo")
    else:
        print("Coloca un numero mas alto")
    numero = int(input("Introduce un numero: "))

print("Acertaste")
print("El numero era: ", a)
