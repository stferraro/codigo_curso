def media_numeros(lista):
    media = sum(lista) / len(lista)
    return media

lista = [34, 67, 89, 92, 35, 45]
print(f'la media es {media_numeros(lista):.2f}')

