from settings import *


def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print("Передали ли мне что-нибудь?:")
        print(args)
        print(kwargs)
        function_to_decorate(*args, **kwargs)
    return a_wrapper_accepting_arbitrary_arguments


class ButtonBase:
    def __init__(self, height, width, text=None):
        self.height = height
        self.width = width
        self.is_pressed = False
        self.x = 0
        self.y = 0
        self._main_state = None
        self._hovered_state = None
        self._pressed_state = None
        self.action = None
        self.text = text

    def __is_hovered(self):
        pos = pygame.mouse.get_pos()
        return self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height

    def __is_clicked(self, _clicked):
        return _clicked and self.__is_hovered()

    def __set_x_y(self, x, y):
        self.x = x
        self.y = y

    def render(self, x, y, _clicked):
        self.__set_x_y(x, y)

        if self.__is_clicked(_clicked):
            self.__make_pressed_state()
        elif self.__is_hovered():
            self.__make_hovered_state()
        else:
            self.__make_main_state()

    def set_action(self, action):
        if action:
            self.action = action
        else:
            print("На кнопку не было добавлено действие")

    def __make_main_state(self):
        screen.blit(self._main_state, (self.x, self.y))

    def __make_hovered_state(self):
        screen.blit(self._hovered_state, (self.x, self.y))

    def __make_pressed_state(self):
        screen.blit(self._pressed_state, (self.x, self.y))
        self.action()


class ButtonImage(ButtonBase):
    def __init__(self, height, width, main_state, hovered_state, pressed_state, text=""):
        super().__init__(height, width, text)
        self._main_state = main_state
        self._hovered_state = hovered_state
        self._pressed_state = pressed_state


class ButtonForm(ButtonBase):
    def __init__(self, height, width, main_color, hovered_color, pressed_color, text=""):
        super().__init__(height, width, text)
        self._main_state = ButtonForm.__create_form((height, width), main_color)
        self._hovered_state = ButtonForm.__create_form((height, width), hovered_color)
        self._pressed_state = ButtonForm.__create_form((height, width), pressed_color)

    @staticmethod
    def __create_form(size, color):
        form = pygame.Surface(size)
        form.fill(color)
        return form
