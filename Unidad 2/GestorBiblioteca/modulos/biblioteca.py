"""
Modulo dde bibioteca

Contiene la clase principal de la biblioteca que actua como el controlador del sistema. Gestiona la coleccion de libros y usuarios, tambien maneja opereaciones de prestamos y devolucion.
"""
#Importamos funciones del modulo de 'persistencia' y las clases del modulo 'modelos'
from . import persistencia
from .modelos import Libro, Usuario, ItemBiblioteca
from pathlib import Path

class Biblioteca:
    def __init__(self, nombreArchivo: str = "bibliotecaDatos.json"):
        self._libros = {}
        self._usuarios = {}
        rutaRaizProyecto = Path(__file__).parent.parent
        self._archivoJson = rutaRaizProyecto / nombreArchivo

    #Agregar libros y usuarios
    def agregarLibro(self, libro: Libro):
        if isinstance(libro, ItemBiblioteca):
            if libro._titulo in self._libros:
                print(f"El libro '{libro._titulo}' ya existe.")
            else:
                self._libros[libro._titulo] = libro
                print(f"Libro '{libro._titulo}' agregado.")
        else:
            print("Error: Solo se pueden agregar objetos de tipo ItemBiblioteca.")
    
    def agregarUsuario(self, usuario: Usuario):
        if isinstance(usuario, Usuario):
            if usuario._nombre in self._usuarios:
                print(f"El usuario '{usuario._nombre}' ya existe.")
            else:
                self._usuarios[usuario._nombre] = usuario
                print(f"Usuario '{usuario._nombre}' registrado.")
        else:
            print("Error: Solo se pueden agreagar objetos de tipo Usuario.")

    #Busquedas
    def buscarLibro(self, titulo: str) -> Libro | None:
        return self._libros.get(titulo)
    
    def buscarUsuario(self, nombre: str) -> Usuario | None:
        return self._usuarios.get(nombre)
    
    #Operaciones
    def prestarLibro(self, nombreUsuario: str, tituloLibro: str):
        usuario = self.buscarUsuario(nombreUsuario)
        libro = self.buscarLibro(tituloLibro)

        if not usuario:
            print(f"Error: Usuario '{nombreUsuario}' no encontrado.")
            return
        
        if not libro:
            print(f"Error: Libro '{tituloLibro}' no encontrado.")
            return
        
        if libro._estado == "prestado":
            print(f"El libro '{tituloLibro}' ya ha sido prestado.")
            return
        
        libro._estado = "prestado"
        usuario._librosPrestados.append(libro._titulo)
        print(f"'{nombreUsuario}' ha tomado prestado '{tituloLibro}'.")

    def devolverLibro(self, nombreUsuario: str, tituloLibro: str):
        usuario = self.buscarUsuario(nombreUsuario)
        libro = self.buscarLibro(tituloLibro)

        if not usuario:
            print(f"Error: Usuario '{nombreUsuario}' no encontrado.")
            return
        
        if not libro:
            print(f"Error: Libro '{tituloLibro}' no encontrado.")
            return
        
        if tituloLibro not in usuario._librosPrestados:
            print(f"'{nombreUsuario}' no tiene prestado ese libro.")
            return
        
        libro._estado  = "disponible"
        usuario._librosPrestados.remove(tituloLibro)
        print(f"'{nombreUsuario}' ha devuelto '{tituloLibro}'.")

    def mostrarLibrosDisponibles(self):
        print("LIBROS DISPONIBLES")
        encontrados = 0 

        for libro in self._libros.values():
            if libro._estado == "disponible":
                print(f" - {libro.mostrarInfo()}")
                encontrados += 1
        
        if encontrados == 0:
            print("No hay libros disponibles en este momento.")
        print("=" * 19)
    
    #Persistencia
    def guardarDatos(self):
        print("Guardando los datos.")
        datos = {
            "libros": [libro.toDict() for libro in self._libros.values()],
            "usuarios": [usuario.toDict() for usuario in self._usuarios.values()]
        }

        persistencia.guardarJson(datos, self._archivoJson)
    
    def cargarDatos(self):
        print("Cargando los datos.")
        datos = persistencia.cargarJson(self._archivoJson)

        if not datos:
            print("No se cargaron datos, empezando biblioteca vacia.")
            return
        
        try:
            self._libros = {}
            for datosItem in datos.get("libros", []):
                itemObj = None
                if datosItem.get("tipo") == "Libro":
                    itemObj = Libro(datosItem["titulo"],
                                    datosItem["autor"],
                                    datosItem["año"])
                
                if itemObj:
                    itemObj._estado = datosItem.get("estado", "disponible")
                    self._libros[itemObj._titulo] = itemObj
            
            self._usuarios = {}
            for datosUsuario in datos.get("usuarios", []):
                usuarioObj = Usuario(datosUsuario["nombre"])
                # Restauramos su lista de préstamos
                usuarioObj._librosPrestados = datosUsuario.get("libros_prestados", [])
                self._usuarios[usuarioObj._nombre] = usuarioObj
            
            print(f"Se cargaron {len(self._libros)} libros y {len(self._usuarios)} usuarios.")
        
        except KeyError as e:
            print(f"Error de formato en el archivo JSON. Faltan datos clave: {e}")

        except Exception as e:
            print(f"Error inesperado al cargar los datos.")
        
    