cantidad = float(input('¿Cuánto es la cantidad a invertir?: '))
interes = float(input('¿Cuál es el interés anual (%)?: '))
años = int(input('¿Cuantos años dura la inversión?: '))

capital = cantidad * (1 + interes / 100) ** años

print(f"El capital obtenido es: ", round(capital, 2))