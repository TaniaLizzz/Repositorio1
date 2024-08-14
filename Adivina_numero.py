from random import randint

def juego_adivinanza():
    print("¡Bienvenido al juego de adivinanza!")
    nombre = input("¿Cuál es tu nombre? ")
    print(f"Hola, {nombre}. He pensado un número entre 1 y 100. \nTienes 8 intentos para adivinar")
    
    numero_secreto = randint(1, 100)
    intentos = 0
     #Evalua 
    while intentos < 8:
        intentos += 1
        try:
            guess = int(input(f"Intento {intentos}: Ingresa tu número: "))
            
            if guess < 1 or guess > 100:
                print("El número debe estar entre 1 y 100.")
            elif guess < numero_secreto:
                print("El número secreto es mayor. Intenta de nuevo.")
            elif guess > numero_secreto:
                print("El número secreto es menor. Intenta de nuevo.")
            else:
                print(f"¡Felicidades, {nombre}! Has adivinado el número en {intentos} intentos.")
                return
        except ValueError:
            print("Por favor, ingresa un número válido.")
    
    print(f"Lo siento, {nombre}. Se acabaron los intentos. El número era {numero_secreto}.")
    print("Gracias por jugar. ¡Hasta la próxima!")

juego_adivinanza()