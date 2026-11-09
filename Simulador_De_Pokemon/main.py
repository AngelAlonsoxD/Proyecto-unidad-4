
from clases.pokemon import Pokemon

# Variable global: almacena los Pokémon capturados.
pokemons = []


def pedir_entero(mensaje, minimo=0):
    # Variable local.
    while True:
        try:
            valor = int(input(mensaje))

            if valor < minimo:
                print(f"Introduce un número igual o mayor que {minimo}.")
                continue

            return valor

        except ValueError:
            print("Entrada inválida. Escribe un número entero.")


def elegir_pokemon():
    if not pokemons:
        print("Primero captura un Pokémon.")
        return None

    for i, pokemon in enumerate(pokemons, start=1):
        print(
            f"{i}. {pokemon.nombre} "
            f"(Nivel {pokemon.nivel}, salud {pokemon.salud})"
        )

    indice = pedir_entero("Elige el número: ", 1)

    if indice > len(pokemons):
        print("Número fuera de la lista.")
        return None

    return pokemons[indice - 1]


def capturar_pokemon():
    nombre = input("Nombre: ").strip()
    tipo = input("Tipo: ").strip()

    if not nombre or not tipo:
        print("El nombre y el tipo son obligatorios.")
        return

    ataque = pedir_entero("Ataque inicial: ", 1)
    defensa = pedir_entero("Defensa inicial: ")
    salud = pedir_entero("Salud inicial: ", 1)

    nuevo_pokemon = Pokemon(nombre, tipo, ataque, defensa, salud)
    pokemons.append(nuevo_pokemon)


def entrenar_pokemon():
    pokemon = elegir_pokemon()

    if pokemon is None:
        return

    print("\nSin valores: mejoras predeterminadas.")
    print("Introduce de 1 a 3 valores: ataque, defensa y salud.")

    entrada = input(
        "Mejoras separadas por espacios: "
    ).strip()

    if not entrada:
        pokemon.entrenar()
        return

    try:
        mejoras = tuple(int(x) for x in entrada.split())
        pokemon.entrenar(*mejoras)

    except ValueError:
        print("Introduce únicamente números enteros.")


def ver_pokemons():
    if not pokemons:
        print("No hay Pokémon capturados.")
        return

    for pokemon in pokemons:
        pokemon.mostrar_info()


def combatir():
    print("\nElige el Pokémon atacante:")
    atacante = elegir_pokemon()

    if atacante is None:
        return

    print("\nElige el Pokémon objetivo:")
    objetivo = elegir_pokemon()

    if objetivo is not None:
        atacante.atacar(objetivo)


def liberar_pokemon():
    pokemon = elegir_pokemon()

    if pokemon is None:
        return

    confirmacion = input(
        f"¿Quieres liberar a {pokemon.nombre}? (s/n): "
    ).strip().lower()

    if confirmacion == "s":
        nombre = pokemon.nombre
        pokemons.remove(pokemon)
        del pokemon
        print(f"🕊️ {nombre} ha sido retirado del equipo.")
    else:
        print("Liberación cancelada.")


def main():
    while True:
        print("\n====== SIMULADOR POKÉMON ======")
        print("1. Capturar Pokémon 🐉")
        print("2. Entrenar Pokémon 💪")
        print("3. Ver información 📋")
        print("4. Contar Pokémon creados 🧮")
        print("5. Liberar Pokémon 🕊️")
        print("6. Atacar a otro Pokémon ⚔️")
        print("0. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            capturar_pokemon()

        elif opcion == "2":
            entrenar_pokemon()

        elif opcion == "3":
            ver_pokemons()

        elif opcion == "4":
            Pokemon.total_pokemons()

        elif opcion == "5":
            liberar_pokemon()

        elif opcion == "6":
            combatir()

        elif opcion == "0":
            print("¡Hasta pronto, entrenador!")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
