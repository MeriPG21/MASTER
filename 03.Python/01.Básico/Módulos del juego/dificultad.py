def dificultad():
    print("Elige la dificultad \n1. Fácil (20 intentos) \n2. Medio (12 intentos) \n3. Difícil (5 intentos)")
    
    try: 
        opcion = int(input())
        if opcion >= 1 and opcion <= 3: 
            return opcion
        else: 
            print("Elige una opción de dificultad válido")
    except ValueError: 
        print("Por favor, introduce una opción de dificultad válida")
        return 0 