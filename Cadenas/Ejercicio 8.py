precio = float(input("Introduce el precio en euros: "))
euros = int(precio)
centimos = int((precio - euros) * 100)

print(f"Euros: {euros} y centimos: {centimos}.")