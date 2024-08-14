# print(list(enumerate("Hola")))

# for indice, numero in enumerate([5.55,6,7.50]):
#     print(indice, numero)
    
# lista = ['a','b','c']

# # for item in enumerate(lista):
# #     print(item)
    
# # for index, item in enumerate(lista):
# #     print(index,item)
    
# for index, item in enumerate(range(50,55)):
#     print(index, item)
    
# mis_tuplas = list(enumerate(lista))
# print(mis_tuplas)

# #practica 1
# lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

# for indice, nombre in enumerate(lista_nombres):
#     print(f'{nombre} se encuentra en el índice {indice}')

#Practica 2
# palabra = "Python"
# lista_indices = list(enumerate(palabra))
# print(lista_indices)

#practica 3
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres):
    if nombre.startswith('M'):
        print(indice)
