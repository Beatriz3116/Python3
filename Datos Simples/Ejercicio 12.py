barras_viejas = int(input('Introduce el número de barras vendidas que no son del día: '))

precio_normal = 3.49
descuento = 0.6
con_descuento = precio_normal * (1 - descuento)
total  = barras_viejas * con_descuento

print('Precio habitual de una barra: ', precio_normal, '€')
print('Descuento aplicado por no ser fresca: 60%')
print('Coste final total: ', round(total, 2), '€')