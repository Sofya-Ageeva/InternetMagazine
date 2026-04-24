import pytest
from src.category import Category
from src.product import Product
from src.iterator import CategoryIterator


def test_iterator_basic():
    """Базовый тест итератора."""
    category = Category("Техника", "Бытовая техника")
    product1 = Product("Холодильник", "Белый", 50000, 3)
    product2 = Product("Стиралка", "Белая", 30000, 7)
    category.add_product(product1)
    category.add_product(product2)

    iterator = CategoryIterator(category)
    products = list(iterator)

    assert len(products) == 2
    assert products[0].name == "Холодильник"
    assert products[1].name == "Стиралка"


def test_iterator_empty_category():
    """Тест итератора для пустой категории."""
    category = Category("Пустая", "Нет товаров")
    iterator = CategoryIterator(category)

    with pytest.raises(StopIteration):
        next(iterator)
