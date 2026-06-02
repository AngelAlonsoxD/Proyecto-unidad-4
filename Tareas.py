def obtener_rango(lv):
    match True:
        case _ if 1 <= lv <= 10:
            return "Aprendiz"
        case _ if 11 <= lv <= 30:
            return "Guerrero"
        case _ if 31 <= lv <= 60:
            return "Élite"
        case _ if 61 <= lv <= 99:
            return "Leyenda"
        case _ if lv == 100:
            return "Maestro Supremo"
        case _:
            return "Inválido"

def datos(nom, lv):
    if lv < 1:
        print("Error en nivel")
    else:
        r = obtener_rango(lv)
        print(f"Nombre: {nom}")
        print(f"Nivel: {lv}")
        print(f"Rango: {r}")

datos("Arthas", 45)

#2

prods = ["Manzana", "Leche", "Pan", "Arroz", "Huevo"]
pre = [15.00, 22.50, 18.00, 35.00, 28.00]
cant = [100, 50, 75, 60, 200]

print("Lista de productos:\n")

valores = []
for p, pr, c in zip(prods, pre, cant):
    total = pr * c
    valores.append(total)
    print(f"{p} | Precio: {pr} | Cantidad: {c} | Total: {total}")

mayor_precio = 0
nombre_mayor = ""

for p, pr in zip(prods, pre):
    if pr > mayor_precio:
        mayor_precio = pr
        nombre_mayor = p

stock_bajo = sum(1 for c in cant if c < 70)

print("\nProducto más caro:", nombre_mayor)
print("Precio:", mayor_precio)
print("Productos con poco stock:", stock_bajo)
