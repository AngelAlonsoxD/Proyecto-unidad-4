class InventarioTienda:
    def __init__(self, nombre_tienda):
        self.nombre_tienda = nombre_tienda
        self.productos = []

    def agregar_producto(self, nombre, precio, cantidad):
        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
        self.productos.append(producto)
        print("Producto agregado correctamente.")

    def vender_producto(self, nombre, cantidad):
        for producto in self.productos:
            if producto["nombre"].lower() == nombre.lower():
                if producto["cantidad"] >= cantidad:
                    producto["cantidad"] -= cantidad
                    print("Venta realizada con éxito.")
                else:
                    print("No hay suficiente stock.")
                return
        print("El producto no existe.")

    def mostrar_inventario(self):
        if len(self.productos) == 0:
            print("\nEl inventario está vacío.")
        else:
            print(f"\nInventario de {self.nombre_tienda}")
            print("-" * 40)
            for producto in self.productos:
                print(f"Nombre: {producto['nombre']}")
                print(f"Precio: ${producto['precio']:.2f}")
                print(f"Cantidad: {producto['cantidad']}")
                print("-" * 40)

    def producto_mas_caro(self):
        if len(self.productos) == 0:
            print("No hay productos en el inventario.")
            return

        mas_caro = self.productos[0]

        for producto in self.productos:
            if producto["precio"] > mas_caro["precio"]:
                mas_caro = producto

        print(f"Producto más caro: {mas_caro['nombre']}")
        print(f"Precio: ${mas_caro['precio']:.2f}")


# Programa principal
nombre = input("Ingrese el nombre de la tienda: ")
tienda = InventarioTienda(nombre)

while True:
    print("\n===== MENÚ =====")
    print("1. Agregar producto")
    print("2. Vender producto")
    print("3. Mostrar inventario")
    print("4. Producto más caro")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre_producto = input("Nombre del producto: ")

        precio = float(input("Precio: "))
        if precio <= 0:
            print("El precio debe ser mayor que 0.")
            continue

        cantidad = int(input("Cantidad: "))
        if cantidad <= 0:
            print("La cantidad debe ser mayor que 0.")
            continue

        tienda.agregar_producto(nombre_producto, precio, cantidad)

    elif opcion == "2":
        nombre_producto = input("Nombre del producto: ")

        cantidad = int(input("Cantidad a vender: "))
        if cantidad <= 0:
            print("La cantidad debe ser mayor que 0.")
            continue

        tienda.vender_producto(nombre_producto, cantidad)

    elif opcion == "3":
        tienda.mostrar_inventario()

    elif opcion == "4":
        tienda.producto_mas_caro()

    elif opcion == "5":
        print("Gracias por usar el sistema.")
        break

    else:
        print("Opción no válida.")