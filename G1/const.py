import os

# Estados del juego
ESTADO_INICIO = "inicio"
ESTADO_INSTRUCCIONES = "instrucciones"
ESTADO_JUGANDO = "jugando"
ESTADO_DERROTA = "derrota"
ESTADO_VICTORIA = "victoria"
MAX_PASOS = 50 
CANT_OBSTACULOS = 10
CANT_BATERIAS= 1
CANT_LLAVES= 1
LLAVES_PARA_GANAR= 3
# Rutas a la carpeta de imágenes de pantallas
DIR_PANTALLAS = os.path.join(os.path.dirname(__file__), "data", "pantallas")
DIR_SPRITES = os.path.join(os.path.dirname(__file__), "data", "sprites")

# Se específica el nombre del archivo para cada imagen de pantalla.
# El formato de imagen utilizado puede ser PNG, JPG/JPEG, BMP, o GIF.
PANTALLA_INICIO = "pantalla_inicio.bmp"
PANTALLA_INSTRUCCIONES = "pantalla_instrucciones.bmp"
PANTALLA_VICTORIA = "pantalla_victoria.bmp"
PANTALLA_DERROTA = "pantalla_derrota.bmp"

BATERIA_SPRITE = "Bateria.png"
LLAVES_SPRITE = "Llaves.png"
ENEMIGO_SPRITE = "ENEMIGO_SPRITE.png"
OBSTACULO_SPRITE = "obstaculo.png"
Jugador_spriteF = "cyborg_front.png"
FLOOR = "baldosa.png"
#tamaño pantalla
ANCHO_VENTANA = 1200
ALTO_VENTANA = 800
LADO_TABLERO = 800
ANCHO_PANEL = ANCHO_VENTANA - LADO_TABLERO

# Para evitar que el jugador se mueva demasiado rápido
RETRASO = 200

# Códigos de cada elemento del tablero
VACIO = 0
OBSTACULO = 1
JUGADOR = 2
BATERIA = 3
LLAVE = 4
ENEMIGO = 5

CANT_ENEMIGOS = 2
RETRASO_ENEMIGOS= 300
# Tamaño del tablero
# Si se cambian estas constantes, se debe modificar la definición
# del tablero que se encuentra en función reiniciar().
FILAS = 15
COLUMNAS = 15
BORDE = (
[( c , 0) for c in range ( COLUMNAS ) ]
+ [( c , FILAS - 1) for c in range ( COLUMNAS ) ]
+ [(0 , f ) for f in range (1 , FILAS - 1) ]
+ [( COLUMNAS - 1 , f ) for f in range (1 , FILAS - 1) ]
)