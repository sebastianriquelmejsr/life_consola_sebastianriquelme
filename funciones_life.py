import random
import copy
from preguntas import * 
from tablero_life import *


def dar_bienvenida()->str:
    print ("L I F E")
    nombre_jugador = input ("Ingrese su nombre: ")
    print(F"Bienvenido {nombre_jugador} al Juego de la vida!")
    return nombre_jugador

def mostrar_menu()->int:
    print("""||| MENU PRINCIPAL |||
1 - JUGAR
2 - PUNTAJES
3 - SALIR""")
    validar = True
    while validar:
        try:
            opcion = validar_entrada(int(input("Por favor, seleccione una opcion: ")),1,3,"Seleccione una opcion valida (1 | 2 | 3): ")
            validar = False                     
        except:
            print ("Opcion incorrecta, ingrese un dato valido")                                                                   
    return opcion  

def empezar_juego():
    nombre_jugador = dar_bienvenida()
    puntos = 15000
    posicion = 0
    copia_preguntas = copy.deepcopy(preguntas)
    jugar = True
    while jugar:
        posicion = lanzar_dado(nombre_jugador, puntos, posicion, tablero)
        puntos = sumar_restar_puntos(posicion, tablero, puntos)
        puntos = mostrar_trivia(posicion, tablero, puntos, copia_preguntas)
        jugar = comprobar_estado(nombre_jugador, posicion, puntos, tablero)
 
def cambiar_minus(text:str)->str:                                                   
    minuscula = ""                                                                  
    for letra in text:                                                              
        valor_ascii = ord(letra)                                                    
        if valor_ascii >= 65 and valor_ascii <= 90:    
            minuscula += chr(valor_ascii + 32)                                      
        else:
            minuscula += letra                                                      
    return minuscula 

def validar_entrada(entrada:int, minimo:int, maximo:int, mensaje:str)->int:  
    while entrada < minimo or entrada > maximo:
        entrada = int (input(f"Error, {mensaje}"))
    return entrada


def validar_respuesta(ingreso:str, resp1:str, resp2:str, resp3:str, mensaje:str)->str: 
    ingreso = cambiar_minus(ingreso)
    while ingreso != resp1 and ingreso != resp2 and ingreso != resp3:
        ingreso = cambiar_minus(input(f"Error, {mensaje}"))
    return ingreso 

def lanzar_dado(jugador:str, puntos:int, posicion:int,tablero:list)->int:
    print (f"{jugador}, tu punto de partida es: {posicion} y tus puntos {puntos}")  
    dado = input("Pulse la tecla ENTER para lanzar el dado ")                     
    dado = random.randint(1,6)
    print (f"Usted avanza {dado} casilleros!")
    posicion += dado
    if posicion >= len(tablero):
        posicion = len(tablero)
    return posicion

def sumar_restar_puntos(posicion:int,tablero:list, puntos:int)->int:
    if  tablero[posicion - 1] == -1:
        print("Perdiste 3000 puntos!")
        puntos -= 3000
    elif tablero[posicion - 1] == 1:
        print("Ganaste 3000 puntos!")
        puntos += 3000
    return puntos

def mostrar_trivia(posicion:int,tablero:list, puntos:int, copia_preguntas:list)->int:
        if  tablero[posicion - 1] == 0:
            print("Responda trivia!")          
            pregunta_usuario = random.choice(copia_preguntas)
            copia_preguntas.remove(pregunta_usuario)
            print (f"{pregunta_usuario["pregunta"]}")
            print (f"a) {pregunta_usuario["respuesta_a"]}")
            print (f"b) {pregunta_usuario["respuesta_b"]}")
            print (f"c) {pregunta_usuario["respuesta_c"]}")
            respuesta = validar_respuesta(input("Ingrese la respuesta(a|b|c): "), "a", "b", "c", "ingrese una respueta valida(a|b|c): ")
            if respuesta == pregunta_usuario["respuesta_correcta"]:
                print("Respuesta correcta!! ganaste 3000 puntos")
                puntos += 3000
            else:
                print("Respuesta incorrecta. Perdes 3000 puntos")
                puntos -= 3000      
        return puntos

def comprobar_estado(jugador:str, posicion:int, puntos: int, tablero:list)->bool:
    iniciar_juego = True
    if posicion >= len(tablero):                                        
        print(f"Llego a la meta, felicidades {jugador}!!")
        print(f"Tu puntaje fue: {puntos}")
        anotar_jugador(cambiar_minus(jugador),puntos)
        iniciar_juego = False    
    elif puntos <= 0:
        print ("Te quedaste sin puntos, el juego termino")
        iniciar_juego = False
    return iniciar_juego

def anotar_jugador(jugador:str, puntaje:int):
    with open("score.csv", "a") as archivo:
        archivo.write(f"{jugador},{puntaje}\n")

def leer_score()->list:
    lista = []
    try:
        with open("score.csv", "r") as archivo:
            for linea in archivo:
                jugador_ganador = linea.split(",")
                lista.append(jugador_ganador)
    except FileNotFoundError:
        print("No se encontro el archivo ")
    return lista

def ordenar_nombres(lista_jugadores)->list:
    for i in range(len(lista_jugadores) -1):
        for j in range(i + 1, len(lista_jugadores)):
            if lista_jugadores[i][0] > lista_jugadores[j][0]:
                aux = lista_jugadores[i]
                lista_jugadores[i] = lista_jugadores[j]
                lista_jugadores[j] = aux
    return lista_jugadores

def mostrar_score():
    score = leer_score()
    score = ordenar_nombres(score)
    print("Ganadores")              
    for nombre, puntaje in score:
        print(f"Jugador: {nombre} | Puntos: {puntaje}")   
     




