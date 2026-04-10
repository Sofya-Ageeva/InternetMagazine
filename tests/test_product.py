import pytest

from src.product import Product


@pytest.fixture
def sample_product():
    return Product("Смартфон", "Современный смартфон", 29999.99, 10)


def test_product_initialization(sample_product):
    assert sample_product.name == "Смартфон"
    assert sample_product.description == "Современный смартфон"
    assert sample_product.price == 29999.99
    assert sample_product.quantity == 10


def test_product_types():
    product = Product("Ноутбук", "Игровой ноутбук", 59999.99, 5)
    assert isinstance(product.name, str)
    assert isinstance(product.description, str)
    assert isinstance(product.price, (float, int))
    assert isinstance(product.quantity, int)


def test_product_quantity_zero():
    """Тест: количество может быть равно нулю (товар закончился)."""
    product = Product("Планшет", "Старый планшет", 15000.00, 0)
    assert product.quantity == 0
