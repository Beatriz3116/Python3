nombre = input("Ingrese su nombre: ")
genero = input("Ingrese su género (M/F): ")

if (nombre < 'M' and genero == 'F'):
    print('Grupo A')
elif (nombre > 'N' and genero == 'M'):
    print('Grupo A')
else:
    print('Grupo B')
