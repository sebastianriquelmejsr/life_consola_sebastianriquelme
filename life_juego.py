from funciones_life import * 
    
iniciar_juego = True

while iniciar_juego:
    opcion = mostrar_menu()
    match opcion:
        case 1:
            empezar_juego()
        case 2:
            mostrar_score()
        case 3:
            print(f"Adios!")
            iniciar_juego = False    
