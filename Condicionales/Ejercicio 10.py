pizza = int(input('Quieres pizza vegetariana o no vegetariana? '))
if pizza == 'vegetariana':
    print('Los ingredientes disponibles son: pimiento y tofu')
    ingrediente = input('Elige un ingrediente: ')
    if ingrediente == 'pimiento':
        print('Tu pizza vegetariana lleva pimiento')
    elif ingrediente == 'tofu':
        print('Tu pizza vegetariana lleva tofu')
else:
    print('Los ingredientes disponibles son: pepperoni, jamón y salmón')
    ingrediente = input('Elige un ingrediente: ')
    if ingrediente == 'pepperoni':
        print('Tu pizza no vegetariana lleva pepperoni')
    elif ingrediente == 'jamón':
        print('Tu pizza no vegetariana lleva jamón')
    elif ingrediente == 'salmón':
        print('Tu pizza no vegetariana lleva salmón')