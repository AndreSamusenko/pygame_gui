import pygame
from Button import *
from settings import *


def printer():
    print("Нажали")


Button1 = ButtonImage(100, 100, main_state_img, pressed_state_img, pressed_state_img)
Button1.set_action(printer)
Button2 = ButtonImage(100, 100, main_state_img, pressed_state_img, pressed_state_img)
Button2.set_action(printer)


while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
    Button1.render(300, 300, clicked)
    Button2.render(450, 300, clicked)
    pygame.display.update()
    clicked = False
    clock.tick(30)
