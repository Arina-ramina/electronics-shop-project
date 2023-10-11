"""Тесты с использованием pytest для модуля item."""
from src.item import Item
from src.phone import Phone


def test_name_setter():
    """Проверка на изменение имени"""
    item = Item('test1', 20.0, 5)
    item.name = 'test2'
    assert item.name == 'test2'


def test_repr():
    """Проверка на ожидаемый результат по шаблону """
    item = Item('test1', 10000, 20)

    assert repr(item) == "Item('test1', 10000, 20)"


def test_str():
    """Проверка на ожидаемый результат по шаблону """
    item = Item('test1', 10000, 20)

    assert str(item) == 'test1'


def test_len_name():
    """Длина имени не более 10"""
    item = Item('test1', 20.0, 5)
    item.name = 'This is long name'
    assert item.name == 'This is lo'


def test_calculate_total_price():
    """Проверка на корректный расчет общей стоимости товара"""
    item1 = Item('test1', 20.0, 5)
    assert item1.calculate_total_price() == 100.0


def test_apply_discount():
    """Проверка на изменение скидки к цене товара"""
    item1 = Item('test2', 20.0, 5)
    item1.pay_rate = 0.5
    item1.apply_discount()
    assert item1.price == 10


def test_string_to_number():
    assert Item.string_to_number('5') == 5


def test_add_items():
    """Проверка на верное количество при сложении из разных классов"""
    item1 = Item('test1', 20.0, 1)
    item2 = Item('test2', 10, 2)
    phone1 = Phone('test3', 10, 3, 2)
    phone2 = Phone('test4', 10, 4, 2)
    assert item1 + item2 == 3
    assert item1 + phone1 == 4
    assert phone1 + phone2 == 7
