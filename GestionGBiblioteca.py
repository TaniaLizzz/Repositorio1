class Libro:  #Clase
    def __init__(self, titulo, autor, ejemplares):
        self.titulo = titulo
        self.autor = autor
        self.ejemplares = ejemplares
        self.prestados = 0
    
    def disponibles(self):  #Funcion
        return self.ejemplares - self.prestados  #100- 0
    
    def prestar(self):
        if self.disponibles() > 0:  #100 > 0 puede prestar
            self.prestados += 1
            print(f"Has tomado prestado el libro '{self.titulo}' del autor ''{self.autor}")
            return True
        else:
            print("Lo siento, no hay ejemplares disponibles de '{self.titulo}' en este momento")
            return False 
    
    def devolver(self):
        if self.prestados > 0: 
            self.prestados -= 1
            print(f"Has devuelto el libro '{self.titulo}' del autor ''{self.autor}")
            return True
        else:
            print(f"No tienes ejemplares de '{self.titulo} para devolver")
            return False
        
    def __str__(self):
        return f"'{self.titulo}' de {self.autor} - Disponibles: {self.disponibles()}"
    
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.librosPrestados = [] #lista 
        
    def tomarPrestado(self, libro): #Parametro de Libro, que es un objeto
        if libro.prestar():
            self.librosPrestados.append(libro)  #Agrega el libro a esa lista
            return True
        else:
            return False
        
    def devolver(self, libro):
        libro.devolver()
        if libro in self.librosPrestados:
            self.librosPrestados.remove(libro)
            
    def librosPrestados(self):
        if self.librosPrestados():
            return ", ".join([libro.titulo for libro in self.librosPrestados()])
        else:
            return "ninguno"
        
    def __str__(self):
        return f"Usuario: '{self.nombre}' - Libros prestados: {self.librosPrestados()}"
    
class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.catalogo = []
        self.usuarios = []
        
    def agregarLibro(self, libro):
        self.catalogo.append(libro)
    
    def registrarUsuario(self, libro):
        self.catalogo.append(libro)
        
        