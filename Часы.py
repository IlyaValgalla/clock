import pygame
import time
from datetime import datetime

# Инициализация Pygame
pygame.init()

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Размеры экрана
WIDTH = 800
HEIGHT = 300

# Размеры сегментов
SEGMENT_LENGTH = 50
SEGMENT_WIDTH = 10

# Настройка экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Цифровые часы")

# Функция для рисования сегмента
def draw_segment(pos, orientation):
    if orientation == 'H':  # Горизонтальный
        pygame.draw.rect(screen, RED, [pos[0], pos[1], SEGMENT_LENGTH, SEGMENT_WIDTH])
    else:  # Вертикальный
        pygame.draw.rect(screen, RED, [pos[0], pos[1], SEGMENT_WIDTH, SEGMENT_LENGTH])

# Функция для отображения цифры
def display_digit(pos, digit):
    # Конфигурация сегментов для каждой цифры
    segments = [
        [1, 1, 1, 1, 1, 1, 0],  # 0
        [0, 1, 1, 0, 0, 0, 0],  # 1
        [1, 1, 0, 1, 1, 0, 1],  # 2
        [1, 1, 1, 1, 0, 0, 1],  # 3
        [0, 1, 1, 0, 0, 1, 1],  # 4
        [1, 0, 1, 1, 0, 1, 1],  # 5
        [1, 0, 1, 1, 1, 1, 1],  # 6
        [1, 1, 1, 0, 0, 0, 0],  # 7
        [1, 1, 1, 1, 1, 1, 1],  # 8
        [1, 1, 1, 0, 0, 1, 1]   # 9
    ]
    
    # Позиции сегментов
    segment_positions = [
        ((pos[0] + SEGMENT_WIDTH, pos[1]), 'H'),
        ((pos[0] + SEGMENT_LENGTH + SEGMENT_WIDTH, pos[1] + SEGMENT_WIDTH), 'V'),
        ((pos[0] + SEGMENT_LENGTH + SEGMENT_WIDTH, pos[1] + SEGMENT_WIDTH + SEGMENT_LENGTH), 'V'),
        ((pos[0] + SEGMENT_WIDTH, pos[1] + 2 * SEGMENT_LENGTH), 'H'),
        ((pos[0], pos[1] + SEGMENT_WIDTH + SEGMENT_LENGTH), 'V'),
        ((pos[0], pos[1] + SEGMENT_WIDTH), 'V'),
        ((pos[0] + SEGMENT_WIDTH, pos[1] + SEGMENT_LENGTH), 'H')
    ]
    
    # Отрисовка сегментов для заданной цифры
    for i, segment in enumerate(segments[digit]):
        if segment:
            draw_segment(segment_positions[i][0], segment_positions[i][1])

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Отрисовка фона
    screen.fill(BLACK)

    # Получение текущего времени
    now = datetime.now()
    hours, minutes, seconds = now.hour, now.minute, now.second

    # Отображение времени
    display_digit((50, 50), hours // 10)
    display_digit((150, 50), hours % 10)
    display_digit((300, 50), minutes // 10)
    display_digit((400, 50), minutes % 10)
    display_digit((550, 50), seconds // 10)
    display_digit((650, 50), seconds % 10)

    # Обновление экрана
    pygame.display.flip()

    # Частота обновления экрана
    time.sleep(1)

pygame.quit()
