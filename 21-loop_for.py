# lista = ['a','b','c']

# for letra in lista:
#     print("letra :" + letra)
    
# for letra in lista:
#     numero_letra = lista.index(letra) + 1 #que iniciee desde 1 los indices
#     print(f"Letra {numero_letra}: {letra}")
     
# lista2 = ['pablo', 'laura','juan','julia','luis']  #con strings

#Recorre todos los nombres
# for nombre in lista2:
#     if nombre.startswith('l'): #si el nombre empieza con l lo muestra
#         print(nombre)
#     else: 
#         print("El nombre no comienza con l")
        
# palabra = "python es genial"
# #letra es el eleento iterador y palabra es lo que se va a recorrer, tambien se puede recorrer el elemento iterador
# for letra in palabra:   
#     print(letra)
    
# for letra in 'python':
#     print(letra)

# for numero in (1,2,3,4):
#     print(numero)
    
# for numero in [[1,2],[3,4],[5,6]]:
#     print(numero)
    
#dos elementos iteradores
# for a,b in [[1,2],[3,4],[5,6]]:
#     print(a)
#     print(b)

# dic = {'clave1':'a','clave2':'b','clave3':'c'}

# for item in dic:
#     print(item)
    
# for item in dic.items():
#     print(item)

# for item in dic.values():
#     print(item)

#Práctica Loop For 1
alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
for nombre in alumnos_clase:
    print(f"Hola {nombre}")
print("\n")
#Práctica Loop For 2
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0

for numero in lista_numeros:
    suma_numeros += numero
print("La suma total es:", suma_numeros)
#Práctica Loop For 3
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0
for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero
print("La suma de los números pares es:", suma_pares)
print("La suma de los números impares es:", suma_impares)