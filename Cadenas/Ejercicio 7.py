correo = input("Dime tu correo electrónico: ")

arroba = correo.find("@")
usuario = correo[:arroba]
nuevo_correo = usuario + "@ceu.es"

print(f"Tu nuevo correo electronico es: {nuevo_correo} .")