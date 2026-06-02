vector = [50, 75, 46, 22, 80, 65, 8]
print ("vector original: ", vector)
max = 0
men = vector[0]

for i in range (len(vector)):
        if vector [i] > max:
            max = vector[i]
        elif vector [i] < men:
            men = vector [i]
print("men: ", men, "max: ", max)

#2
numeros = [50, 75, 46, 22, 80, 65, 8]

numeros.sort(reverse= True)
print("numeros ordenados de mayor a menor: ", numeros)

#3 Escribir un programa que pregunte al usuario los numeros ganadores de la loteria primitiva,
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor  
#InsertionSort
#SelectionSort
#Sort
