import dificultad as dificultad_juego

def dos_jugadores():
    dificultad = dificultad_juego.dificultad()
    print("Has escogido el nivel", dificultad, "de dificultad")
    numero_adivinar = int(input())
    while numero_adivinar < 1 or numero_adivinar > 1000:
        print("Elige un número, para que tu contrincante adivine, válido")
        numero_adivinar = int(input())
    else: 
        numero = int(input())
        if dificultad == 1:
            intentos = 19
            if not(numero_adivinar == numero):
                if numero_adivinar > numero:
                    print("El número a adivinar es mayor")
                if numero_adivinar < numero:
                    print("El número a adivinar es menor")
                while intentos > 0:
                    print("Te quedan", intentos, "intentos")
                    intentos = intentos -1 
                    numero = int(input())
                    if not(numero_adivinar == numero):
                        if numero_adivinar > numero:
                            print("El número a adivinar es mayor")
                        if numero_adivinar < numero:
                            print("El número a adivinar es menor")
                    if numero_adivinar == numero: 
                        print("Has ganado")
                        return "Ganador"
                        break 
                else: 
                    print("Has sobrepasado los intentos")
                    return "Perdedor"
            elif numero_adivinar == numero: 
                print("Has ganado")
                return "Ganador"
        elif dificultad == 2:
            intentos = 11
            if not(numero_adivinar == numero):
                if numero_adivinar > numero:
                    print("El número a adivinar es mayor")
                if numero_adivinar < numero:
                    print("El número a adivinar es menor")
                while intentos > 0:
                    print("Te quedan", intentos, "intentos")
                    intentos = intentos -1 
                    numero = int(input())
                    if not(numero_adivinar == numero):
                        if numero_adivinar > numero:
                            print("El número a adivinar es mayor")
                        if numero_adivinar < numero:
                            print("El número a adivinar es menor")
                    if numero_adivinar == numero: 
                        print("Has ganado")
                        return "Ganador"
                        break 
                else: 
                    print("Has sobrepasado los intentos")
                    return "Perdedor"
            elif numero_adivinar == numero: 
                print("Has ganado")
                return "Ganador"
        elif dificultad == 3:
            intentos = 4
            if not(numero_adivinar == numero):
                if numero_adivinar > numero:
                    print("El número a adivinar es mayor")
                if numero_adivinar < numero:
                    print("El número a adivinar es menor")
                while intentos > 0:
                    print("Te quedan", intentos, "intentos")
                    intentos = intentos -1 
                    numero = int(input())
                    if not(numero_adivinar == numero):
                        if numero_adivinar > numero:
                            print("El número a adivinar es mayor")
                        if numero_adivinar < numero:
                            print("El número a adivinar es menor")
                    if numero_adivinar == numero: 
                        print("Has ganado")
                        return "Ganador"
                        break 
                else: 
                    print("Has sobrepasado los intentos")
                    return "Perdedor"
            elif numero_adivinar == numero: 
                print("Has ganado")
                return "Ganador"
        else: 
            print("Opción de dificultad no válida")   
                
