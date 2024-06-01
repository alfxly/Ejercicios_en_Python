total_compra = 0

print("Ingrese los precios y cantidades de los artículos.")
print("Para terminar, ingrese un precio de 0.")

for articulo in range(10):
    precio = float(input("Ingrese el precio del artículo: "))
    if precio == 0:
        break
    cantidad = int(input("Ingrese la cantidad de artículos iguales: "))
    
    total_compra += precio * cantidad
    
print("El total de la compra es:", total_compra)