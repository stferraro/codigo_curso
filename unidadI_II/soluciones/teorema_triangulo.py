a = float(input("Valor de a: "))
b = float(input("Valor de b: "))
c = float(input("Valor de c: "))

if a+b > c and a+c > b and b+c > a:
    print("Es un triangulo")
else:
    print("No es un triangulo")
    