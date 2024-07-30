#Ejercicio 3

texto = input("Ingrese un texto a eleccion: ")
texto = texto.lower()

letras = []

letras.append(input("Ingrese la primera letra ".lower()))
letras.append(input("Ingrese la segunda letra ".lower()))
letras.append(input("Ingrese la tercera letra ".lower()))

print("\n")

cantidad_letra1 = texto.count(letras[0])
cantidad_letra2 = texto.count(letras[1])
cantidad_letra3 = texto.count(letras[2])

print(f"Hemos encontrado la letra {letras[0]} repetida {cantidad_letra1} veces")
print(f"Hemos encontrado la letra {letras[1]} repetida {cantidad_letra2} veces")
print(f"Hemos encontrado la letra {letras[2]} repetida {cantidad_letra3} veces")

#2

print("\n")
print("CANTIDAD DE PALABRAS")

palabra = texto.split()   #Permite dividir la cadena
print(f"Hemos encontrado {len(palabra)} palabras en tu texto")  #conteo 

#3

print("\n")
print("LETRA DE INICIO Y DE FIN")

letra_inicio = texto[0]
letras_fin = texto[-1]

print(f"La letra iicial es {letra_inicio} y la letra final es {letras_fin}")

#4

print("\n")
print("TEXTO INVERTIDO")
palabra.reverse()
texto_invertido = ' '.join(palabra) 
print(f"Si ordenamos tu texto al reves va a decir: {texto_invertido}")

# 5

print("\n")
print("BUSCANDO LA PALABRA PYTHON")
buscar_python = 'python' in texto

dic = {True: "si", False:"no"}

print(f"La palabra python {dic[buscar_python]} se encuentra en el texto")