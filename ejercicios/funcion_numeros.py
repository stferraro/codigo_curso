
import math

def insertar_numeros():
    lista = []
    numero = int(input("Introduce un numero: "))
    while numero != 0:
        lista.append(numero)
        numero = int(input("Introduce un numero: "))
    return lista

def operaciones_numeros (lista):
    datos = {}
    media = sum(lista) / len(lista)
    media_str = "{:.2f}".format(media)
    varianza = sum((x - media)**2 for x in lista) / len(lista)
    varianza_str = "{:.2f}".format(varianza)
    desviacion = math.sqrt(varianza)
    desviacion_str = "{:.2f}".format(desviacion)
    datos['media'] = media_str
    datos['varianza'] = varianza_str
    datos['desviacion'] = desviacion_str
    return datos


lista = insertar_numeros()
datos = operaciones_numeros(lista)
print (datos)
 