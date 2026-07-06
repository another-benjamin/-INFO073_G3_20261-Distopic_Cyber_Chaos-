import os
import pygame
from const import LADO_TABLERO, ANCHO_PANEL, ALTO_VENTANA, FILAS, COLUMNAS, OBSTACULO, JUGADOR, BATERIA, LLAVE, ENEMIGO, DIR_PANTALLAS, LLAVES_PARA_GANAR, DIR_SPRITES, BATERIA_SPRITE, LLAVES_SPRITE, ENEMIGO_SPRITE, Jugador_spriteF, FLOOR, OBSTACULO_SPRITE


def dibujar_panel(screen, fuente, llaves):
    panel = pygame.Rect(LADO_TABLERO, 0, ANCHO_PANEL, ALTO_VENTANA)
    pygame.draw.rect(screen, "gray15", panel)
    
    x = LADO_TABLERO + 24
    
    titulo = fuente.render("Cyborg", True, "orange")
    screen.blit(titulo, (x, 30))
    
    largo_txt = fuente.render(f"Llaves: {llaves}", True, "white")
    screen.blit(largo_txt, (x, 100))
    
    meta_txt = fuente.render(f"Llaves para ganar: {LLAVES_PARA_GANAR}", True, "yellow")
    screen.blit(meta_txt, (x, 140))







def refrescar_tablero(screen, tablero, fuente, llaves):
    
    # Rellena la pantalla con el color gris, básicamente pintando
    # por encima de lo que estaba anteriormente.
    
    ruta_bateria = os.path.join(DIR_SPRITES, BATERIA_SPRITE)
    bateria_imagen = pygame.image.load(ruta_bateria)
    ruta_llaves = os.path.join(DIR_SPRITES, LLAVES_SPRITE)
    llaves_imagen = pygame.image.load(ruta_llaves)
    ruta_enemigo = os.path.join(DIR_SPRITES, ENEMIGO_SPRITE)
    enemigo_imagen = pygame.image.load(ruta_enemigo)
    ruta_jugador_frente = os.path.join(DIR_SPRITES, Jugador_spriteF)
    jugador_imagen = pygame.image.load(ruta_jugador_frente)
    ruta_baldosa = os.path.join(DIR_SPRITES, FLOOR)
    baldosa = pygame.image.load(ruta_baldosa)
    ruta_obstaculo = os.path.join(DIR_SPRITES,OBSTACULO_SPRITE )
    obstaculo_imagen = pygame.image.load(ruta_obstaculo)
    screen.fill((80, 115, 115))


    # Podemos calcular el tamaño en pixeles que tendrá cada
    # casilla al dividir tanto la altura de la pantalla (screen.get_height())
    # como el ancho (screen.get_width()) por la cantidad de filas y columnas respectivamente.
    # Por ejemplo en este caso alto_elem sería 800 / 15 = 53.3, lo que nos indica que la
    # altura de cada elemento es de 53.3 píxeles.
    alto_elem = LADO_TABLERO / FILAS
    ancho_elem = LADO_TABLERO / COLUMNAS
    
    
    
    # Como el jugador es un círculo, se necesita el radio.
    radio = ancho_elem / 2


    # Posición en eje "y" en unidad de píxeles.
    pos_y = 0
    for i in range(FILAS):
        # Posición en eje "x" en unidad de píxeles.
        pos_x = 0
        for j in range(COLUMNAS):
            pos_x= j * ancho_elem
            pos_y= i * alto_elem
            screen.blit(baldosa,[pos_x,pos_y])
    pos_y = 0
    for i in range(FILAS):
        # Posición en eje "x" en unidad de píxeles.
        pos_x = 0
        for j in range(COLUMNAS):
            if tablero[i][j] == OBSTACULO:
                # Dibuja un rectángulo en la posición (pos_x, pos_y) y que sea
                # de tamaño (ancho_elem, alto_elem) y color negro.
                screen.blit(obstaculo_imagen,(pos_x,pos_y)
                )
            elif tablero[i][j] == JUGADOR:
                # Dibujamos un círculo verde en la posición (pos_x + radio, pos_y + radio),
                # con un radio definido por la variable "radio" (ancho_elem / 2).
                screen.blit(jugador_imagen,(pos_x,pos_y)
                )
            elif tablero[i][j] == BATERIA:
                screen.blit(bateria_imagen,(pos_x, pos_y))
            
            elif tablero[i][j] == LLAVE:
                screen.blit(llaves_imagen,(pos_x, pos_y))

            elif tablero[i][j] == ENEMIGO:
                screen.blit(enemigo_imagen,(pos_x,pos_y))
            # Estamos recorriendo los píxeles de la pantalla, por lo que
            # debemos sumar el ancho y altura en pixeles de cada elemento que
            # ya hayamos recorrido para avanzar al siguiente.
            pos_x += ancho_elem
        pos_y += alto_elem
    dibujar_panel(screen, fuente, llaves)
    # Refresca el contenido que se ve en pantalla.
    pygame.display.flip() 
    

    
def mostrar_pantalla(screen, nombre_archivo):


    ruta = os.path.join(DIR_PANTALLAS, nombre_archivo)

    try:
        imagen = pygame.image.load(ruta)
        imagen = pygame.transform.scale(imagen, screen.get_size())

        # Dibujamos la imagen en la pantalla en la coordenada (0, 0).
        screen.blit(imagen, (0, 0))

        # Refrescamos pantalla.
        pygame.display.flip()
    except FileNotFoundError:
        # Fallback de seguridad en caso de que las imágenes no existan aún
        screen.fill("black")
        pygame.display.flip()
        print(f"Advertencia: No se encontró la imagen {ruta}") 