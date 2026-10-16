edad = int(input("Ingrese su edad: "))
if edad < 4:
    print("Su entrada es gratuita.")
elif edad < 18:
    print("Su entrada cuesta 5 euros.")
else:
    print("Su entrada cuesta 10 euros.")

print("Gracias por su visita.")