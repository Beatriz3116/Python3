contraseña = 'contraseña'
contraseña_usuario = input("Ingrese su nueva contraseña: ")

if contraseña_usuario.lower() == contraseña.lower():
    print('¡La contraseña coincide!')
else:
    print('La contraseña no coincide. Inténtelo de nuevo.')