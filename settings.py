import pygame

pygame.display.set_caption("GUI test")
screen = pygame.display.set_mode((800, 500))
main_state_img = pygame.image.load(r"images\main_state.png")
pressed_state_img = pygame.image.load(r"images\pressed_state.png")
clock = pygame.time.Clock()
pygame.font.init()
MB_CLICKED = False
