from Proveedores import proveedor
from Productos import Producto
global prov1,Prod1
opcion= ""
prod1= Producto
prov1= proveedor

while(opcion!=5):
    print("1. Agregar Proveedor")
    print("2. Crear Un Producto")
    print("3. Agregar producto a Proveedor")
    print("4. Listar Productos")
    print("5. SALIR")
    print("Ingrese la Opcion que Desea")

    opcion = int(input())
    if opcion== 1:
            prov1=proveedor()
            apellido= input("Ingrese apelldios: ")
            nombre= input("Ingrese el nombre: ")
            telefono = input("Ingrese telefono: ")

            prov1.AgregarProveedor(apellido,nombre,telefono)

    elif opcion == 2:
            Prod1= Producto()
            codigo= int(input("Ingrese el codigo del producto: "))
            nomproducto= input("Ingrese el nombre del producto: ")
            precio= int(input("Ingrese el precio del producto: "))

            prod1.CrearProducto(codigo,nomproducto,precio)

    elif opcion == 3:
            prov1.AgregarProdutos(prod1)

    elif opcion == 4:
            prod1.ListaDeProductos()