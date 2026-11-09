
class Pokemon:
    """Representa un Pokémon y sus estadísticas."""

    _total_creados = 0

    def __init__(self, nombre, tipo, ataque, defensa, salud, nivel=1):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud

        Pokemon._total_creados += 1
        print(f"✨ ¡{self.nombre} ha sido creado!")

    def __del__(self):
        try:
            print(f"🕊️ {self.nombre} ha sido liberado.")
        except AttributeError:
            pass

    def entrenar(self, *mejoras):
        """Mejora las estadísticas y aumenta el nivel."""

        if not mejoras:
            mejoras = (2, 1, 5)
        elif len(mejoras) > 3:
            print("Máximo 3 valores: ataque, defensa y salud.")
            return

        if any(not isinstance(x, int) or x < 0 for x in mejoras):
            print("Las mejoras deben ser enteros no negativos.")
            return

        estadisticas = ["ataque", "defensa", "salud"]

        for atributo, aumento in zip(estadisticas, mejoras):
            setattr(self, atributo, getattr(self, atributo) + aumento)

        self.nivel += 1
        print(f"💪 {self.nombre} subió al nivel {self.nivel}.")

    def mostrar_info(self):
        print(f"\n--- {self.nombre} ---")
        print(f"Tipo: {self.tipo}")
        print(f"Nivel: {self.nivel}")
        print(f"Ataque: {self.ataque}")
        print(f"Defensa: {self.defensa}")
        print(f"Salud: {self.salud}")

    def atacar(self, objetivo):
        if objetivo is self:
            print("No puedes atacarte a ti mismo.")
            return

        if objetivo.salud <= 0:
            print(f"{objetivo.nombre} ya no puede combatir.")
            return

        dano = max(1, self.ataque - objetivo.defensa)
        objetivo.salud = max(0, objetivo.salud - dano)

        print(
            f"⚔️ {self.nombre} ataca a {objetivo.nombre} "
            f"e inflige {dano} de daño."
        )
        print(f"Salud restante: {objetivo.salud}")

    @classmethod
    def total_pokemons(cls):
        """Muestra cuántos Pokémon se han creado."""
        print(f"🧮 Pokémon creados: {cls._total_creados}")
