def main():
    # Preguntar el número de estudiantes y materias
    estudiantes = int(input("¿Cuántos estudiantes hay en el grupo? "))
    materias = int(input("¿Cuántas materias tiene el grupo? "))

    # Crear matriz para calificaciones
    calificaciones = []

    print("\nIngresa las calificaciones (0-100):")

    for i in range(estudiantes):
        fila = []
        for j in range(materias):
            while True:
                try:
                    nota = float(input(f"  Estudiante {i + 1}, Materia {j + 1}: "))
                    if 0 <= nota <= 100:
                        fila.append(nota)
                        break
                    else:
                        print("    ¡Error! La calificación debe estar entre 0 y 100.")
                except ValueError:
                    print("    Entrada inválida, ingresa un número.")
        calificaciones.append(fila)

    # Calcular promedio por estudiante
    promedios_estudiantes = [sum(filas) / materias for filas in calificaciones]

    # Calcular promedio por materia
    promedios_materias = []
    for j in range(materias):
        suma = sum(calificaciones[i][j] for i in range(estudiantes))
        promedios_materias.append(suma / estudiantes)

    # Calificación más alta y más baja
    todas_notas = [nota for filas in calificaciones for nota in filas]
    max_nota = max(todas_notas)
    min_nota = min(todas_notas)

    # Imprimir resultados
    print("\nResultados:")
    print("Promedio por estudiante:")
    for i, promedio in enumerate(promedios_estudiantes, 1):
        print(f"  Estudiante {i}: {promedio:.2f}")

    print("\nPromedio por materia:")
    for j, promedio in enumerate(promedios_materias, 1):
        print(f"  Materia {j}: {promedio:.2f}")

    print(f"\nCalificación más alta: {max_nota:.2f}")
    print(f"Calificación más baja: {min_nota:.2f}")

if __name__ == "__main__":
    main()
