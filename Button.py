import pygame
from settings import *


class ButtonBase:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.is_pressed = False
        self.x = 0
        self.y = 0
        self.main_state = None
        self.hovered_state = None
        self.pressed_state = None
        self.action = None

    def __is_hovered(self):
        pos = pygame.mouse.get_pos()
        return self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height

    def __is_clicked(self, clicked):
        return clicked and self.__is_hovered()

    def __set_x_y(self, x, y):
        self.x = x
        self.y = y

    def render(self, x, y, clicked):
        self.__set_x_y(x, y)

        if self.__is_clicked(clicked):
            screen.blit(self.pressed_state, (self.x, self.y))
            self.action()
        elif self.__is_hovered():
            screen.blit(self.hovered_state, (self.x, self.y))
        else:
            screen.blit(self.main_state, (self.x, self.y))

    def set_action(self, action):
        if action:
            self.action = action
        else:
            print("На кнопку не было добавлено действие")


class ButtonImage(ButtonBase):
    def __init__(self, height, width, main_state, hovered_state, pressed_state):
        super().__init__(height, width)
        self.main_state = main_state
        self.hovered_state = hovered_state
        self.pressed_state = pressed_state


class ButtonForm(ButtonBase):
    def __init__(self, height, width, main_color, hovered_color, pressed_color):
        super().__init__(height, width)
        self.main_state = ButtonForm.__create_form((height, width), main_color)
        self.hovered_state = ButtonForm.__create_form((height, width), hovered_color)
        self.pressed_state = ButtonForm.__create_form((height, width), pressed_color)

    @staticmethod
    def __create_form(size, color):
        form = pygame.Surface(size)
        form.fill(color)
        return form
