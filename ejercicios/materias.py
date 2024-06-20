materias = {}
sumaNotas = 0
print('Bienvenido al sistema de materias')

while True:
    nombreMateria = input('Ingresa el nombre de la materia: ')

    if nombreMateria in materias:
        print('La materia ya existe')
    else:
        while True:
            nota = float(input('Ingresa la nota: '))
            if 0 <= nota <= 20:
                materias[nombreMateria] = nota
                sumaNotas += nota
                break
            else:
                print('La nota debe ser entre 0 y 20')
        else:
            print('Por favor ingresa un número válido')

    continuar = input('¿Quieres agregar otra materia? (s/n): ').lower()
    if continuar != 's':
        break

print(materias)

notas = list(materias.values())    
promedio = sum(notas) / len(notas) 
promedio2 = sumaNotas / len(materias)


print(f'El promedio de tus materias es: {promedio:.2f}')
print(f'El promedio de tus materias es: {promedio2:.2f}')
maximaNota = max(notas)
minimaNota = min(notas)

materiaMaxValor = max(materias, key=materias.get)
materiaMinValor = min(materias, key=materias.get)

#maximo y minimo con algoritmos y while 
maxis = float('-inf')
i = 0
while i < len(notas):
    if notas[i] > maxis:
        maxis = notas[i]
    i += 1

minus = float('inf')
i = 0
while i < len(notas):
    if notas[i] < minus:
        minus = notas[i]
    i += 1

print (f'La materia con la nota maxima es: {materiaMaxValor} con nota {maximaNota} y la minima es: {materiaMinValor} con nota {minimaNota}')
print (f'La materia con la nota maxima es: {materiaMaxValor} con nota {maxis} y la minima es: {materiaMinValor} con nota {minus}')