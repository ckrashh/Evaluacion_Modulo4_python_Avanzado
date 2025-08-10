from libro import Libro
from libroDigital import LibroDigital
class Bibloteca():
    def __init__(self):
        # lista de libros
        self.libros = []

    # metodo para agregar un libro
    def agregar_libro(self,titulo,autor,anio_publicacion,estado=None,formato=None):
        # verifica que el libro no exista
        if self.existe(titulo):
            return self
        # crea el libro o el libro digital segun sea necesario
        if formato:
            libro = LibroDigital(titulo,autor,anio_publicacion,estado,formato)
        else:
            libro = Libro(titulo,autor,anio_publicacion,estado)
        print("\nLibro agregado exitosamente.")
        # agrega el libro
        self.libros.append(libro)
        return self
    
    # metodo para eliminar un libro
    def eliminar_libro(self,titulo):
        # verifica que hay libros
        if not self.libros:
            print("\nNo hay libros en la biblioteca.")
            return self 
        # recorre la lista de los libros
        for libro in self.libros:
            # verifica si el libro existe
            if libro.titulo.lower() == titulo.lower():
                # elimina el libro
                self.libros.remove(libro)
                print(f"\nLibro {libro.titulo} eliminado exitosamente.")
                return self
        # si no se encuentra el libro    
        print("\nEl libro no existe en la biblioteca.")
        return self
    
    # metodo para buscar un libro especifico
    def buscar_libro(self,titulo):
        # verifica que hay libros
        if not self.libros:
            print("\nNo hay libros en la biblioteca.")
            return self
        # recorre la lista de los libros
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                # imprime el libro
                print("\nLibro encontrado:")
                print(libro)
                return self
        # si no se encuentra el libro    
        print("\nEl libro no existe en la biblioteca.")
        return self    
    
    # metodo para prestar un libro
    def prestar_libro(self,titulo):
        # verifica que hay libros
        if not self.libros:
            print("\nNo hay libros en la biblioteca.")
            return self
        # recorre la lista de los libros
        for libro in self.libros:
            # verifica si el libro esta disponible
            if libro.titulo.lower() == titulo.lower() and libro.estado == "Disponible":
                libro.estado = "Prestado"
                print(f"\nLibro {titulo} prestado exitosamente.")
                return self
            # verifica si el libro ya esta prestado
            if libro.titulo.lower() == titulo.lower() and libro.estado == "Prestado":
                print("\nEl libro ya esta prestado.")
                return self
        # si no se encuentra el libro
        print("\nEl libro no existe en la biblioteca.")
        return self
    
    # metodo para devolver un libro
    def devolver_libro(self,titulo):
        # verifica que hay libros
        if not self.libros:
            print("\nNo hay libros en la biblioteca.")
            return self
        # recorre la lista de los libros
        for libro in self.libros:
            # verifica si el libro esta prestado
            if libro.titulo.lower() == titulo.lower() and libro.estado == "Prestado":
                libro.estado = "Disponible"
                print(f"\nLibro {titulo} devuelto exitosamente.")
                return self
            # verifica si el libro no esta prestado
            if libro.titulo.lower() == titulo.lower() and libro.estado == "Disponible":
                print("\nEl libro no esta prestado.")
                return self
        # si no se encuentra el libro    
        print("\nEl libro no existe en la biblioteca.")
        return self
    
    # guarda los datos en un txt
    def guardar_txt(self):
        with open("Evaluacion_Modulo4/biblioteca.txt", "w", encoding="utf-8") as archivo:
            for libro in self.libros:
                archivo.write(str(libro) + "\n")
        print("\nBiblioteca guardada exitosamente.")
        return self

    # carga los datos desde un txt
    def cargar_txt(self):
        try:
            # obtiene los datos
            datos = self.transformar_archivo()
            if not datos:
                raise FileNotFoundError
            for dato in datos:
                # verifica si el libro es digital
                if "Formato" in dato:
                    libro = LibroDigital(dato["Título"],dato["Autor"],dato["Año de publicación"],dato["Estado"],dato["Formato"])
                else:
                    libro = Libro(dato["Título"],dato["Autor"],dato["Año de publicación"],dato["Estado"])
                self.libros.append(libro)
            print("\nBiblioteca cargada exitosamente.")
        except FileNotFoundError:
            pass
        return self
    
    # muestra todos los libros
    def mostrar_libros(self):
        for libro in self.libros:
            print(libro)
    
    # valida si ya existe un libro
    def existe(self,titulo):
        if not self.libros:
            return False
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                print("El libro ya existe en la biblioteca.")
                return True   
            
    @classmethod
    def transformar_archivo(self):
        lista_datos = []
        # Inicializar un diccionario para almacenar los datos
        try:
            with open("Evaluacion_Modulo4/biblioteca.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo.readlines():
                    # Dividir la linea en partes
                    datos = {}
                    partes = [parte.strip() for parte in linea.split(",")]
                    # Iterar sobre cada parte y extraer la información
                    for parte in partes:
                        clave, valor = parte.split(":", 1)
                        clave = clave.strip()
                        valor = valor.strip()
                        datos[clave] = valor
                    #guardar todos los datos en una lista
                    lista_datos.append(datos)
            return lista_datos
        except FileNotFoundError:
            return None