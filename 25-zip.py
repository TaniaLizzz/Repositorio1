capitales = ['Berlin','Tokio','Paris']
paises = ['Alemania','Japon','Francia']

combinados = list(zip(capitales,paises))

print(combinados)

for capital, pais in combinados:
    print(f"La capital de {pais} es {capital}")