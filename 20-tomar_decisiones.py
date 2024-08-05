# if 10 > 9:
#     print("Es correcto")

# x = False

# if x:
#     print("Es correcto")
# else:
#     print("Es incorrecto")
    
# if 5 == 2:
#     print("Si es igual")
# else:
#     print("No es igual")
    
# # mascota = 'perro'
# # mascota = 'gato'
# mascota = 'loro'

# if mascota == 'perro':
#     print("Tienes un perro")
# elif mascota == 'gato':
#     print("Tienes un gato")
# else:
#     print("No es una mascota")
    
# edad = 15
# calificacion = 5

# if edad < 18:
#     print("Eres menor de edad")
#     if calificacion >= 3:
#         print("Aprobado")
#     else:
#         print("No aprobado")
# else:
#     print("Eres adulto")
    
    
#Practica control de flujo 1

# num1 = int(input("Ingresa un número: "))
# num2 = int(input("Ingresa otro número: "))

# if num1 > num2:
#     print(f"{num1} es mayor que {num2}")
# elif num2 > num1:
#     print("num2 es mayor que num1")
# else:
#     print("num1 y num2 son iguales")
    
#Practica control de flujo 2
# edad = 16
# tiene_licencia = False

# if edad >= 18 and tiene_licencia:  #And es cuando ambas se cumplen y or solo una
#     print("Puedes conducir")
# elif edad >= 18 and not tiene_licencia:
#     print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
# else:
#     print("No puedes conducir. Necesitas tener al menos 18 años")
# print("\n")
# #Opcional para que el usuario ingrese sus datos 
# edad = int(input("Introduce tu edad: "))
# tiene_licencia_input = input("¿Tienes licencia de conducir? (si/no): ").strip().lower()
# tiene_licencia = tiene_licencia_input == 'si'

# if edad >= 18 and tiene_licencia:
#     print("Puedes conducir")
# elif edad >= 18 and not tiene_licencia:
#     print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
# else:
#     print("No puedes conducir. Necesitas tener al menos 18 años")

edad = 16
tiene_licencia = False

if edad >= 18 and tiene_licencia: #Como acá contemplo lo de la licencia en elif ya no es necesario
    print("Puedes conducir")
elif edad < 18:
    print("No puedes conducir aun, debes tener 18 y contar con una licencia")
else:
    print("No puedes conducir.Necesitas tener al menos 18 años")