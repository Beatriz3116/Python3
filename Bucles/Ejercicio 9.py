contrasena_correcta = "contraseña"

intentos = ""

while intentos != contrasena_correcta:
    intentos = input("Introduce la contraseña: ")
    if intentos != contrasena_correcta:
        print("Contraseña incorrecta. Inténtalo de nuevo.")

print("¡Contraseña correcta! Acceso concedido.")