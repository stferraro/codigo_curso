ingredientes_generales = 'mozzarela y tomate'

valor = int(input('Tipo de Pizza(1. Vegetariana, 2. No Vegetariana: '))

while valor != 1 and valor != 2:
    valor = int(input('Error, Tipo de Pizza(1. Vegetariana, 2. No Vegetariana: '))

if valor == 1:
    ingredientes = ' Pimiento y tofu'
    ingredientes = ingredientes_generales +  ', ' + ingredientes
    print(ingredientes)
elif valor == 2:
    ingredientes = ' Peperoni, Jamón y Salmón'
    ingredientes = ingredientes_generales + ', ' + ingredientes
    print(ingredientes)
    
