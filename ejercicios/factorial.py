n = int(input("Introduce un numero: "))
f = 1

for i in range(1, n+1):
    f = f * i

print(f"El factorial de {n} es: {f}")