numeros = []
for i in range (6):
    n = int(input("Ingrese un numero ganador: "))
    numeros.append(n)

numeros.sort()

print ("Numeros ordenados de menor a mayor")
print(numeros)