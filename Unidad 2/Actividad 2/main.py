class Producto:
    def __init__(self, nombre:str, precio:float):
        #Atributo publico
        self.nombre = nombre

        #Atributo protegido
        self.precio = precio
        
        #Atributo privado
        self.__stock = 0

    #Getter para el stock
    @property
    def stock(self) -> int:
        return self.__stock
        
    #Setter para el stock
    @stock.setter
    def stock(self, cantidad: int):
        if cantidad >= 0:
            self.__stock = cantidad
        else:
            raise ValueError("El stock no puede ser un número negativo.")
            
    #Getter para el precio
    @property
    def precio(self) -> float:
        return self._precio
        
    #Setter del precio
    @precio.setter
    def precio(self, valor: float):
        if valor > 0: 
            self._precio = valor
        else:
            raise ValueError("El precio debe ser un numero positivo.")
        
    #Print del objeto producto
    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Precio: {self.precio:,.2f}, Stock: {self.stock}"
        
    #Compara si dos productos son iguales
    def __eq__(self, other) -> bool:
        if not isinstance(other, Producto):
            return NotImplemented
        return self.nombre.lower() == other.nombre.lower()

class Inventario:
    def __init__(self):
        #Atributo privado
        self.__productos = {}
    
    def agregarProducto(self, producto: Producto, cantidad: int):
        if not isinstance(producto, Producto):
            raise TypeError("Solo se pueden agragar objetos de la clase producto.")
        
        #Usamos el metodo de busqueda para ver si ya existe
        productoExiste = self.buscarProducto(producto.nombre)

        if productoExiste:
            #Si existe, actualizamos el stock
            productoExiste.stock += cantidad
            print(f"Stock del producto", producto.nombre," actualizado")
        else:
            #Si es nuevo, lo agregamos al diccionario
            producto.stock = cantidad
            self.__productos[producto.nombre] = producto
            print(f"Producto ", producto.nombre, " agregado al inventario.")

    def buscarProducto(self, nombre:str) -> Producto | None:
        return self.__productos.get(nombre)
    
    def valorInventario(self) -> float:
        total = 0.0 
        for producto in self.__productos.values():
            total += producto.precio * producto.stock
        return total
    
    #Devuelve cantidad de productos unicos en el inventario
    def __len__(self) -> int:
        return len(self.__productos)
    
    #Representacion del inventario completo
    def __str__(self) -> str:
        if not self.__productos:
            return "El inventario esta vacio."
        
        titulo = "INVENTARIO DE LA TIENDA \n"
        #Generador para unir cada producto en un formato legible
        strListadoProductos = []
        for producto in self.__productos.values():
            strListadoProductos.append(str(producto))

        listadoProductos = "\n".join(strListadoProductos)
        total = f"\nValor total del inventario ${self.valorInventario():,.2f}"
        return titulo + listadoProductos + total

if __name__ == "__main__":

    #Creamos el inventarios
    miInventario = Inventario()
    print("Inventario creado. \n")

    #Creacion de los productos
    p1 = Producto("Ruedas", 2500)
    p2 = Producto("Aceite", 500)
    p3 = Producto("Trapos", 120)
    p4 = Producto("Cera", 170)

    #Agregamos los productos con un stock inicial
    miInventario.agregarProducto(p1, 12)
    miInventario.agregarProducto(p2, 50)
    miInventario.agregarProducto(p3, 70)
    miInventario.agregarProducto(p4, 65)

    #Imprimimos el estado inicial del inventario
    print("\n" + str(miInventario))

    #Modificacion del stock y precios
    print("\nModificando stock y precios")
    productoRueda = miInventario.buscarProducto("Ruedas")
    if productoRueda:
        productoRueda.stock -= 2 
        productoRueda.precio = 2300
        print("Venta de dos ruedas y reduccion de precio.")
    
    #Modificaion no valida
    try:
        productoRueda.stock = -5
    except ValueError as e:
        print("Error controlado", e)
    
    print("\n" + str(miInventario))

    #Localizacion de un producto
    print("\nBuscando productos")
    busqueda = miInventario.buscarProducto("Aceite")
    if busqueda:
        print("Producto encontrado ", busqueda)
    else:
        print("No se encontro el producto")

    #Comparacion de productos
    print("Comparando productos")
    productoA = Producto("Trapos", 100)
    productoB = miInventario.buscarProducto("Trapos")

    if productoA == productoB:
        print(productoA, " y ", productoB, " se consideran el mismo producto.")
    
    print("\nCantidad de tipos de productos en el inventario: ", len(miInventario))