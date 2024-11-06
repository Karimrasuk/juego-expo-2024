import pygame
import random
import sys
import math

# Inicializa Pygame
pygame.init()

# Dimensiones de la ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ruleta")

# Colores
GREEN = (0, 128, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Fuente
font = pygame.font.SysFont("Arial", 36)

# Datos de la ruleta
NUMBERS = list(range(0, 37))
RED_NUMBERS = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
BLACK_NUMBERS = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

def draw_wheel(angle):
    """Dibuja la rueda de la ruleta."""
    pygame.draw.circle(screen, GREEN, (WIDTH // 2, HEIGHT // 2), 250)

    for i, number in enumerate(NUMBERS):
        number_angle = math.radians(i * (360 / len(NUMBERS)) - angle)
        x = WIDTH // 2 + int(220 * math.cos(number_angle))
        y = HEIGHT // 2 + int(220 * math.sin(number_angle))
        color = RED if number in RED_NUMBERS else BLACK
        text = font.render(str(number), True, WHITE)
        screen.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))

def main():
    clock = pygame.time.Clock()
    running = True
    spinning = False
    angle = 0
    result = None

    while running:
        screen.fill(BLACK)

        if spinning:
            angle += 10  # Velocidad de la ruleta
            if angle >= 360:
                angle -= 360
            
            if angle % 360 == 0:
                result = random.choice(NUMBERS)
                spinning = False
        else:
            draw_wheel(angle)

        # Mostrar resultado
        if result is not None:
            
