"""тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

def test_calculate_total_price():
    item1 = Item('test1', 20.0, 5)
    assert item1.calculate_total_price() == 100.0

def test_apply_discount():
    item1 = Item('test2', 20.0, 5)
    item1.pay_rate = 0.5
    item1.apply_discount()
    assert item1.price == 10
