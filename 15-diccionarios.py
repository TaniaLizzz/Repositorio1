# diccionario = {'c1':'valor1','c2':'valor2'}
# print(type(diccionario))

# resultado = diccionario['c1']
# print(resultado)

# cliente = {'nombre':'John', 'apellido':'Rojas','peso':88,'talla':1.76}
# consulta = cliente['apellido']
# print(consulta)

# consulta = cliente['talla']
# print(consulta)

# dic = {'c1':55,'c2':[10,20,30], 'c3':{'s1':100,'s2':200}}
# print(dic['c2'][1])
# print(dic['c3']['s2'])

# dic2 = {'c1':['a','b','c'],'c2':['d','e','f']}
# print(dic2['c2'[1].upper()])

# dic3 = {1:'a',2:'b'}
# dic3[3]='c'
# print(dic3)

# dic3[2]='B'
# print(dic3)


#Practica 1
mi_dic = {"nombre": "Karen","apellido": "Jurgens","edad": 35,"ocupacion": "periodista"}
print(mi_dic)


#Practica 2
def print_second_item(diccionario):
    lista_points2 = diccionario['points2']
    return lista_points2[1]  #indice 1, segundo valor 

diccionario = {'nombre': 'ejemplo','points2': [100, 200, 300]}
print(print_second_item(diccionario))


#Practica 3
mi_dic["edad"] = 36
mi_dic["ocupacion"] = "editora"
mi_dic["pais"] = "Colombia"
print(mi_dic)