import pygame

# Inicialización de Pygame
pygame.init()

# Dimensiones de la ventana del juego
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Colores
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Crear la ventana del juego
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Ejemplo de Colisión")

# Rectángulos de los objetos
rect1 = pygame.Rect(100, 100, 50, 50)
rect2 = pygame.Rect(200, 100, 50, 50)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar la posición de los rectángulos
    rect1.x += 1

    # Comprobar colisión entre los rectángulos
    if rect1.colliderect(rect2):
        print("¡Colisión!")

    # Limpiar la ventana
    window.fill(BLACK)

    # Dibujar los rectángulos
    pygame.draw.rect(window, RED, rect1)
    pygame.draw.rect(window, RED, rect2)

    # Actualizar la ventana
    pygame.display.update()

# Finalizar Pygame
pygame.quit()
