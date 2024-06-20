temperatura_maxima = float(input("Temperatura maxima del dia: "))
temperatura_minima = float(input("Temperatura minima del dia: "))

max_fahrenheit = ((temperatura_maxima * 9) / 5) + 32
min_fahrenheit = ((temperatura_minima * 9) / 5) + 32

temperatura_f_media = ((max_fahrenheit + min_fahrenheit) / 2)
media_celsius = ((temperatura_f_media - 32) * 5) / 9

print(f"la temperatura en grados farenheit es de : {temperatura_f_media:.2f}")
print(f'la temperatura en grados celsius es de : {media_celsius:.2f}')