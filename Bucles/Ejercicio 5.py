invertir = float(input("Ingrese la cantidad a invertir: "))
interes = float(input("Ingrese el interés anual (en porcentaje): "))
años = int(input("Ingrese el número de años: "))
for i in range(1, años + 1):
    capital = invertir * (1 + interes / 100) ** i
    print("Capital al final del año", i, ":", round(capital, 2))
