puntuacion = float(input("Introduce tu puntuación: "))

if puntuacion < 0.0:
    print("Error: La puntuación no puede ser negativa.")
else:
    if puntuacion == 0.0:
        nivel = "Inaceptable"
    elif puntuacion == 0.4:
        nivel = "Aceptable"
    else:
        nivel = "Meritorio"
    
dinero = puntuacion * 2400
    
print(f"Nivel de rendimiento: {nivel}")
print(f"Cantidad de dinero a recibir: {dinero:.2f}€")