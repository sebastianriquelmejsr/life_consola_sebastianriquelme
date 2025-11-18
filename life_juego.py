from preguntas import * 
from tablero_life import *
from funciones_life import * 
import copy

copia_preguntas = copy.deepcopy(preguntas)

nombre_jugador = dar_bienvenida()
opcion = mostrar_menu()
    
puntos = 15000
posicion = 0
iniciar_juego = True

while iniciar_juego:
    match opcion:
        case 1:
            posicion = lanzar_dado(nombre_jugador, puntos, posicion, tablero)
            puntos = sumar_restar_puntos(posicion, tablero, puntos)
            puntos = mostrar_trivia(posicion, tablero, puntos, copia_preguntas)
            iniciar_juego = comprobar_estado(nombre_jugador, posicion, puntos, tablero)
        case 2:
            mostrar_score()
            iniciar_juego = False
        case 3:
            print(f"Adios {nombre_jugador} !")
            iniciar_juego = False    
