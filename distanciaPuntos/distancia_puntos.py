'''distancia entre dos puntos con grafico
A(x1,y1)
B(x2,y2)'''

import matplotlib.pyplot as plt
import math

def calcula_distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def graficar(x1, y1, x2, y2):
    plt.plot([x1, x2], [y1, y2])
    plt.show()

x1 = float(input("Coordenada x1: "))
y1 = float(input("Coordenada y1: "))
x2 = float(input("Coordenada x2: "))
y2 = float(input("Coordenada y2: "))
d = calcula_distancia(x1, y1, x2, y2)
print(f"La distancia entre los puntos es: {d:.2f}")
graficar(x1, y1, x2, y2)