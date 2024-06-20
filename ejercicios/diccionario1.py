datos = {}

datos['nombre'] = 'Juan'
datos['edad'] = 25
datos['direccion'] = 'Calle 123'
datos['telefono'] = '04123456789'

print(f'''{datos.get('nombre')}, tiene {datos.get('edad')} años, 
      vive en {datos.get('direccion')}, 
      y su numero de telefono es {datos.get('telefono')}''')