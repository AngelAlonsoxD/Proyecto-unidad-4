def pedir_entero_positivo(mensaje):
    """Solicita un número entero estrictamente mayor a 0 con validación."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print(" Por favor, ingresa un número entero mayor a 0.")
        except ValueError:
            print(" Entrada inválida. Debes ingresar un número entero.")

def pedir_flotante_positivo(mensaje):
    """Solicita un número decimal (float) estrictamente mayor a 0 con validación."""
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            print(" Por favor, ingresa un número mayor a 0.")
        except ValueError:
            print(" Entrada inválida. Debes ingresar un número válido (ej. 3.5).")

def pedir_popularidad(mensaje):
    
    while True:
        try:
            valor = int(input(mensaje))
            if 1 <= valor <= 100:
                return valor
            print("❌ La popularidad debe estar en el rango de 1 a 100.")
        except ValueError:
            print(" Entrada inválida. Debes ingresar un número entero del 1 al 100.")

def agregar_canciones(nombres, artistas, duraciones, popularidades):
    
    print("\n" + "=" * 50)
    print("         REGISTRO DE CANCIONES")
    print("=" * 50)
    
    cantidad = pedir_entero_positivo("¿Cuántas canciones deseas agregar?: ")
    
    for i in range(1, cantidad + 1):
        print(f"\n--- Canción #{len(nombres) + 1} ---")
        
        while True:
            nombre = input("Nombre de la canción: ").strip()
            if nombre:
                break
            print(" El nombre no puede estar vacío.")
            
        while True:
            artista = input("Artista: ").strip()
            if artista:
                break
            print(" El artista no puede estar vacío.")
            
        duracion = pedir_flotante_positivo("Duración en minutos (ej. 3.45): ")
        popularidad = pedir_popularidad("Popularidad (1-100): ")
        
        # Almacenamiento en listas separadas (listas paralelas)
        nombres.append(nombre)
        artistas.append(artista)
        duraciones.append(duracion)
        popularidades.append(popularidad)
        
        print(f" ¡'{nombre}' registrada con éxito!")
        
    print(f"\n✨ Se han agregado {cantidad} canción(es). Total en la playlist: {len(nombres)}.")

def generar_reportes(nombres, artistas, duraciones, popularidades):
    
    print("\n" + "=" * 50)
    print("         REPORTES DE LA PLAYLIST")
    print("=" * 50)
    
    if not nombres:
        print(" No hay canciones registradas en la playlist.")
        print(" Usa la opción 1 para agregar canciones primero.")
        return

    total_canciones = len(nombres)
    duracion_total = sum(duraciones)
    horas = int(duracion_total // 60)
    minutos_restantes = duracion_total % 60
    
    max_pop = max(popularidades)
    min_pop = min(popularidades)
    promedio_pop = sum(popularidades) / total_canciones
    
    print(f" Número total de canciones: {total_canciones}")
    if horas > 0:
        print(f"  Duración total: {duracion_total:.2f} minutos ({horas} h {minutos_restantes:.2f} min)")
    else:
        print(f"  Duración total: {duracion_total:.2f} minutos")
    
    print(f" Promedio de popularidad: {promedio_pop:.2f} / 100")
    
    # Canción más popular (soporta empates)
    print(f"\n Canción más popular (Popularidad: {max_pop}/100):")
    for i in range(total_canciones):
        if popularidades[i] == max_pop:
            print(f"   • '{nombres[i]}' - {artistas[i]} ({duraciones[i]:.2f} min)")
            
    # Canción menos popular (soporta empates)
    print(f"\n Canción menos popular (Popularidad: {min_pop}/100):")
    for i in range(total_canciones):
        if popularidades[i] == min_pop:
            print(f"   • '{nombres[i]}' - {artistas[i]} ({duraciones[i]:.2f} min)")

def buscar_canciones(nombres, artistas, duraciones, popularidades):
    print("\n" + "=" * 50)
    print("         FILTRAR CANCIONES")
    print("=" * 50)
    
    if not nombres:
        print(" No hay canciones registradas para buscar.")
        return

    print("1. Buscar por artista")
    print("2. Buscar por rango de popularidad")
    print("3. Volver al menú principal")
    
    opcion = input("Elige una opción (1-3): ").strip()
    
    if opcion == "1":
        termino = input("\nIngresa el nombre o fragmento del artista: ").strip().lower()
        if not termino:
            print(" La búsqueda no puede estar vacía.")
            return
            
        coincidencias = []
        for i in range(len(nombres)):
            if termino in artistas[i].lower():
                coincidencias.append(i)
                
        if coincidencias:
            print(f"\n Se encontraron {len(coincidencias)} canción(es) asociadas a '{termino}':")
            print("-" * 65)
            print(f"{'#':<4}{'Canción':<25}{'Artista':<20}{'Duración':<10}{'Pop':<5}")
            print("-" * 65)
            for idx in coincidencias:
                print(f"{idx+1:<4}{nombres[idx][:23]:<25}{artistas[idx][:18]:<20}{duraciones[idx]:<10.2f}{popularidades[idx]:<5}")
            print("-" * 65)
        else:
            print(f" No se encontraron canciones para el artista '{termino}'.")
        
    elif opcion == "2":
        print("\nDefine el rango de popularidad (1 a 100):")
        min_val = pedir_popularidad("Popularidad mínima: ")
        max_val = pedir_popularidad("Popularidad máxima: ")
        
        if min_val > max_val:
            print(" El mínimo era mayor que el máximo. Intercambiando valores automáticamente...")
            min_val, max_val = max_val, min_val
            
        coincidencias = []
        for i in range(len(nombres)):
            if min_val <= popularidades[i] <= max_val:
                coincidencias.append(i)
                
        if coincidencias:
            print(f"\n🔍 Se encontraron {len(coincidencias)} canción(es) con popularidad entre {min_val} y {max_val}:")
            print("-" * 65)
            print(f"{'#':<4}{'Canción':<25}{'Artista':<20}{'Duración':<10}{'Pop':<5}")
            print("-" * 65)
            for idx in coincidencias:
                print(f"{idx+1:<4}{nombres[idx][:23]:<25}{artistas[idx][:18]:<20}{duraciones[idx]:<10.2f}{popularidades[idx]:<5}")
            print("-" * 65)
        else:
            print(f" No se encontraron canciones en el rango [{min_val} - {max_val}].")
            
    elif opcion == "3":
        return
    else:
        print(" Opción no válida.")

def playlist_recomendada(nombres, artistas, duraciones, popularidades):
    print("\n" + "=" * 50)
    print("       PLAYLIST RECOMENDADA (TOP HITS)")
    print("=" * 50)
    
    if not nombres:
        print(" No hay canciones registradas en la playlist.")
        return
        
    promedio_pop = sum(popularidades) / len(popularidades)
    
    # Filtrar canciones con popularidad estrictamente superior al promedio
    recomendadas = [i for i in range(len(nombres)) if popularidades[i] > promedio_pop]
    
    print(f" Umbral de corte (Popularidad promedio): {promedio_pop:.2f}/100")
    
    if not recomendadas:
        print("ℹ Ninguna canción supera estrictamente el promedio.")
        return
        
    # Ordenar por popularidad descendente para presentar los mejores temas primero
    recomendadas_ordenadas = sorted(recomendadas, key=lambda i: popularidades[i], reverse=True)
    
    print(f" ¡{len(recomendadas)} canción(es) destacada(s) para los escenarios principales!\n")
    print("-" * 65)
    print(f"{'#':<4}{'Canción':<25}{'Artista':<20}{'Duración':<10}{'Pop':<5}")
    print("-" * 65)
    
    duracion_recomendada = 0.0
    for pos, idx in enumerate(recomendadas_ordenadas, start=1):
        duracion_recomendada += duraciones[idx]
        print(f"{pos:<4}{nombres[idx][:23]:<25}{artistas[idx][:18]:<20}{duraciones[idx]:<10.2f}{popularidades[idx]:<5}")
    print("-" * 65)
    print(f" Duración de la playlist recomendada: {duracion_recomendada:.2f} minutos.")

def main():
    # Listas paralelas requeridas
    nombres = []
    artistas = []
    duraciones = []
    popularidades = []
    
    while True:
        print("\n" + "=" * 50)
        print("       FESTIVAL DE MÚSICA - SMART PLAYLIST ")
        print("=" * 50)
        print("1. Agregar canciones")
        print("2. Ver reportes")
        print("3. Buscar canciones")
        print("4. Playlist recomendada")
        print("5. Salir")
        print("=" * 50)
        
        opcion = input("Selecciona una opción (1-5): ").strip()
        
        if opcion == "1":
            agregar_canciones(nombres, artistas, duraciones, popularidades)
        elif opcion == "2":
            generar_reportes(nombres, artistas, duraciones, popularidades)
        elif opcion == "3":
            buscar_canciones(nombres, artistas, duraciones, popularidades)
        elif opcion == "4":
            playlist_recomendada(nombres, artistas, duraciones, popularidades)
        elif opcion == "5":
            print("\n ¡Gracias por usar Festival Smart Playlist! ¡Éxito en el festival! \n")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción del 1 al 5.")

if __name__ == "__main__":
    main()