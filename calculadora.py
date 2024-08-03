
class Calculadora :
    
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b
    
    def multiplicacion(self, a, b):
        return a * b
    
    def division(self, a, b):
        if b == 0:
            return 'No se puede dividir entre 0'
        else:
            return a / b
        

calculadora = Calculadora(10, 5)

c = calculadora.suma(10, 5)
d = calculadora.resta(10, 5)
e = calculadora.multiplicacion(10, 5)
f = calculadora.division(10, 5)

print(f'{c}, {d}, {e}, {f:.2f}')
