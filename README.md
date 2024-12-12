# Sistema de Gestión de Inventario para Supermercado

Este proyecto implementa un sistema básico de gestión de inventario en Python. Es ideal para administrar productos en un entorno de supermercado, permitiendo operaciones como agregar, modificar, eliminar y consultar productos.

## 🚀 Funcionalidades

- **Agregar Producto**: Permite incluir un nuevo producto con nombre, cantidad y precio.
- **Modificar Producto**: Permite actualizar la cantidad y el precio de un producto existente.
- **Eliminar Producto**: Remueve un producto del inventario por su nombre.
- **Consultar Productos**: Muestra todos los productos en el inventario, indicando su nombre, cantidad y precio.
- **Menú Interactivo**: Un menú en consola que guía al usuario en la gestión del inventario.

## 📂 Estructura del Código

### Clase `Producto`
Define los atributos y métodos básicos de un producto:
- **Atributos**: `nombre`, `cantidad`, `precio`.
- **Métodos**: Modificar atributos, representación en texto.

### Clase `Inventario`
Gestiona un conjunto de productos con las siguientes funcionalidades:
- Agregar productos.
- Modificar productos existentes.
- Eliminar productos.
- Mostrar el inventario completo.

### Función Principal (`main`)
- Crea una instancia de `Inventario`.
- Ofrece un menú interactivo con las opciones mencionadas.
- Maneja entradas del usuario y controla el flujo del programa.

## 🛠️ Requisitos

- Python 3.6 o superior.

## 📋 Cómo Usar

1. Clona este repositorio:  
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git

2. Navega al directorio del proyecto:
cd tu-repositorio

3. Ejecuta el script:
python Supermarket.py

4. Sigue las instrucciones del menú en consola:

1. Agregar producto
2. Modificar producto
3. Eliminar producto
4. Consultar productos
5. Salir
Seleccione una opción: 1
Nombre del producto: Manzanas
Cantidad: 10
Precio: 2.5
Producto agregado exitosamente.


Este README está estructurado para proporcionar toda la información relevante del proyecto y facilitar su comprensión a otros usuarios o colaboradores.
