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
            return f"Nombre:", self.nombre, " Precio: ", self.precio, .2,"Stock: ", self.stock
        
        def __eq__(self, other) -> bool:
            if not isinstance(other, Producto):
                return NotImplemented
            return self.nombre.lower() == other.nombre.lower()
            