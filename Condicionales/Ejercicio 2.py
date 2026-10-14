contraseña = 'contraseña'
contraseña_usuario = input("Ingrese su contraseña: ")

if contraseña_usuario.lower() == contraseña.lower():
    print('¡La contraseña coincide!')
else:
    print('La contraseña no coincide.')