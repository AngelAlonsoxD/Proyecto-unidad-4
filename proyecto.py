# ============================================================
# PROYECTO 2 - JUEGO DE TRIVIA
# Fundamentos de proramacion
# Nombre: Angel Roberto Alonso Guerrero
# ============================================================

import random
import time
import os

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")
def pausa():
    input("\nPresiona ENTER para continuar...")
def mostrar_titulo():
    print("=" * 60)
    print("              JUEGO DE TRIVIA")                          
    print("=" * 60)
def mostrar_reglas():
    limpiar()
    mostrar_titulo()
    print("\nREGLAS DEL JUEGO:\n")
    print("1. Cada jugador inicia con 3 vidas.")
    print("2. Cada respuesta correcta vale 10 puntos.")
    print("3. Cada respuesta incorrecta resta 1 vida.")
    print("4. El jugador con más puntos gana.")
    print("5. Las preguntas aparecen aleatoriamente.")
    print("6. Hay diferentes categorías.")
    print("7. Debes responder usando A, B, C o D.")
    pausa()

def mostrar_creditos():
    limpiar()
    mostrar_titulo()
    print("\nCRÉDITOS\n")
    print("Proyecto realizado por:")
    print("Angel Roberto Alonso Guerrero")
    print("Materia: Programación")
    print("Lenguaje utilizado: Python")
    print("Tema: Juego de Trivia")
    pausa()
class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre
class Pregunta:
    def __init__(self,
                enunciado,
                opciones,
                respuesta_correcta,
                categoria,
                dificultad):
        self.enunciado = enunciado
        self.opciones = opciones
        self.respuesta_correcta = respuesta_correcta
        self.categoria = categoria
        self.dificultad = dificultad
    def mostrar_pregunta(self):
        print("\n--------------------------------------")
        print("Categoría:", self.categoria)
        print("Dificultad:", self.dificultad)
        print("--------------------------------------")
        print("\n" + self.enunciado)
        letras = ["A", "B", "C", "D"]
        for i in range(4):
            print(letras[i] + ". " + self.opciones[i])
    def verificar_respuesta(self, respuesta_usuario):
        letras = ["A", "B", "C", "D"]
        if respuesta_usuario.upper() in letras:
            indice = letras.index(respuesta_usuario.upper())
            return self.opciones[indice] == self.respuesta_correcta
        return False
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntaje = 0
        self.vidas = 3
        self.aciertos = 0
        self.errores = 0
    def sumar_puntos(self):
        self.puntaje += 10
        self.aciertos += 1
    def perder_vida(self):
        self.vidas -= 1
        self.errores += 1
    def ganar_vida(self):
        self.vidas += 1
    def mostrar_info(self):
        print("\nJugador:", self.nombre)
        print("Puntaje:", self.puntaje)
        print("Vidas:", self.vidas)
        print("Aciertos:", self.aciertos)
        print("Errores:", self.errores)
    def reiniciar(self):
        self.puntaje = 0
        self.vidas = 3
        self.aciertos = 0
        self.errores = 0
class Partida:
    def __init__(self):
        self.rondas = 0
    def aumentar_ronda(self):
        self.rondas += 1
preguntas = [
    Pregunta(
        "¿Cuál es la capital de México?",
        ["Guadalajara", "Monterrey", "Ciudad de México", "Puebla"],
        "Ciudad de México",
        "Geografía",
        "Fácil"
    ),
    Pregunta(
        "¿Cuánto es 5 x 6?",
        ["20", "30", "25", "40"],
        "30",
        "Matemáticas",
        "Fácil"
    ),
    Pregunta(
        "¿Qué planeta es conocido como el planeta rojo?",
        ["Venus", "Marte", "Saturno", "Júpiter"],
        "Marte",
        "Ciencia",
        "Fácil"
    ),
    Pregunta(
        "¿Quién creó Python?",
        ["Bill Gates", "Guido van Rossum", "Elon Musk", "Steve Jobs"],
        "Guido van Rossum",
        "Programación",
        "Media"
    ),
    Pregunta(
        "¿Qué significa HTML?",
        ["Hyper Text Markup Language",
        "High Transfer Machine Language",
        "Hyperlink Machine Language",
        "Home Tool Markup Language"],
        "Hyper Text Markup Language",
        "Programación",
        "Media"
    ),
    Pregunta(
        "¿Cuál es el océano más grande?",
        ["Atlántico", "Pacífico", "Índico", "Ártico"],
        "Pacífico",
        "Geografía",
        "Fácil"
    ),
    Pregunta(
        "¿Cuánto es 15 + 25?",
        ["35", "40", "45", "50"],
        "40",
        "Matemáticas",
        "Fácil"
    ),
    Pregunta(
        "¿Cuál es el lenguaje principal de Android?",
        ["Python", "Java", "C#", "Swift"],
        "Java",
        "Programación",
        "Media"
    ),
    Pregunta(
        "¿Quién pintó la Mona Lisa?",
        ["Picasso", "Da Vinci", "Van Gogh", "Miguel Ángel"],
        "Da Vinci",
        "Arte",
        "Media"
    ),
    Pregunta(
        "¿Cuál es el resultado de 9 x 9?",
        ["72", "81", "99", "90"],
        "81",
        "Matemáticas",
        "Fácil"
    ),
    Pregunta(
        "¿Qué gas respiramos?",
        ["Oxígeno", "Nitrógeno", "Hidrógeno", "Helio"],
        "Oxígeno",
        "Ciencia",
        "Fácil"
    ),
    Pregunta(
        "¿Cuál es el país más grande del mundo?",
        ["China", "Canadá", "Rusia", "Estados Unidos"],
        "Rusia",
        "Geografía",
        "Media"
    ),
    Pregunta(
        "¿Qué lenguaje usa iOS?",
        ["Swift", "Java", "Python", "PHP"],
        "Swift",
        "Programación",
        "Media"
    ),
    Pregunta(
        "¿Cuántos continentes existen?",
        ["5", "6", "7", "8"],
        "7",
        "Geografía",
        "Fácil"
    ),
    Pregunta(
        "¿Quién descubrió América?",
        ["Napoleón", "Cristóbal Colón", "Newton", "Galileo"],
        "Cristóbal Colón",
        "Historia",
        "Fácil"
    )
]
def registrar_jugadores():
    jugadores = []
    while True:
        try:
            cantidad = int(input("¿Cuántos jugadores participarán?: "))
            if cantidad > 0:
                break
            else:
                print("Debes ingresar mínimo 1 jugador.")
        except:
            print("Ingresa un número válido.")
    for i in range(cantidad):
        nombre = input(f"Ingrese el nombre del jugador {i+1}: ")
        jugadores.append(Jugador(nombre))
    return jugadores
