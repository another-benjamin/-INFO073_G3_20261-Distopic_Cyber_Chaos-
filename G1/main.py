from const import *
from logic import cambiar_direccion, reiniciar, avanzar, avanzar_enemigos
from render import refrescar_tablero, mostrar_pantalla 
import pygame

def main():
    pygame.init()

    # Establecemos la resolución de la pantalla.
    screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

    # Establecemos el título de la ventana.
    pygame.display.set_caption("Juego Básico")
    
    fuente = pygame.font.Font(None, 36)

    running = True

    estado = ESTADO_INICIO
    tablero = []
    pos_jugador = (0, 0)
    pos_enemigos = []
    direccion = (0, 0)
    tiempo_ultimo_mov = 0
    tiempo_ultimo_mov_evil= 0
    pasos = 0
    llaves_comidas= 0 
    posiciones_cuerpo = [pos_jugador, direccion]

    mostrar_pantalla(screen, PANTALLA_INICIO)
    pygame.mixer.music.load ("g1/data/music/Gary VS David - Beloga.mp3")
    pygame.mixer.music.play ( -1)
    # Este es el bucle principal del juego, todo lo que sucede en el juego
    # está aquí.
    while running:
        # Se analizan los eventos del bucle actual.
        for evento in pygame.event.get():
            # Si es que se quiere cerrar la ventana.
            if evento.type == pygame.QUIT:
                running = False

            # Si es que se presiona alguna tecla.
            if evento.type == pygame.KEYDOWN:
                if estado == ESTADO_INICIO:
                    if evento.key == pygame.K_RETURN:
                        tablero, pos_jugador, pos_enemigos = reiniciar()
                        pasos= 0
                        direccion = (0, 0)
                        llaves_comidas=0
                        # Obtiene tiempo en milisegundos
                        tiempo_ultimo_mov = pygame.time.get_ticks()
                        estado = ESTADO_JUGANDO
                        refrescar_tablero(screen, tablero, fuente, posiciones_cuerpo)
                    elif evento.key == pygame.K_i:
                        estado = ESTADO_INSTRUCCIONES
                        mostrar_pantalla(screen, PANTALLA_INSTRUCCIONES)

                elif estado == ESTADO_INSTRUCCIONES:
                    estado = ESTADO_INICIO
                    mostrar_pantalla(screen, PANTALLA_INICIO)

                elif estado in (ESTADO_DERROTA, ESTADO_VICTORIA):
                    if evento.key == pygame.K_r:
                        tablero, pos_jugador, pos_enemigos = reiniciar()
                        pasos= 0
                        direccion = (0, 0)
                        llaves_comidas=0
                        tiempo_ultimo_mov = pygame.time.get_ticks()
                        estado = ESTADO_JUGANDO
                        refrescar_tablero(screen, tablero, fuente, posiciones_cuerpo)

                    if evento.key == pygame.K_ESCAPE:
                        estado = ESTADO_INICIO
                        mostrar_pantalla(screen, PANTALLA_INICIO)

                elif estado == ESTADO_JUGANDO:
                    direccion = cambiar_direccion(pygame.key.get_pressed(), direccion)

        if estado == ESTADO_JUGANDO:
            tiempo_actual = pygame.time.get_ticks()
        

            # La variable RETRASO hace que si no han pasado esa cantidad de ticks,
            # entonces no se avanzará en el tablero.
            if direccion != (0, 0) and tiempo_actual - tiempo_ultimo_mov >= RETRASO:
                resultado, pos_jugador, llaves_comidas = avanzar(tablero, pos_jugador, direccion, llaves_comidas)

                if resultado == "derrota":
                    estado = ESTADO_DERROTA
                    mostrar_pantalla(screen, PANTALLA_DERROTA)
                elif resultado == "victoria":
                    estado = ESTADO_VICTORIA
                    mostrar_pantalla(screen, PANTALLA_VICTORIA)
                else:
                    tiempo_ultimo_mov = tiempo_actual
                    pasos +=1
                    restantes = MAX_PASOS - pasos
                    pygame.display.set_caption(f"juego - pasos restantes: {restantes}")
                    if resultado == "regenerar":
                        pasos = 0
                        
                    if pasos >= MAX_PASOS:
                        estado = ESTADO_DERROTA
                        mostrar_pantalla(screen, PANTALLA_DERROTA)
                    else:
                        refrescar_tablero(screen, tablero, fuente, posiciones_cuerpo)
                if tiempo_actual - tiempo_ultimo_mov_evil >= RETRASO_ENEMIGOS:
                    resultado, pos_enemigos = avanzar_enemigos(tablero, pos_enemigos)

                    if resultado == "derrota":
                        estado = ESTADO_DERROTA
                        mostrar_pantalla(screen, PANTALLA_DERROTA)
                    else:
                        tiempo_ultimo_mov_evil = tiempo_actual
                        refrescar_tablero(screen,tablero, fuente, posiciones_cuerpo)
    pygame.quit()


if __name__ == "__main__":
    main()
