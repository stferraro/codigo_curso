import math


class Triangulo:
    
    def __init__(self, base, altura):
        self.__base = base
        self.___altura = altura
        
        
    @property
    def base(self):
        return self.__base
    
    
    @base.setter
    def base(self, base):
        if base > 0:
            self.__base = base
            
            
    @property
    def altura(self):
        return self.___altura
    
    
    @altura.setter
    def altura(self, altura):
        if altura > 0:
            self.___altura = altura

    def area(self):
        return self.base * self.altura / 2
    
    
    def hipotenusa(self):
        return math.sqrt(self.base**2 + self.altura**2)
    
    def perimetro(self):
        return self.base + self.altura + self.hipotenusa()
    
    
base = float(input("Valor de la base: "))
altura = float(input("Valor de la altura: "))

triangulo = Triangulo(base, altura)

h = triangulo.hipotenusa()

area = triangulo.area()

perimetro = triangulo.perimetro()


print(f"La hipotenusa es: {h:.2f}")
print(f"El area es: {area:.2f}")
print(f"El perimetro es: {perimetro:.2f}")