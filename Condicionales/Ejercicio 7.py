renta = float(input("Ingrese su renta anual: "))
if renta < 10000:
    impuesto = renta * 0.05
elif renta < 20000:
    impuesto = renta * 0.15
elif renta < 35000:
    impuesto = renta * 0.20
elif renta < 60000:
    impuesto = renta * 0.30
else:
    impuesto = renta * 0.45

print(f"El impuesto a pagar es: {impuesto}")