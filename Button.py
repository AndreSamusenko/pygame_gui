from settings import *


class ButtonBase(ABC):
    @abstractmethod
    def __init__(self, width, height, text=None):
        self._height = height
        self._width = width
        self.__is_pressed = False
        self._x = 0
        self._y = 0
        self._main_state = None
        self._hovered_state = None
        self._pressed_state = None
        self._is_active = True
        self._is_visible = True
        self.__action = None
        self.__text = text
        self.__font = pygame.font.Font('freesansbold.ttf', 24)
        self.__font_color = (0, 0, 0)
        self.__text_obj = None
        if text:
            self.__create_text(text)

    @property
    def is_pressed(self):
        return self.__is_pressed

    @property
    def center(self):
        return tuple([self._x + self._width / 2, self._y + self._height / 2])

    @property
    def center_x(self):
        return self._x + self._width / 2

    @property
    def center_y(self):
        return self._y + self._height / 2

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text):
        self.__create_text(text)

    @property
    def is_active(self):
        return self._is_active

    @is_active.setter
    def is_active(self, state: bool):
        self._is_active = state

    @property
    def is_visible(self):
        return self._is_active

    @is_visible.setter
    def is_visible(self, active_state: bool):
        self._is_active = active_state

    def __make_main_state(self):
        screen.blit(self._main_state, (self._x, self._y))
        self.__show_text()

    def __make_hovered_state(self):
        screen.blit(self._hovered_state, (self._x, self._y))
        self.__show_text()

    def __make_pressed_state(self):
        screen.blit(self._pressed_state, (self._x, self._y))
        self.__show_text()
        self.__action()

    def __is_hovered(self):
        pos = pygame.mouse.get_pos()
        return self._x <= pos[0] <= self._x + self._width and self._y <= pos[1] <= self._y + self._height

    def __is_clicked(self, _clicked):
        return _clicked and self.__is_hovered()

    def __set_x_y(self, x, y):
        self._x = x
        self._y = y

    def __create_text(self, text):
        self.__text = text
        self.__text_obj = self.__font.render(str(text), True, self.__font_color)

    def __show_text(self):
        if self.__text_obj:
            screen.blit(self.__text_obj, (self.center_x - self.__text_obj.get_width() / 2,
                                          self.center_y - self.__font.get_height() / 2))

    def render(self, x, y, _is_mb_clicked):
        self.__set_x_y(x, y)

        if self.__is_clicked(_is_mb_clicked):
            self.__make_pressed_state()
        elif self.__is_hovered():
            self.__make_hovered_state()
        else:
            self.__make_main_state()

    def set_action(self, action):
        if action:
            self.__action = action
        else:
            print("На кнопку не было добавлено действие")

    def click_virtually(self):
        self.__make_pressed_state()

    def set_font(self, font='freesansbold.ttf', size=24, color=(0, 0, 0)):
        self.__font = pygame.font.Font(font, size)
        self.__font_color = color


class ButtonImage(ButtonBase):
    def __init__(self, width, height,  main_state, hovered_state, pressed_state, text=""):
        super().__init__(width, height, text)
        self._main_state = main_state
        self._hovered_state = hovered_state
        self._pressed_state = pressed_state


class ButtonForm(ButtonBase):
    def __init__(self, width, height, main_color, hovered_color, pressed_color, text=""):
        super().__init__(width, height, text)
        self._main_state = ButtonForm.__create_form((width, height), main_color)
        self._hovered_state = ButtonForm.__create_form((width, height), hovered_color)
        self._pressed_state = ButtonForm.__create_form((width, height), pressed_color)

    @staticmethod
    def __create_form(size, color):
        form = pygame.Surface(size)
        form.fill(color)
        return form
