while True:
    palabra = input("Introduce una palabra (o pon 'salir' para poder terminar): ")
    if palabra.lower() == 'salir':
        print("Programa terminado.")
        break
    print(palabra)