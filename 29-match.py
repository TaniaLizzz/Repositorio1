serie = 'N-02'

# if serie == 'N-01':
#     print('Samsung')
# elif serie == 'N-02':
#     print('Nokia')
# elif serie == 'N-03':
#     print('Motorola')
# else:
#     print('No es un celular')
    
# match serie:
#     case 'N-01':
#         print('Samsung')
#     case 'N-02':
#         print('Nokia')
#     case 'N-03':
#         print('Motorola')
#     case _:
#         print('No es un celular')
        
cliente = {'nombre':'luis','edad':45,'ocupacion':'docente'}
pelicula = {'titulo':'Matrix','ficha_tecnica':{'protagonista':'Keanu Reeves','director':'Lana'}}

elemento = [cliente,pelicula, 'libro']

for e in elemento:
    match e:
        case {'nombre':nombre,'edad':edad,'ocupacion':ocupacion}:
            print("Es un cliente")
            print(nombre,edad,ocupacion)
        case {'titulo':titulo,'ficha_tecnica':{'protagonista':protagonista,'director':director}}:
            print("Es una pelicula")
            print(titulo, protagonista, director)
        case _:
            print("Esto es un libro")