import random
import pygame

from const import FILAS, COLUMNAS, VACIO, BORDE, JUGADOR, ENEMIGO, CANT_ENEMIGOS, LLAVE, CANT_BATERIAS, OBSTACULO, CANT_OBSTACULOS, BATERIA, LLAVES_PARA_GANAR, CANT_LLAVES




def aparecer_aleatorio(tablero, id_elem, incluir_borde=True):
    vacios = []

    for fila in range(FILAS):
        for columna in range(COLUMNAS):
                if tablero[fila][columna] == VACIO:
                    vacios.append(( columna , fila ))
    if not incluir_borde:
            vacios = [pos for pos in vacios if pos not in BORDE]
    if len(vacios) == 0:
        return -1, -1
    
    columna, fila = random.choice(vacios)
    tablero[fila][columna]= id_elem
    return columna, fila 





def cambiar_direccion(keys, direccion_actual):
    if keys[pygame.K_w]:
        return (0, -1)

    if keys[pygame.K_s]:
        return (0, 1)

    if keys[pygame.K_a]:
        return (-1, 0)

    if keys[pygame.K_d]:
        return (1, 0)

    return direccion_actual





def avanzar(tablero, pos_jugador, direccion, llaves_comidas):
    # Obtenemos los componentes "x" e "y" de cada tupla recibida
    # con información de la dirección y posición del jugador.
    dir_col, dir_fila = direccion
    ind_actual_col, ind_actual_fila = (
        pos_jugador  # Tupla (columna, fila) que representa los índices en el tablero.
    )


    # Aplicamos la dirección a la posición del jugador.
    ind_nueva_col = ind_actual_col + dir_col
    ind_nueva_fila = ind_actual_fila + dir_fila


    # Verificamos que no haya choque con el borde del tablero.
    if not (0 <= ind_nueva_col < COLUMNAS and 0 <= ind_nueva_fila < FILAS):
        return "derrota", pos_jugador, llaves_comidas



    # Obtenemos el elemento que se encuentre en el tablero en la nueva posición del jugador.
    pos_elem = tablero[ind_nueva_fila][ind_nueva_col]




    if pos_elem == OBSTACULO or pos_elem == ENEMIGO:
        return "derrota", pos_jugador, llaves_comidas

    if pos_elem == BATERIA:
        tablero[ind_actual_fila][ind_actual_col] = VACIO
        tablero[ind_nueva_fila][ind_nueva_col] = JUGADOR
        aparecer_aleatorio(tablero, BATERIA)
        return "regenerar", (ind_nueva_col, ind_nueva_fila), llaves_comidas

    if pos_elem == LLAVE:
        llaves_comidas += 1
        tablero [ ind_actual_fila ][ ind_actual_col ] = VACIO
        tablero [ ind_nueva_fila][ind_nueva_col]=JUGADOR
        aparecer_aleatorio(tablero, LLAVE)
        if llaves_comidas == LLAVES_PARA_GANAR :
            return "victoria", ( ind_nueva_col , ind_nueva_fila ) ,llaves_comidas
        return "ok", ( ind_nueva_col , ind_nueva_fila ) , llaves_comidas


    # Movimiento normal, si es que no encontramos manzana ni obstáculo.
    tablero[ind_actual_fila][ind_actual_col] = VACIO
    tablero[ind_nueva_fila][ind_nueva_col] = JUGADOR



    return "ok", (ind_nueva_col, ind_nueva_fila), llaves_comidas 




def poblar_tablero(tablero):
    
    for i in range(CANT_OBSTACULOS):
        aparecer_aleatorio(tablero, OBSTACULO, incluir_borde = False)
    for i in range(CANT_BATERIAS):
        aparecer_aleatorio(tablero, BATERIA, incluir_borde = False)
    for i in range(CANT_LLAVES):
        aparecer_aleatorio(tablero, LLAVE,incluir_borde=False)






def reiniciar():

    # Si se modifica constante FILAS o COLUMNAS al inicio, también
    # se debe modificar este arreglo de tablero con los valores correspondientes.
    # Esto puede ser mejorado usando dos bucles "for" anidados o comprensión de listas.
    tablero = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]


    poblar_tablero(tablero)

    # Colocamos al jugador en una posición aleatoria.
    pos_jugador = aparecer_aleatorio(tablero, JUGADOR)
    pos_enemigos = []

    for _ in range(CANT_ENEMIGOS):
        pos_enemigos.append(aparecer_aleatorio(tablero,ENEMIGO))
    return tablero, pos_jugador, pos_enemigos


def obtener_direccion_aleatoria():
    return random.choice([(0,-1),(0,1),(-1,0),(1,0)])


def avanzar_enemigos(tablero, pos_enemigos, pos_jugador):
    # Extraemos las coordenadas del jugador
    col_jugador, fil_jugador = pos_jugador
    
    for i in range(len(pos_enemigos)):
        col, fil = pos_enemigos[i]

        # 1. Determinar las direcciones ideales para acercarse al jugador
        posibles_direcciones = []
        
        # Eje X (Columnas)
        if col_jugador > col:
            posibles_direcciones.append((1, 0))  # Mover a la Derecha
        elif col_jugador < col:
            posibles_direcciones.append((-1, 0)) # Mover a la Izquierda
            
        # Eje Y (Filas)
        if fil_jugador > fil:
            posibles_direcciones.append((0, 1))  # Mover Abajo
        elif fil_jugador < fil:
            posibles_direcciones.append((0, -1)) # Mover Arriba

        # Mezclamos las opciones un poco para que no siempre prioricen el mismo eje
        # Esto hace que el movimiento se vea más natural
        random.shuffle(posibles_direcciones)

        # 2. Elegir la primera dirección válida
        dir_col, dir_fil = 0, 0
        movimiento_exitoso = False
        
        # Intentar avanzar en las direcciones que lo acercan al jugador
        for d_col, d_fil in posibles_direcciones:
            nuevacol = col + d_col
            nuevafil = fil + d_fil
            
            # Verificar si el camino está dentro del mapa
            if 0 <= nuevacol < COLUMNAS and 0 <= nuevafil < FILAS:
                # Si la casilla está vacía O es el jugador, es un buen camino
                if tablero[nuevafil][nuevacol] in (VACIO, JUGADOR):
                    dir_col, dir_fil = d_col, d_fil
                    movimiento_exitoso = True
                    break # Encontramos ruta, dejamos de buscar

        # 3. Plan B: Si no puede avanzar hacia el jugador (está bloqueado por una pared/obstáculo)
        if not movimiento_exitoso:
            dir_col, dir_fil = obtener_direccion_aleatoria()
        
        # 4. Aplicar el movimiento final
        nuevacol = col + dir_col
        nuevafil = fil + dir_fil
        
        if 0 <= nuevacol < COLUMNAS and 0 <= nuevafil < FILAS:
            if tablero[nuevafil][nuevacol] == VACIO:
                tablero[fil][col] = VACIO
                tablero[nuevafil][nuevacol] = ENEMIGO
                pos_enemigos[i] = (nuevacol, nuevafil)
            elif tablero[nuevafil][nuevacol] == JUGADOR:
                return "derrota", pos_enemigos
                
    return "ok", pos_enemigos


