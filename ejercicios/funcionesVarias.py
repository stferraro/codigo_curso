import math

def media_numeros(lista):
    media = sum(lista) / len(lista)
    return media

def varianza_numeros (lista):
    a = media_numeros (lista)
    for i in lista:
        b = (i - a)**2
    c = b / len (lista)
    return c

def desviacion_tipica_numeros (lista):
    d = math.sqrt(varianza_numeros (lista))
    return d

def pider_numeros ():
    lista = []
    for i in range (0, 5):
        n = float(input("Introduce un valor: "))
        lista.append(n)
    return lista

def diccionario_valores ():
    diccionario_valores = {}
    a = media_numeros (lista)
    diccionario_valores['media'] = a
    b = varianza_numeros (lista)
    diccionario_valores['varianza'] = b
    c = desviacion_tipica_numeros (lista)
    diccionario_valores['desviacion'] = c
    return diccionario_valores

lista = pider_numeros ()
print (lista)
print (media_numeros (lista))
print (varianza_numeros (lista))
print (desviacion_tipica_numeros (lista))
diccionarioValores = diccionario_valores ()
print (diccionarioValores)
