#numeros primos del 1 al 100 en python

for i in range(2, 101):
    primo = True
    for j in range(2, i):
        if i % j == 0:
            primo = False
            break
    if primo:
        print(i, end=', ')
        
    