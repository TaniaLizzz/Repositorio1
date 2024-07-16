# x = 10
# y = 5
# # suma = x+y

# #FUNCION FORMAT
# print("Mis numeros son {} y {}".format(x,y))
# print("Mis numeros son {} y {}".format(y,x))
# print("Mis numeros son {} y {} es igual a {}".format(x,y,x+y))


# #CADENAS LITERALES (f-strings)
# print(f"El primer número es {x} y el segundo número es {y}")
# print(f"El primer número es {x} y el segundo número es {y} entonces la suma es {x+y}")

# color = "rojo"
# matricula =  75451

# print(f"El auto es {color} y su matricula {matricula}")

#Práctica Formatear Cadenas 1
nombre_asociado = input("Digite su nombre: ")
numero_asociado = input("Digite su número de asociado: ")
print(f"Estimado/a {nombre_asociado}, su número de asociado es: {numero_asociado}\n")

#Práctica Formatear Cadenas 2
puntos_nuevos = int(input("Ingrese la cantidad de puntos nuevos que ha ganado: "))
puntos_totales = puntos_nuevos
print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos \n")

#Práctica Formatear Cadenas 3
# Solicitar al usuario ingresar los puntos anteriores y los puntos nuevos ganados
puntos_anteriores = puntos_nuevos
puntos_nuevos = int(input("Ingrese la cantidad de puntos nuevos que ha ganado: "))
# Calcular la cantidad total de puntos acumulados teniendo en cuenta los anteriores
puntos_totales = puntos_anteriores + puntos_nuevos
print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos")
print(f"En esta ocasión, la cantidad de puntos acumulados: ({puntos_totales}) será igual a los puntos anteriores ({puntos_anteriores}) más los puntos nuevos ({puntos_nuevos}).")
