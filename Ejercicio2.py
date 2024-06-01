"""En un supermercado una ama de casa pone en su carrito los artículos que
va tomando de los estantes. La señora quiere asegurarse de que el cajero
le cobre bien lo que ella ha comprado, por lo que cada vez que toma un
artículo anota su precio junto con la cantidad de artículos iguales que ha
tomado y determina cuánto dinero gastara en ese artículo; a esto le suma lo
que ira gastando en los demás artículos, hasta que decide que ya gasto su
presupuesto. Ayúdale a esta señora a obtener el total de sus compras."""



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