def mostrar_ranking(jugadores):
    jugadores.sort(key=lambda x: x.puntaje, reverse=True)
    print("\n================ RANKING ================\n")
    posicion = 1
    for jugador in jugadores:
        print(str(posicion) + ".",
            jugador.nombre,
            "-",
            jugador.puntaje,
            "puntos")
        posicion += 1
def guardar_puntajes(jugadores):
    archivo = open("puntajes.txt", "a")
    archivo.write("\n===== RESULTADOS =====\n")
    for jugador in jugadores:
        archivo.write(
            jugador.nombre +
            " - " +
            str(jugador.puntaje) +
            " puntos\n"
        )
    archivo.close()
def iniciar_juego():
    limpiar()
    mostrar_titulo()
    jugadores = registrar_jugadores()
    partida = Partida()
    random.shuffle(preguntas)
    print("\nIniciando juego...")
    time.sleep(2)
    for pregunta in preguntas:
        jugadores_activos = [j for j in jugadores if j.vidas > 0]
        if len(jugadores_activos) == 0:
            break
        partida.aumentar_ronda()
        print("\n======================================")
        print("RONDA:", partida.rondas)
        print("======================================")
        for jugador in jugadores:
            if jugador.vidas <= 0:
                continue
            jugador.mostrar_info()
            pregunta.mostrar_pregunta()
            respuesta = input(
                "\nSelecciona una opción (A, B, C o D): "
            ).upper()
            while respuesta not in ["A", "B", "C", "D"]:
                respuesta = input(
                    "Opción inválida. Intenta nuevamente: "
                ).upper()
            if pregunta.verificar_respuesta(respuesta):
                print("\n✅ RESPUESTA CORRECTA")
                jugador.sumar_puntos()
            else:
                print("\n❌ RESPUESTA INCORRECTA")
                print("Respuesta correcta:",
                    pregunta.respuesta_correcta)
                jugador.perder_vida()
            time.sleep(1)
            if jugador.vidas == 0:
                print("\n" + jugador.nombre +
                    " ha perdido todas sus vidas.")
            print("\n-----------------------------------")
    limpiar()
    mostrar_titulo()
    print("\n=========== RESULTADOS FINALES ===========\n")
    for jugador in jugadores:
        print("Jugador:", jugador.nombre)
        print("Puntaje:", jugador.puntaje)
        print("Vidas restantes:", jugador.vidas)
        print("Aciertos:", jugador.aciertos)
        print("Errores:", jugador.errores)
        print("----------------------------------------")
    mostrar_ranking(jugadores)
    ganador = max(jugadores, key=lambda x: x.puntaje)
    print("\n🏆 EL GANADOR ES:", ganador.nombre)
    print("Puntaje final:", ganador.puntaje)
    guardar_puntajes(jugadores)
    pausa()
def menu_principal():
    opcion = 0
    while opcion != 4:
        limpiar()
        mostrar_titulo()
        print("\n1. Iniciar Juego")
        print("2. Ver Reglas")
        print("3. Ver Créditos")
        print("4. Salir")
        try:
            opcion = int(input("\nSelecciona una opción: "))
        except:
            opcion = 0
        if opcion == 1:
            iniciar_juego()
        elif opcion == 2:
            mostrar_reglas()
        elif opcion == 3:
            mostrar_creditos()
        elif opcion == 4:
            print("\nGracias por jugar.")
        else:
            print("\nOpción inválida.")
            time.sleep(1)
menu_principal()