import math
from bibloteca import Bibloteca
from datetime import datetime
#validar opciones validas
def val_opcion(opcion):
    try:
        if int(opcion) <= 0 or int(opcion) > 7 or math.isnan(float(opcion)) or opcion == 1e309:
            print("Por favor, ingrese una opcion valida.")
            return False
        else:
            return True
    except (ValueError,TypeError):
        print("Por favor, ingrese solo numeros.")

#validar que los campos no esten vacios
def campos_vacios(nombre_libro, autor_libro, anio_libro):
    if len(nombre_libro) == 0 or len(autor_libro) == 0 or len(anio_libro) == 0:
        print("Por favor, ingrese todos los campos.")
        return False
    return True

# funcion para validar la fecha
def val_fecha(ani_publicacion):
    try:
        ani_publicacion = datetime.strptime(ani_publicacion, '%Y-%m-%d').date()  
        if ani_publicacion > datetime.now().date():
            raise Exception("La fecha de publicación no puede ser mayor a la actual.") 
        return True
    except (TypeError,ValueError):
        print("Por favor, ingrese una fecha valida.")
    except Exception as e:
        print(e)

# funcion para validar si el libro es digital
def val_s_n(es_libro_digital):
    try:
        if es_libro_digital.lower() == "s":
            return True 
        elif es_libro_digital.lower() == "n":
            return False
        raise ValueError
    except ValueError:
        print("Por favor, ingrese solo s o n.") 

# funcion del menu   
def menu():
    
    biblo = Bibloteca()
    biblo.cargar_txt()
    while True:
        print("\n--- Gestor de Biblioteca ---")
        print("1. Agregar libro")
        print("2. Eliminar libro")
        print("3. Ver todos los libros")
        print("4. Buscar libro")
        print("5. Marcar libro como prestado")
        print("6. Devolver libro")
        print("7. Salir")
        opcion = input("Elige una opcion: ")
        if val_opcion(opcion):
            if opcion == "1":
                while True:
                    print("\n--- Agregar Libro ---")
                    formato = None
                    nombre_libro = input("Ingrese el nombre del libro: ")
                    autor_libro = input("Ingrese el autor del libro: ")
                    anio_libro = input("Ingrese el año de publicación del libro (aaaa-mm-dd): ")
                    es_libro_digital = input("es libro digital ? (s/n)")
                    if val_s_n(es_libro_digital):
                        formato = "pdf"
                    if campos_vacios(nombre_libro, autor_libro, anio_libro) and val_fecha(anio_libro):
                        anio_libro = datetime.strptime(anio_libro, '%Y-%m-%d').date()
                        biblo.agregar_libro(nombre_libro, autor_libro, anio_libro, estado=None, formato=formato)
                        break
            elif opcion == "2":
                while True:
                    print("\n--- Eliminar Libro ---")
                    nombre_libro = input("Ingrese el nombre del libro a eliminar: ")
                    if not nombre_libro:
                        print("Por favor, no dejar campo vacio.")
                    else:
                        biblo.eliminar_libro(nombre_libro)
                        break
            elif opcion == "3":
                print("\n--- Libros ---")
                biblo.mostrar_libros()
            elif opcion == "4":
                while True:
                    print("\n--- Buscar Libro ---")
                    nombre_libro = input("Ingrese el nombre del libro a buscar: ")
                    if not nombre_libro:
                        print("Por favor, no dejar campo vacio.")
                    else:
                        biblo.buscar_libro(nombre_libro)
                        break
            elif opcion == "5":
                while True:
                    print("\n--- Prestar Libro ---")
                    nombre_libro = input("Ingrese el nombre del libro a prestar: ")
                    if not nombre_libro:
                        print("Por favor, no dejar campo vacio.")
                    else:
                        biblo.prestar_libro(nombre_libro)
                        break
            elif opcion == "6":
                while True:
                    print("\n--- Devolver Libro ---")
                    nombre_libro = input("Ingrese el nombre del libro a devolver: ")
                    if not nombre_libro:
                        print("Por favor, no dejar campo vacio.")
                    else:
                        biblo.devolver_libro(nombre_libro)
                        break
            elif opcion == "7":
                biblo.guardar_txt()
                print("Saliendo...")
                break
        
if __name__ == "__main__":
    menu()