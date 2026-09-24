inversion = float(input('Introduce la cantidad inicial depositada: '))

año1 = inversion * 1.04
año2 = año1 * 1.04
año3 = año2 * 1.04

print('Ahorros tras el primer año: ', round(año1, 2))
print('Ahorros tras el segundo año: ', round(año2, 2))
print('Ahorros tras el tercer año: ', round(año3, 2))