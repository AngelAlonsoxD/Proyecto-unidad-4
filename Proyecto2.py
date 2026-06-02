# ============================================================
# PROYECTO - JUEGO DE TRIVIA
# Fundamentos de proramacion
# Nombre: Angel Roberto Alonso Guerrero 
#Fecha: 05 de junio del 2026
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