# mi_lista = ['a','b','c','d']
# mi_lista2 = ['e','f','g','h']

# print(type(mi_lista))

# otra_lista = ['hola',55,6.1]

# resultado = len(mi_lista)
# print(resultado)

# #INDEXACION
# resultado = mi_lista[2]
# print(resultado)

# resultado = mi_lista.index("c")
# print(resultado)

# resultado = mi_lista[:] #Desde inicio hasta el final 
# print(resultado)
# resultado = mi_lista[:2] 
# print(resultado)
# resultado = mi_lista[0:2] #inicia posicionamineto  cero hasta 2
# print(resultado)

#CONCATENAR, listas mut
# resultado = mi_lista + mi_lista2
# print(resultado)

#Cambiar elemento
# mi_lista[0] = 'alfa'
# print(mi_lista)

# #Agrega elementos al final
# mi_lista.append('z')
# print(mi_lista)

# #Elimina el ultimo elemento
# mi_lista.pop()
# print(mi_lista)

# #elimina de la posicion
# mi_lista.pop(0)
# print(mi_lista)

#ordena los elementos de la lista
# mi_lista.sort()
# print(mi_lista)

# #Invierte
# mi_lista.reverse()
# print(mi_lista)

mi_lista = [1,'a',2.4,'b',5]
print(mi_lista)

medios_transporte = ['avión','auto','barco','bicicleta']
print(medios_transporte)
medios_transporte.append('motocicleta')
print(medios_transporte)

lista = ['manzana', 'banana' , 'mango', 'cereza', 'sandia']
eliminado = lista.pop(2)
print(lista)
print(eliminado)