texto = "ABCDEFGHIJKLM"
#Hasta: no incluye la posición
# fragmento = texto[2:5] #Obten fragmento de ese texto desde posición 2 hasta posicion 5
# print(fragmento)

# fragmento = texto[2:] #posicion 2 -->
# print(fragmento)

# fragmento = texto[:5] #posicion 0 hasta 4
# print(fragmento)

# fragmento = texto[2] #Solo posicion 2
# print(fragmento)

#Saltando 
# fragmento = texto[2:10:2] #De 2 en 2 hasta 9
# print(fragmento)

# fragmento = texto[2::2]  #DE 2 en 2 hasta el final
# print(fragmento)

# fragmento = texto[::2] #Desde el comienzo hasta el final de 2 en 2
# print(fragmento)

frase = "Controlar la complejidad es la esencia de la programacion"
primera_palabra = frase[:9]
print(primera_palabra)
#print(texto[0:8])

frase = "Nunca confies en un ordenador que no puedas lanzar por una ventana"
resultado = frase[8::3]
print(resultado)

frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
frase_invertida = frase[::-1]
print(frase_invertida)


