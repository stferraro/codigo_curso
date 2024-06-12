''' Quiero a traves de el uso del while hecer un programa que imprima la tabla de 
multiplicacion del 1 al 5'''


x = 1
while x <= 5:
    j = 1
    while j <= 5:
        print(x * j, end=" ")
        j += 1
    print(x * j)
    x += 1