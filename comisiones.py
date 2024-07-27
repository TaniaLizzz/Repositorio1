nombre = input("Por favor, ingresa tu nombre: ")
ventas_mes = input("Ingresa el monto total de tus ventas en este mes: " )
ventas = float(ventas_mes)  #Se convierte a float 

comision = ventas * 13 / 100  #Calcular el 13%

mensaje = f"Hola {nombre}, tu comisión por este mes es: ${comision:.2f}"
print(mensaje)
