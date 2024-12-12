# Define la clase Producto que representa un artículo del inventario con atributos y métodos relacionados.
class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def modificar(self, cantidad, precio):
        if cantidad != -1:
            self.cantidad = cantidad
        if precio != -1:
            self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if any(p.nombre == producto.nombre for p in self.productos):
            print("El producto ya existe.")
        else:
            self.productos.append(producto)
            print("Producto agregado exitosamente.")

    def modificar_producto(self, nombre, cantidad, precio):
        # Busca un producto por su nombre y actualiza su cantidad y precio si se encuentra
        for producto in self.productos:
            if producto.nombre == nombre:
                producto.modificar(cantidad, precio)
                print("Producto modificado.")
                return
        print("Producto no encontrado.")

    def eliminar_producto(self, nombre):
        # Busca y elimina el producto con el nombre proporcionado
        if any(p.nombre == nombre for p in self.productos):
            self.productos = [p for p in self.productos if p.nombre != nombre]
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    def mostrar_inventario(self):
        # Muestra todos los productos en el inventario o indica si está vacío
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)


def main():
    inventario = Inventario()
    continuar = True
    while continuar:
        print("\nMenú:")
        print("1. Agregar producto")
        print("2. Modificar producto")
        print("3. Eliminar producto")
        print("4. Consultar productos")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Solicita los datos del nuevo producto y lo agrega al inventario
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(nombre, cantidad, precio))
        elif opcion == "2":
            # Permite modificar un producto existente
            nombre = input("Nombre del producto a modificar: ")
            cantidad = input("Nueva cantidad (dejar vacío para no modificar): ")
            precio = input("Nuevo precio (dejar vacío para no modificar): ")

            cantidad = int(cantidad) if cantidad.strip() != "" else -1
            precio = float(precio) if precio.strip() != "" else -1

            inventario.modificar_producto(nombre, cantidad, precio)
        elif opcion == "3":
            # Opción del menú para eliminar un producto del inventario
            nombre = input("Nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)
        elif opcion == "4":
            # Opción del menú para mostrar todos los productos
            inventario.mostrar_inventario()
        elif opcion == "5":
            # Finaliza el programa cambiando la variable de control
            print("Saliendo del programa...")
            continuar = False
        else:
            # Maneja opciones no válidas
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()

