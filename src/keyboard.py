from src.item import Item


class MixinLang:
    def __init__(self):
        language = "EN"
        self.__language = language

    @property
    def language(self):
        return self.__language


    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"

    def save_lang(self):
        print(f'Язык клавиатуры - {self.__language}')


class Keyboard(Item, MixinLang):
    def __init__(self, name: str, price: float, quantity: int, languange="EN"):
        super().__init__(name, price, quantity)
        self.__language = languange
        if self.language.upper() != "EN" and self.language.upper() != "RU":
            raise ValueError('язык клавиатуры может быть только EN или RU')
