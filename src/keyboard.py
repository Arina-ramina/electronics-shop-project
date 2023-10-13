from src.item import Item


class MixinLang:
    def __init__(self):
        language = "EN"
        self.language = language

    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"
        else:
            self.language = "EN"

    def save_lang(self):
        print(f'Язык клавиатуры - {self.language}')


class Keyboard(Item, MixinLang):
    def __init__(self, name: str, price: float, quantity: int, languange="EN"):
        super().__init__(name, price, quantity)
        self.language = languange
        if self.language.upper() != "EN" and self.language.upper() != "RU":
            raise ValueError('язык клавиатуры может быть только EN или RU')
