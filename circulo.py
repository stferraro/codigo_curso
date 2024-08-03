import math


class Circulo:
    
    def __init__(self, radio):
        self.__radio = radio
        
        
    @property
    def radio(self):
        return self.__radio
    
    
    @radio.setter
    def radio(self, radio):
        if radio > 0:
            self.__radio = radio
        
    def area(self):
        return self.radio**2 * math.pi
    
    
    def perimetro (self):
        return 2 * math.pi * self.radio
    
    

circulo = Circulo(10)

print(f"El area es: {circulo.area():.2f}")
print(f"El perimetro es: {circulo.perimetro():.2f}")