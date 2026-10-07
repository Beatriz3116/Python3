frase = input("Introduce una frase cualquiera: ")
vocal = input("Introduce una vocal cualquiera: ")

frase_modificada = frase.replace(vocal, vocal.upper())

print(f"La frase modificada es: {frase_modificada}.")