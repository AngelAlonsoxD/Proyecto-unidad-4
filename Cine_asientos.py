def pedir_entero_positivo(mensaje):
    """Solicita un número entero positivo mayor a cero con validación."""
    while True:
        try:
            valor = int(input(mensaje).strip())
            if valor > 0:
                return valor
            print(" Error: Debes ingresar un número mayor a 0. Intenta de nuevo.")
        except ValueError:
            print(" Error: Por favor ingresa un número entero válido.")


def crear_sala(filas, columnas):
    return [["L" for _ in range(columnas)] for _ in range(filas)]


def mostrar_sala(sala):
    filas = len(sala)
    columnas = len(sala[0])
    
    print("\n" + "=" * 45)
    print("            PANTALLA DEL CINE ")
    print("=" * 45)
    
    # Encabezado con número de columnas
    encabezado_cols = "       " + " ".join(f"{col:2d}" for col in range(1, columnas + 1))
    print(encabezado_cols)
    print("     " + "-" * (columnas * 3 + 2))
    
    # Filas con sus respectivos asientos
    for idx_f, fila in enumerate(sala, start=1):
        fila_str = " ".join(f" {asiento}" for asiento in fila)
        print(f"Fila {idx_f:2d} |{fila_str} ")
    
    print("=" * 45)
    print("Leyenda: [L] = Libre | [X] = Ocupado\n")


def pedir_coordenada(filas, columnas):
    while True:
        try:
            f = int(input(f"Ingresa el número de fila (1 a {filas}): ").strip())
            c = int(input(f"Ingresa el número de columna (1 a {columnas}): ").strip())
            
            # Validación de existencia dentro del rango
            if 1 <= f <= filas and 1 <= c <= columnas:
                return f - 1, c - 1  # Convertir a índices basados en 0
            else:
                print(f" Error: El asiento no existe. La sala tiene {filas} filas y {columnas} columnas.\n")
        except ValueError:
            print(" Error: Por favor ingresa números enteros válidos.\n")


def reservar_asiento(sala):
    filas = len(sala)
    columnas = len(sala[0])
    
    print("\n---  RESERVAR ASIENTO ---")
    f_idx, c_idx = pedir_coordenada(filas, columnas)
    
    if sala[f_idx][c_idx] == "L":
        sala[f_idx][c_idx] = "X"
        print(f" ¡Éxito! El asiento en la Fila {f_idx + 1}, Columna {c_idx + 1} ha sido reservado correctamente.")
    else:
        print(f" El asiento en la Fila {f_idx + 1}, Columna {c_idx + 1} ya está OCUPADO. No se puede reservar.")


def liberar_asiento(sala):
    filas = len(sala)
    columnas = len(sala[0])
    
    print("\n---  LIBERAR ASIENTO ---")
    f_idx, c_idx = pedir_coordenada(filas, columnas)
    
    if sala[f_idx][c_idx] == "X":
        sala[f_idx][c_idx] = "L"
        print(f" ¡Éxito! El asiento en la Fila {f_idx + 1}, Columna {c_idx + 1} ha sido liberado.")
    else:
        print(f" El asiento en la Fila {f_idx + 1}, Columna {c_idx + 1} ya se encontraba LIBRE.")

def contar_asientos(sala):
    total = len(sala) * len(sala[0])
    ocupados = sum(fila.count("X") for fila in sala)
    libres = sum(fila.count("L") for fila in sala)
    porcentaje_ocupacion = (ocupados / total) * 100 if total > 0 else 0
    
    print("\n" + "=" * 35)
    print("        ESTADÍSTICAS DE LA SALA")
    print("=" * 35)
    print(f"Total de asientos:   {total}")
    print(f"Asientos libres:     {libres} ")
    print(f"Asientos ocupados:   {ocupados} ")
    print(f"Ocupación actual:    {porcentaje_ocupacion:.1f}%")
    print("=" * 35 + "\n")


def mostrar_menu():
    print("*" * 35)
    print("      🎬 SISTEMA DE CINE - MENÚ")
    print("*" * 35)
    print("1. Mostrar sala")
    print("2. Reservar asiento")
    print("3. Liberar asiento")
    print("4. Contar asientos ocupados y libres")
    print("5. Salir")
    print("*" * 35)


def main():
    print("=" * 50)
    print("   BIENVENIDO AL SISTEMA DE GESTIÓN DE SALA DE CINE")
    print("=" * 50)
    
    # A) Configuración inicial de la matriz de la sala
    print("\n--- Configuración de la Sala ---")
    filas = pedir_entero_positivo("Ingresa el número de filas del cine: ")
    columnas = pedir_entero_positivo("Ingresa el número de columnas (asientos por fila): ")
    
    sala = crear_sala(filas, columnas)
    print(f"\n Sala de cine creada con éxito ({filas}x{columnas} - {filas * columnas} asientos en total).\n")
    
    # B) Bucle del menú interactivo
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ").strip()
        
        if opcion == "1":
            mostrar_sala(sala)
        elif opcion == "2":
            reservar_asiento(sala)
        elif opcion == "3":
            liberar_asiento(sala)
        elif opcion == "4":
            contar_asientos(sala)
        elif opcion == "5":
            print("\n ¡Gracias por usar el sistema de cine! Hasta pronto.\n")
            break
        else:
            print("\n Opción no válida. Por favor, elige un número del 1 al 5.\n")


if __name__ == "__main__":
    main()