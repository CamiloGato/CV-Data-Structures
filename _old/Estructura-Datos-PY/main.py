import pygame
import sys
import random
import tkinter as tk
from tkinter import messagebox
from pygame.locals import *
from pygame.math import Vector2

"""----Creacion de la clase comida----"""


class Comida:
    def __init__(self) -> None:
        self.inico()  # posicion inicial de la manzana

    def draw_comida(self, win):
        comida_rect = pygame.Rect(self.pos.x * TAMANO_CAJA, self.pos.y * TAMANO_CAJA, TAMANO_CAJA, TAMANO_CAJA)
        # creacion de los rectangulos como comida

        pygame.draw.rect(win, self.color, comida_rect)  # dibuja la comida

    def nueva_posicion(self):  # coordenadas de la siguiente manzana
        self.x = random.randint(0, NUM_CAJA - 1)
        self.y = random.randint(0, NUM_CAJA - 1)
        self.pos = Vector2(self.x, self.y)
        self.color = ROJO

    def inico(self):  # posicion de la manzana inicial
        self.pos = Vector2(8, 4)
        self.color = ROJO


"""---- Creacion de la clase Snake ----"""


class Snake:
    def __init__(self) -> None:
        self.body = [Vector2(6, 6), Vector2(6, 7),
                     Vector2(6, 8)]  # coordenadas iniciales para el cuerpo de la serpiente
        self.direction = Vector2(0, -1)  # direccion inicial de la serpiente
        self.snack = False

    def draw_snake(self, win):  # Dibuja la serpiente
        for i, block in enumerate(self.body):  # a cada vector de la serpiente le da un indice, para darle los colores
            if i == 0:
                color = GRIS  # la cabeza de color gris

            else:
                color = BLANCO  # el cuerpo blanco

            block_rect = pygame.Rect(block.x * TAMANO_CAJA, block.y * TAMANO_CAJA, TAMANO_CAJA, TAMANO_CAJA)
            # crea los rectangulos de la cabeza y el cuerpo de la serpiente

            pygame.draw.rect(win, color, block_rect)  # dibuja la serpiente

    def move_snake(self):  # movimiento de la serpiente
        if not self.snack:
            body_copia = self.body[:-1]  # crea una copia del cuerpo sin la cola
            body_copia.insert(0, body_copia[
                0] + self.direction)  # inserta en el primer indice de la copia , el primer indice mas la direccion
            self.body = body_copia  # actualize la copia del cuerpo como la nueva serpiente

        else:
            body_copia = self.body[:]  # crea una copia del cuerpo
            body_copia.insert(0, body_copia[
                0] + self.direction)  # inserta en el primer indice de la copia , el primer indice mas la direccion
            self.body = body_copia  # actuliza la copia del cuerpo como la nueva serpiente
            self.snack = False  # actualiza el atributo para que el cuerpo siga la cabeza

    def comer_snack(self):
        self.snack = True


"""---- Creacion clase game ----"""


class Game:
    def __init__(self) -> None:
        self.snake = Snake()  # crea un atributo como un objeto Snake
        self.comida = Comida()  # crea un atributo como un objeto comida

    def draw_elementos(self, win):
        self.draw_grid()  # dibuja la cuadricula
        self.snake.draw_snake(win)  # dibuja la serpiente
        if self.comida.pos in self.snake.body:
            """ Condiciona la posicion en la cual aparecera la comida"""
            self.comida.nueva_posicion()  # hace que busque otra posicion
        else:
            self.comida.draw_comida(win)  # dibuja la comida

    def update(self):  # actualiza lo que aparece en pantalla
        self.snake.move_snake()
        self.comida_snack()
        self.check_collision()

    def comida_snack(self):

        # si la cabeza de la serpiente es igual a la posicion de la manzana ejectuta los metodos

        if self.comida.pos == self.snake.body[0]:
            self.snake.comer_snack()
            self.comida.nueva_posicion()  # genera una nueva manzana

    def check_collision(self):
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:  # si la cabeza esta en la misma posicion del cuerpo
                self.game_over()  # se acaba el juego
        # la cabeza no puede estar por fuera de la cuadricula por la izquierda o por la derecha en ambas coordenas

        if not -1 <= self.snake.body[0].x <= NUM_CAJA or not -1 <= self.snake.body[0].y <= NUM_CAJA:
            self.game_over()

    def game_over(self):
        self.message_box("Perdiste", f"Obtuviste {len(self.snake.body) - 3} Intentalo de nuevo!")
        # notifica que a perdido el juego y cuanto puntaje obtuvo
        self.snake.body = [Vector2(6, 6), Vector2(6, 7), Vector2(6, 8)]  # cada que pierde vuelve a esta posicion
        self.snake.direction = Vector2(0, -1)  # inicia con esta direccion
        self.comida.inico()  # reinicia la manzana a la primera posicion

    @staticmethod  # crea la funcion para la cuadricula
    def draw_grid():
        for x in range(NUM_CAJA):
            for y in range(NUM_CAJA):
                grid_rect = pygame.Rect(x * TAMANO_CAJA, y * TAMANO_CAJA, TAMANO_CAJA, TAMANO_CAJA)
                pygame.draw.rect(pantalla, GRIS, grid_rect, 1)

    @staticmethod  # crea la funcion para que muestr el puntaje y que a perdido
    def message_box(subject, message):
        root = tk.Tk()
        root.attributes("-topmost", True)
        root.withdraw()
        messagebox.showinfo(subject, message)
        root.destroy()


pygame.init()  # inicializa los modulos
TAMANO_CAJA, NUM_CAJA = 60, 13  # tamaño pixeles y cuantas cudriculas va a dibujar
ANCHO = TAMANO_CAJA * NUM_CAJA
pantalla = pygame.display.set_mode((ANCHO, ANCHO))  # dibuja el fondo de la pantalla
pygame.display.set_caption("Snake")  # da el titulo del juego
clock = pygame.time.Clock()  # hace que la serpiente avance sin darle movimiento

ROJO = (255, 0, 0)
BLANCO = (255, 255, 255)
GRIS = (128, 128, 128)
NEGRO = (0, 0, 0)

game = Game()  # instancia la clase juego

while True:  # ciclo que controla el juego
    clock.tick(7)  # controla la velocidad el juego
    for event in pygame.event.get():  # itera los tipos de eventos
        if event.type == QUIT:  # verifica cuando el usuario sale del juego
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:  # verifica cuando el usuario usas las teclas
            if event.key == K_w:
                if game.snake.direction.y != 1:
                    game.snake.direction = Vector2(0, -1)

            if event.key == K_s:
                if game.snake.direction.y != -1:
                    game.snake.direction = Vector2(0, 1)

            if event.key == K_a:
                if game.snake.direction.x != 1:
                    game.snake.direction = Vector2(-1, 0)

            if event.key == K_d:
                if game.snake.direction.x != -1:
                    game.snake.direction = Vector2(1, 0)

    pantalla.fill(NEGRO)  # relleña el fondo de pantalla de negro
    game.draw_elementos(pantalla)  # dibuja los elemtos del juego en la pantalla
    game.update()  # actualiza el juego
    pygame.display.update()  # actualiza la pantalla del juego
