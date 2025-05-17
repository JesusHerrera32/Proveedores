class Producto:
    def __init__(self):
        pass
        
    
    def CrearProducto(self,codigo,nombre,precio):
        self.codigo= codigo
        self.nombre= nombre
        self.precio= precio

    def __str__(self) :
          f"{self.codigo} {self.nombre} {self.precio}"


    def ListaDeProductos():
        for MisProductos in Producto:
            print(f"{MisProductos}")
