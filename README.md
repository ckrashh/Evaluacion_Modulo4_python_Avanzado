# 📚 Evaluacion_Modulo4_python_Avanzado

## 🎯 Descripción del Proyecto

Este proyecto es la **evaluación final del Módulo 4 del Bootcamp de Python Avanzado** de Talento Digital. Implementa un sistema de gestión de bibliotecas simple basado en la **Programación Orientada a Objetos (POO)** en Python.

El programa permite a un usuario gestionar libros (físicos y digitales) a través de un menú interactivo, incluyendo funcionalidades como crear, eliminar, buscar y prestar/devolver libros, con persistencia de datos mediante un archivo de texto.

---

## ✨ Funcionalidades Principales

El programa ofrece un menú de 7 opciones con las siguientes capacidades:

1.  **Crear Libro:** Permite ingresar el título, autor, fecha de emisión (formato `AAAA-MM-DD`) y especificar si es un libro digital (`sí` o `no`).
2.  **Eliminar Libro:** Elimina un libro de la biblioteca buscando por su título.
3.  **Ver Libros:** Muestra una lista de todos los libros existentes en la biblioteca.
4.  **Buscar Libro:** Permite buscar un libro por su título y muestra sus detalles.
5.  **Marcar como Prestado:** Permite cambiar el estado de un libro a "prestado" buscando por su título.
6.  **Devolver Libro:** Permite cambiar el estado de un libro a "disponible" (devuelto) buscando por su título.
7.  **Salir del Programa:** Cierra la aplicación, guardando automáticamente todos los libros en el archivo de persistencia.

---

## 💻 Tecnologías Utilizadas

| Tecnología | Descripción |
| :--- | :--- |
| **Python** | Lenguaje principal para el desarrollo del sistema y la lógica de POO. |
| **POO** | Utilizado para estructurar los objetos `Libro`, `LibroDigital` y `Biblioteca`. |
| **Manejo de Archivos** | Implementación para la persistencia de datos (guardado y carga de libros) usando un archivo `.txt`. |

---

## 🚀 Estructura del Proyecto

El repositorio está organizado en varios archivos Python que representan la estructura orientada a objetos de la solución:

. ├── bibloteca.py # Clase principal de la Biblioteca y su lógica de gestión. ├── libro.py # Clase base Libro con atributos (título, autor, fecha, estado, etc.). ├── libroDigital.py # Clase LibroDigital que hereda de Libro. ├── main.py # Punto de entrada del programa y la lógica del menú interactivo. ├── biblioteca.txt # Archivo de persistencia de datos (generado o leído al inicio). └── README.md # Este archivo de documentación.


---

## ⚙️ Instalación y Uso

### Prerrequisitos

Asegúrate de tener **Python 3.x** instalado en tu sistema.

### Instalación

1.  Clona el repositorio en tu máquina local:

    ```bash
    git clone [https://github.com/ckrashh/Evaluacion_Modulo4_python_Avanzado.git](https://github.com/ckrashh/Evaluacion_Modulo4_python_Avanzado.git)
    ```
2.  Navega al directorio del proyecto:

    ```bash
    cd Evaluacion_Modulo4_python_Avanzado
    ```

### Ejecución

1.  Ejecuta el programa principal desde la terminal:

    ```bash
    python main.py
    ```

2.  **Carga Inicial:** Al iniciar, el programa intentará cargar los datos de la biblioteca desde el archivo `biblioteca.txt`. Si el archivo no existe, se iniciará con una biblioteca vacía.

3.  **Menú:** Sigue las opciones del menú que se mostrará en la consola para interactuar con la biblioteca.

---

## 👤 Autor

* Gerald Carrillo - [Perfil de GitHub](https://github.com/ckrashh)

---
