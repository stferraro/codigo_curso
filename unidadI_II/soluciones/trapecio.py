'''dado en input el valor de la base menor y de la altura de un trapecio isosceles, crear una aplicacion en python que realice el calculo
del area y el perimetro del trapecio'''


import math 

base_menor = float(input("Valor de la base menor: "))
altura = float(input("Valor de la altura: "))

base_mayor = (base_menor + altura / 2)
lado_obliquo = math.sqrt(base_menor**2 + altura**2)

area_trapecio = (base_menor + base_mayor) * altura / 2
perimetro_trapecio = base_menor + base_mayor + (2 * lado_obliquo)


print(f"El area del trapecio es: {area_trapecio:.2f} y el perimetro es: {perimetro_trapecio:.2f}")


    
 




