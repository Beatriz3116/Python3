barras_vierjas = int(input('Introduce el número de barras vendidas que no son del día: '))

precio_habitual = 3.49
descuento = 0.6
precio_descuento = precio_habitual * (1 - descuento)
coste_total  = barras_vierjas * precio_descuento

print('Precio habitual de una barra: ', precio_habitual, '€')
print('Descuento aplicado por no ser fresca: 60%')
print('Coste final total: ', round(coste_total, 2), '€')