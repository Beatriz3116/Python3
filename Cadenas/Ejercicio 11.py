producto = input("Introduce el nombre del producto: ")
precio = float(input("Introduce el precio del producto: "))
cantidad = int(input("Introduce la cantidad del producto: "))

total = precio * cantidad

print(f"El produnto: {producto}")
print(f"El precio unitario es: {precio:9.2f}€")
print(f"La cantidad de unidades es: {cantidad:03d}")
print(f"El total a pagar es: {total:11.2f}€")