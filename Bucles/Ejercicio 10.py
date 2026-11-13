num = int(input("Ingrese un número entero: "))
if num < 2:
    print("No es un número primo.")
else:
    es_primo = True
    i = 2
    
while i < num:
    if num % i == 0:
        es_primo = False
        break
    i += 1

if es_primo:
    print(f"{num} es un número primo.")
else:
    print(f"{num} no es un número primo.")