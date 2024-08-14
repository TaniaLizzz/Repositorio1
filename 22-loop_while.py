# monedas = 5

# while monedas > 0:  #Verdadero
#     print(f"Tengo {monedas} monedas")
#     #Para que vaya disminuyendo, hasta que se convierta en false
#     monedas -= 1  #monedas= monedas - 1 
    
    
# pass ocupa un lugar donde se espera una declaracion


# respuesta = 's'

# while respuesta == 's':
#     pass #
#     respuesta = input("Quieres salir? (s/n)")
    
# nombre = input("Dime tu nombre: ")

# for letra in nombre:
#     if letra == 'r':
#         break
#     else:
#         print(letra)
        
#Practica Loop while 1

# numero = 10

# while numero >= 0:  
#     print(f"Número {numero}")
#     numero -= 1
    
# #practica 2

# numero = 50
# while numero >= 0:
#     if numero % 5 == 0:  #division entre 5
#         print(numero)
#     numero -= 1

#practica 3

lista_numeros = [4, 5, 8, 7, 6, 9, 8, 2, 4, 5, 7, 1, 9, 5, 6, -1, -5, 6, -6, -4, -3]

for numero in lista_numeros:
    print(numero)
    if numero < 0:  #negativo
        break
