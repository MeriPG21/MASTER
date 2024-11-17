import random 
import dificultad as modulo_dificultad
import opciones as modulo_opciones

def solitario():
    dificultad = modulo_dificultad.dificultad()
    print("Has escogido el nivel", dificultad, "de dificultad")
    numero_adivinar = random.randint(1,1000)
    print(numero_adivinar)
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
                elif numero_adivinar == numero: 
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