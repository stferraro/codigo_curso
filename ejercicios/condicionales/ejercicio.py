renta = float(input("Introduce tu renta anual: "))

if renta < 10000:
    costo = renta * 5 / 100
elif renta >= 10000 and renta < 20000:
    costo = renta * 15 / 100
elif renta >= 20000 and renta < 35000:
    costo = renta * 20 / 100
elif renta >= 35000 and renta < 60000:
    costo = renta * 30 / 100
else:
    costo  = renta * 45 / 100
    
print(f"El costo de la renta es de: {costo:.2f}")
    