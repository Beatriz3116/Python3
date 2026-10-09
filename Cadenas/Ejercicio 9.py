fecha = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")

separacion = fecha.split("/")
dia = int(separacion[0])
mes = int(separacion[1])
anio = int(separacion[2])

print(f"La fecha de tu nacimiento es el dia {dia} del mes {mes} y del año {anio}.")