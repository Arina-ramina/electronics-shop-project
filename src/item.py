import codecs
import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []


    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)


    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self, name):
        if len(name) < 10:
            self.__name = name
        else:
            self.__name = name[0:10]
        Item.all.remove(self)
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"


    def __str__(self):
        return f"{self.__name}"

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price


    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate


    @classmethod
    def instantiate_from_csv(cls, filename: str) -> None:
        '''инициализием экземпляры класса Item данными из файла src/items.csv'''
        cls.all.clear() #очистка списка перед загрузкой данных из файла csv

        with codecs.open(filename,'r', encoding='utf-8', errors='replace') as f:
            reader = csv.DictReader(f)
            items=[]
            for row in reader:
                name = row['name']
                price = float(row['price'])
                quantity = int(row['quantity'])
                item = cls(name, price, quantity)
                items.append(item)

            cls.all= items


    @staticmethod
    def string_to_number(str_number: str) -> int:
        number = str_number.split('.')
        return int(number[0])





