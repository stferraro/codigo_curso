a = float(input("Valor de a: "))

c = a / 2

if c.is_integer():
    print("Es par")
else:
    print("Es impar")   
    
    
#

edad = int(input("Edad: "))
ingresos = float(input("Ingresos: "))

if edad > 16 and ingresos >= 1000:
    print("tiene que pagar impuesto")
else:
    print("No tiene que pagar impuesto") 