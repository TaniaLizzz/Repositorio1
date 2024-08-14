# for numero in range(5):
#     print(numero)
    
# for numero in range(1,5): #desde el 1 hasta el 5 (no incluye el 5)
#     print(numero)


# lista = list(range(1,20))

#practica 1
# mi_lista = list(range(2500, 2586))
# print(mi_lista)


#practica 2
# mi_lista = list(range(3, 301, 3))
# print(mi_lista)


#practica 3

numeros = range(1, 16)   #incluye el 15
suma_cuadrados = 0  

for numero in numeros:
    cuadrado = numero**2
    suma_cuadrados += cuadrado

print(f"La suma de cuadrados es: {suma_cuadrados}")
