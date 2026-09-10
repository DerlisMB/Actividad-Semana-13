def calcular_total(precio, cantidad):
    """
    Calcula el total de una compra multiplicando el precio unitario
    por la cantidad de productos.
    """
    total = precio * cantidad
    return total


if __name__ == "__main__":
    # Valores de ejemplo
    precio = 10
    cantidad = 3

    # Llamada a la función
    resultado = calcular_total(precio, cantidad)

    # Mostrar el resultado en consola
    print(f"El total de la compra es: {resultado}")