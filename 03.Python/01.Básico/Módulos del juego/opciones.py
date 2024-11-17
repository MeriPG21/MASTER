def menu():
    print("1. Partida modo solitario \n2. Partida 2 jugadores \n3. Estadística \n4. Salir")
    try:
        opcion = int(input())
        if opcion >= 1 and opcion <= 4:
            return opcion
        else: 
            print ("Por favor, introduce una de las cuatro opciones")
    except ValueError:
        print("Por favor, introduce una opción váldida")
        return 0