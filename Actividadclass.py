
suma = 0
while True:
    num = int(float(input("Ingresa un numero: ")))
    
    if num == 0:
        break
    suma += num

print("El total de la suma es: ", suma)

#2

usuario_correcto = "Angel"
contraseña_correcta = "1234"

for i in range (3):
    usuario = input("Ingrese su usuario: ")
    contraseña = input ("Ingrese su contraseña: ")
    
if usuario == usuario_correcto and contraseña == contraseña_correcta:
    print("Puede ingresar")
    break
    print ("Te quedan ", 2 - i, " intentos")
else:
    print("Haz agotado los 3 intentos")
