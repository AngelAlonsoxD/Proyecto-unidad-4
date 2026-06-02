positivos = 0
negativos = 0
suma = 0
for i in range (25):
    num = float(input("Ingrese un numero: "))
    suma += num
    if num > 0:
        positivos += 1
    elif num < 0: 
        negativos += 1
    else:
        ceros += 1

print("Cantidad de positivos: ", positivos)
print("Cantidad de negativos: ", negativos)
print("Cantidad de ceros: ", suma)