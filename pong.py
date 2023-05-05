import pygame
from data import *
from random import choice
import time
import json

class Board(pygame.Rect):
    def __init__(self, x, y, width, height, image=None, speed= 5):
        super().__init__(x, y, width, height)
        self.IMAGE = image
        self.SPEED = speed
        self.MOVE = {"UP": False, "DOWN": False}
    def move(self):
        if self.MOVE["UP"] and self.y > 0:
            self.y -= self.SPEED
        elif self.MOVE["DOWN"] and self.y < setting_win["HEIGHT"] - setting_board["HEIGHT"]:
            self.y += self.SPEED

class Point():
    def __init__(self, name_left, name_right):
        self.NAME_LEFT = name_left
        self.NAME_RIGHT = name_right
        self.LEFT_POINT = 0
        self.RIGHT_POINT = 0
        self.FONT = pygame.font.Font(None, 40)
    def blit_point(self, window):
        window.blit(self.FONT.render(f"{self.LEFT_POINT} : {self.RIGHT_POINT}", True, (200,255,255)), (setting_win["WIDTH"] // 2 - 50, 10))

class Ball():
    def __init__(self, x, y, radius, image= None, speed = 5):
        self.X = x
        self.Y = y
        self.RECT = pygame.Rect(x - radius, (radius ** 2 + radius ** 2)**0.5,(radius ** 2 + radius ** 2)**0.5)
        self.RADIUS = radius
        self.IMAGE = image
        self.SPEED = choice([-speed, speed])
        self.CONST = speed
        self.ANGLE = 0
        self.POINT = Point("left", "right")
        self.a ={-1}
    def make_angle(self, ang):
        if self.SPEED <0:
            self.SPEED = - self.CONST
        elif self.SPEED >0:
            self.SPEED = self.CONST
        self.ANGLE = ang * uniform(abs(self.SPEED // 2), abs(self.SPEED))
        coff = abs(self.SPEED) / abs((self.SPEED ** 2+ self.ANGLE**2)**0.5)
        self.ANGLE *= coff
        self.SPEED *= coff
    def restart(self, board_left, board_right, window):
        if self.POINT.LEFT_POINT == 1 or self.POINT.RIGHT_POINT == 1:
            history[str(time.time())] = {self.POINT.NAME_LEFT: self.POINT.LEFT_POINT, self.POINT.NAME_RIGHT: self.POINT.RIGHT_POINT}
            with open('history.json', 'w', encoding="utf-8") as file:
        self.SPEED = choice([-self.CONST, self.CONST])
        self.ANGLE = 0
        self.X, self.Y = restart["RESTART_BALL"]
        self.RECT.center = restart["RESTART_BALL"]
        board_left.y = restart["RESTART_BOARD_LEFT"][1] 
        board_right.y = restart["RESTART_BOARD_RIGHT"][1] 
        window.fill((0,0,0))
        pygame.draw.rect(window, (255,255,255), board_left)
        pygame.draw.rect(window, (255,255,255), board_right)
        pygame.draw.circle(window, (255,255,255), self.RECT.center, self.RADIUS)
        self.POINT.blit_point(window)
        pygame.display.flip()
        time.sleep(2)
    def move(self, board_left, board_right, window):
        if self.X - self.RADIUS <= 0:
            self.POINT.RIGHT_POINT += 1
            self.restart(board_left, board_right, window)
        elif self.Y - self.RADIUS >= setting_win["WIDTH"]:
            self.POINT.LEFT_POINT += 1
            self.restart(board_left, board_right, window)
        if self.Y - self.RADIUS <= 0 or self.Y + self.RADIUS >= setting_win["HEIGHT"]:
            self.ANGLE *= -1
        elif board_left.collidepoint(self.X - self.RADIUS, self.Y) or board_left.collidepoint(self.X +self.RADIUS, self.Y):
            self.SPEED *= -1
            if board_left.MOVE["UP"]:
                self.make_angle(-1)
            if board_left.MOVE["DOWN"]:
                self.make_angle(1)
        elif board_right.collidepoint(self.X - self.RADIUS, self.Y) or board_right.collidepoint(self.RECT):
            self.SPEED *= -1
            if board_right.MOVE["UP"]:
                self.make_angle(-1)
            if board_right.MOVE["DOWN"]:
                self.make_angle(1)
        self.Y += self.ANGLE
        self.RECT.y = self.Y
        self.X += self.SPEED
        self.RECT.x = self.X
        self.a.add((self.SPEED ** 2 + self.ANGLE ** 2) ** 0.5)

class Menu():
    def __init__(self, width, height, count):
        self.BUTTONS = list()