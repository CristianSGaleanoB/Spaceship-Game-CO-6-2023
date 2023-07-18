import pygame
import math

pygame.init()

# Definir los colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Definir las dimensiones de la pantalla
ANCHO = 800
ALTO = 600

# Crear la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Movimiento circular")

# Definir las coordenadas y el radio del círculo
center_x = ANCHO // 2
center_y = ALTO // 2
radius = 100

# Definir la velocidad y el ángulo de movimiento
speed = 2
angle = 0

# Bucle principal del juego
jugando = True
clock = pygame.time.Clock()
while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    # Limpiar la pantalla
    pantalla.fill(BLANCO)

    # Calcular las coordenadas del objeto en función del ángulo y el radio
    objeto_x = center_x + int(math.cos(math.radians(angle)) * radius)
    objeto_y = center_y + int(math.sin(math.radians(angle)) * radius)


    # Dibujar el objeto en las coordenadas (objeto_x, objeto_y)
    objeto_rect = pygame.Rect(objeto_x - 10, objeto_y - 10, 20, 20)
    pygame.draw.rect(pantalla, NEGRO, objeto_rect)

    # Actualizar el ángulo de movimiento
    angle += speed

    # Actualizar la pantalla
    pygame.display.flip()
    clock.tick(60)  # Limitar la velocidad de fotogramas a 60 FPS

# Salir del juego
pygame.quit()
