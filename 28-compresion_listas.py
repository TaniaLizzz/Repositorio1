# palabra = 'python'

# lista = []

# for letra in palabra:
#     lista.append(letra)
    
# print(lista)

# lista = [letra for letra in 'python']
# print(lista)

# lista2 = [n for n in range(0,21,2)]
# print(lista2)

# lista3 = [n/2 for n in range(0,21,2)]
# print(lista3)

# lista4 = [n for n in range(0,21,2) if n * 2>10]
#Práctica comprensión listas 1
valores = [1, 2, 3, 4, 5, 6.5]
valores_cuadrado = [x**2 for x in valores]
print(valores_cuadrado)

#Práctica comprensión listas 2
valores = [1, 2, 3, 4, 5, 6.5]
valores_pares = [x for x in valores if x % 2 == 0]
print(valores_pares)

#Práctica comprensión listas 3
temperaturas_f = [32, 212, 98.6]
grados_celsius = [(f - 32) * 5/9 for f in temperaturas_f]
print(grados_celsius)
