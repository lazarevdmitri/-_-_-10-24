
import pygame
from pygame.draw import *
from random import randint

pygame.init()
pygame.font.init()

FPS = 60
TIME_LIFE = 1000
last_time = pygame.time.get_ticks()
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 750

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

points = 0
points_font = pygame.font.SysFont('Comic Sans MS', 30)

MAX_BALLS = 5
BALL_SPEED_MIN = -3
BALL_SPEED_MAX = 3

BORDER_LEFT = SCREEN_WIDTH // 4
BORDER_RIGHT = SCREEN_WIDTH // 1.5
BORDER_TOP = 0
BORDER_BOTTOM = SCREEN_HEIGHT

balls_x = []
balls_y = []
balls_x_speed = []
balls_y_speed = []
balls_r = []
balls_color = []


def new_ball(coords_x, coords_y, radius):
    '''
    Создает и возвращает параметры нового шар на экране
    в случайных координатах и случайного цвета.
    coords_x - кортеж из координат начала и конца по оси Х,
    coords_y - кортеж из координат начала и конца по оси Y,
    radius - кортеж из диапазона радиусов.
    '''
    x_start, x_end = coords_x
    y_start, y_end = coords_y
    r_start, r_end = radius

    r = randint(r_start, r_end)
    x = randint(x_start + r, x_end - r)
    y = randint(y_start + r, y_end - r)

    color = COLORS[randint(0, 5)]

    speed_x = randint(BALL_SPEED_MIN, BALL_SPEED_MAX) / 5
    speed_y = randint(BALL_SPEED_MIN, BALL_SPEED_MAX) / 5

    return color, x, y, r, speed_x, speed_y


def click(event):
    '''
    Функция обработки нажатия мыши.
    Проверяет, находятся ли координаты мыши в каком-либо круге,
    если да, то начисляется 1 очко
    '''
    global points
    mouse_x = event.pos[0]
    mouse_y = event.pos[1]
    for i in range(MAX_BALLS):
        # Вычисляем расстояние между центром круга и координатами мыши
        evklid_r = ((balls_x[i] - mouse_x)  2 +
                                            (balls_y[i] - mouse_y)
        2) ** 0.5
        # Если расстояние меньше радиуса круга, значит мы попали в круг
        if evklid_r <= balls_r[i]:
            points += 1


