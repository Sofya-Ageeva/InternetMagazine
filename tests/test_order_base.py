import pytest

from src.order_base import Order, OrderBase
from src.product import Product


def test_order_base_is_abstract():
    """Проверяет, что OrderBase — абстрактный класс."""
    with pytest.raises(TypeError):
        OrderBase()


def test_order_inherits_from_order_base():
    """Проверяет, что Order наследуется от OrderBase."""
    order = Order(Product("Тест", "Описание", 100.0, 5), 2)
    assert isinstance(order, OrderBase)


def test_order_initialization_with_valid_data():
    """Проверяет создание заказа с корректными данными."""
    product = Product("Книга", "Учебная литература", 500.0, 10)
    order = Order(product, 3)

    assert order.product == product
    assert order.quantity == 3
    assert order.total_cost == 1500.0


def test_order_get_total_cost():
    """Проверяет метод get_total_cost."""
    product = Product("Мышь", "Беспроводная", 2500.5, 20)
    order = Order(product, 2)

    total = order.get_total_cost()
    assert total == 5001.0
    assert isinstance(total, float)
