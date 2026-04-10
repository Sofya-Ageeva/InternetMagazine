import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def sample_product():
    return Product("Смартфон", "Современный смартфон", 29999.99, 10)


@pytest.fixture
def category_with_products(sample_product):
    products = [
        sample_product,
        Product("Ноутбук", "Мощный ноутбук", 59999.99, 5)
    ]
    return Category("Электроника", "Электронные товары", products)


def test_category_initialization(category_with_products, sample_product):
    assert category_with_products.name == "Электроника"
    assert category_with_products.description == "Электронные товары"
    assert len(category_with_products.products) == 2
    assert sample_product in category_with_products.products


def test_category_counters_increment():
    # Сбрасываем счётчики
    Category.category_count = 0
    Category.product_count = 0

    Category("Книги", "Книги", [Product("Книга1", "", 1000, 5)])
    Category("Одежда", "Одежда", [
        Product("Футболка", "", 500, 20),
        Product("Штаны", "", 1500, 10)
    ])

    assert Category.category_count == 2
    assert Category.product_count == 3


def test_empty_category():
    category = Category("Игрушки", "Детские игрушки", [])
    assert category.name == "Игрушки"
    assert len(category.products) == 0
    assert Category.category_count >= 1
