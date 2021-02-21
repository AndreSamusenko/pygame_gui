from settings import *


class CheckBoxItem:
    def __init__(self, size):
        self._x = 0
        self._y = 0
        self._size = size
        self._normal_form = CheckBoxItem.__create_form((size, size), (45, 65, 210))
        self._checked_form = CheckBoxItem.__create_form((size, size), (110, 90, 240))
        self.__is_checked = False

    @property
    def is_checked(self):
        return self.__is_checked

    @is_checked.setter
    def is_checked(self, value):
        self.__is_checked = value

    def __reverse_checked(self):
        self.__is_checked = not self.__is_checked

    def __set_x_y(self, x, y):
        self._x = x
        self._y = y

    def __show_normal(self):
        screen.blit(self._normal_form, (self._x, self._y))

    def __show_checked(self):
        screen.blit(self._checked_form, (self._x, self._y))

    def __is_hovered(self):
        pos = pygame.mouse.get_pos()
        return self._x <= pos[0] <= self._x + self._size and self._y <= pos[1] <= self._y + self._size

    def __is_clicked(self, _clicked):
        return _clicked and self.__is_hovered()

    def render(self, x, y, _is_mb_clicked):
        self.__set_x_y(x, y)

        if self.__is_clicked(_is_mb_clicked):
            self.__reverse_checked()

        if not self.__is_checked:
            self.__show_normal()
        else:
            self.__show_checked()

    @staticmethod
    def __create_form(size, color=(0, 234, 234)):
        form = pygame.Surface(size)
        form.fill(color)
        return form
