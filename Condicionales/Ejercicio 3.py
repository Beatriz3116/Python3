num1 = float(input("Ingrese el un número: "))
num2 = float(input("Ingrese otro número: "))

if num2 == 0:
    print("Error: El segundo número no puede ser cero.")
else:
    c = num1 // num2
    r = num1 % num2
    print(f'El cociente de {num1} entre {num2} es {c} y el resto es {r}.')