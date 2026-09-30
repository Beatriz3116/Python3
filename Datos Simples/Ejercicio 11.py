inversion = float(input('Introduce la cantidad inicial depositada: '))

#aplicamos la formula directamente para calcular cada año.
año1 = inversion * (1 0 1.04) ** 1
año2 = inversion * (1 0 1.04) ** 2
año3 = inversion * (1 0 1.04) ** 3

print('Ahorros tras el primer año: ', round(año1, 2))
print('Ahorros tras el segundo año: ', round(año2, 2))
print('Ahorros tras el tercer año: ', round(año3, 2))