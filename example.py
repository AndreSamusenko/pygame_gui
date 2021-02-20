from Button import *
from settings import *


def printer(sender=None):
    print("Button", str(sender)[-11:-1], "was cliked")


Button1 = ButtonImage(100, 100, main_state_img, pressed_state_img, pressed_state_img, "PRESS")
Button1.set_action(lambda: printer(Button1))
Button2 = ButtonForm(100, 100, (255, 174, 100), (205, 174, 100), (105, 174, 100), "PRESS")
Button2.set_action(lambda: printer(Button2))


while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            MB_CLICKED = True
            Button1.text = "NEW"
    Button1.render(300, 300, MB_CLICKED)
    Button2.render(450, 300, MB_CLICKED)
    pygame.display.update()
    MB_CLICKED = False
    clock.tick(15)
