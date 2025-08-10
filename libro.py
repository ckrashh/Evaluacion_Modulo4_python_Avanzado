from datetime import datetime
class Libro:
    def __init__(self, titulo, autor, anio_publicacion,estado):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        if not estado:
            estado = "Disponible"
        self.estado = estado
    
    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Año de publicación: {self.anio_publicacion}, Estado: {self.estado}"
    
    @property
    def estado(self):
        return self._estado
    
    @property
    def titulo(self):
        return self._titulo
    
    @property
    def autor(self):
        return self._autor
    
    @property
    def anio_publicacion(self):
        return self._anio_publicacion
    
    @estado.setter
    def estado(self, estado):
        self._estado = estado

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo
        
    @autor.setter
    def autor(self, autor):
        self._autor = autor
         
    @anio_publicacion.setter
    def anio_publicacion(self, anio_publicacion):
        self._anio_publicacion = anio_publicacion