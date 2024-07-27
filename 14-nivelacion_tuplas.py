#Lista
miTupla = ["Rojo", "Azul", "Verde"]

#Tuplas
miTupla = ("Rojo", "Azul", "Verde")

#Conjuntos
miConjunto = {1,2,3,4,5,6,7,8,9}

#Eliminar datos
miConjunto.remove(9)
print(miConjunto)

#añadir elementos
miConjunto.add(9)
print(miConjunto)

#Diccionarios
miDiccionario = {1:{"nombre":"Juan David", "edad": 25, "Carrera":"Ingeniero de Sistemas"},
                 2:{"nombre":"Johan Gordillo", "edad": 28, "Carrera":"Ingeniero de Sistemas"},
                 3:{"nombre":"Daniel Acosta", "edad": 34, "Carrera":"Psicologia"}}
# # print(miDiccionario[1]) #Sale error
# print(miDiccionario["nombre"])

print(miDiccionario[3])

miVariable= 0