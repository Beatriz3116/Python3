edad = input("Ingrese su edad: ")
ingresos_mensuales = input("Ingrese sus ingresos mensuales: ")
if edad.isdigit() and ingresos_mensuales.isdigit():
    edad = int(edad)
    ingresos_mensuales = int(ingresos_mensuales)
    if edad >= 16 and ingresos_mensuales >= 1000:
        print("Puedes tributar.")
    else:
        print("No puedes tributar.")