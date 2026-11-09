class Artista:
    def __init__(self, nombre: str, genero: str, popularidad: int):
        self.nombre = nombre
        self.genero = genero
        self.popularidad = popularidad

    def presentarse(self):
        """Imprime un mensaje genérico de presentación."""
        print(f"¡Hola a todos! Soy {self.nombre}, toco música del género {self.genero} "
            f"y estoy muy feliz de estar en este festival (Popularidad: {self.popularidad}/100).")

    def actuar(self):
        """Método base para la actuación. Será sobrescrito por las subclases."""
        print(f"{self.nombre} está realizando una actuación en el escenario.")

    def despedirse(self):
        """Imprime un mensaje de despedida."""
        print(f"¡Muchas gracias a todos! Nos vemos pronto. ¡Se despide {self.nombre}!")

class Cantante(Artista):
    def __init__(self, nombre: str, genero: str, popularidad: int, cancion_mas_popular: str):
        super().__init__(nombre, genero, popularidad)
        self.cancion_mas_popular = cancion_mas_popular

    def actuar(self):
        print(f"{self.nombre} canta su éxito {self.cancion_mas_popular} con gran energía.")


class DJ(Artista):
    def __init__(self, nombre: str, genero: str, popularidad: int, estilo: str):
        super().__init__(nombre, genero, popularidad)
        self.estilo = estilo

    def actuar(self):
        print(f"El DJ {self.nombre} mezcla temas de estilo {self.estilo}, haciendo vibrar al público.")


class Banda(Artista):
    def __init__(self, nombre: str, genero: str, popularidad: int, integrantes: int):
        super().__init__(nombre, genero, popularidad)
        self.integrantes = integrantes

    def actuar(self):
        print(f"La banda {self.nombre} con {self.integrantes} integrantes toca un poderoso solo de guitarra.")

def iniciar_festival(lista_artistas: list):
    print("\n" + "=" * 55)
    print("      ¡BIENVENIDOS AL GRAN FESTIVAL MUSICAL!       ")
    print("=" * 55 + "\n")

    if not lista_artistas:
        print("No hay artistas registrados en el festival.")
        return

    for i, artista in enumerate(lista_artistas, 1):
        print(f"--- Acto #{i} en Vivo ---")
        artista.presentarse()
        artista.actuar()
        artista.despedirse()
        print("\n Fin de la actuación \n" + "-" * 55 + "\n")

def pedir_entero(mensaje: str, min_val: int = None, max_val: int = None) -> int:
    while True:
        try:
            valor = int(input(mensaje).strip())
            if min_val is not None and valor < min_val:
                print(f" El valor no puede ser menor a {min_val}.")
                continue
            if max_val is not None and valor > max_val:
                print(f" El valor no puede ser mayor a {max_val}.")
                continue
            return valor
        except ValueError:
            print(" Entrada inválida. Por favor ingresa un número entero.")


def main():
    print(" Sistema de Gestión del Festival Musical \n")
    
    cantidad = pedir_entero("¿Cuántos artistas se presentarán en el festival?: ", min_val=1)
    lista_artistas = []

    for i in range(1, cantidad + 1):
        print(f"\n--- Registro del Artista #{i} ---")
        
        print("Selecciona el tipo de artista:")
        print("  1. Cantante")
        print("  2. DJ")
        print("  3. Banda")
        opcion = pedir_entero("Ingresa una opción (1-3): ", min_val=1, max_val=3)

        nombre = input("Nombre del artista/grupo: ").strip()
        genero = input("Género musical (ej. Rock, Electrónica, Pop, etc.): ").strip()
        popularidad = pedir_entero("Nivel de popularidad (1 al 100): ", min_val=1, max_val=100)

        if opcion == 1:
            cancion_mas_popular = input("Canción más popular: ").strip()
            artista = Cantante(nombre, genero, popularidad, cancion_mas_popular)
        elif opcion == 2:
            estilo = input("Estilo de mezcla (ej. House, Techno, Trance, etc.): ").strip()
            artista = DJ(nombre, genero, popularidad, estilo)
        elif opcion == 3:
            integrantes = pedir_entero("Número de integrantes: ", min_val=1)
            artista = Banda(nombre, genero, popularidad, integrantes)

        lista_artistas.append(artista)

    iniciar_festival(lista_artistas)


if __name__ == "__main__":
    main()