import pytest
from src.category import Category
from src.product import Product


@pytest.fixture(autouse=True)
def reset_category_counters():
    """Сбрасывает счётчики категорий и продуктов перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0


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
    assert len(category_with_products.get_products_list()) == 2


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


##
def test_add_product(category_with_products):
    """Проверяет добавление продукта через метод add_product."""
    new_product = Product("Наушники", "Беспроводные", 5000.0, 20)
    category_with_products.add_product(new_product)
    products_list = category_with_products.get_products_list()
    assert new_product in products_list
    assert Category.product_count == 3  # было 2, стало 3


def test_products_getter_format(category_with_products):
    """Проверяет формат вывода геттера products."""
    output = category_with_products.products
    assert "Смартфон, 29999.99 руб. Остаток: 10 шт." in output
    assert "Ноутбук, 59999.99 руб. Остаток: 5 шт." in output
    # проверяем шаблон для каждого продукта
    lines = output.strip().split('\n')
    for line in lines:
        assert line.endswith('шт.')
        assert 'руб.' in line


def test_product_count_increment(category_with_products):
    """Проверяет увеличение счётчика продуктов при добавлении."""
    initial_count = Category.product_count
    new_product = Product("Мышь", "Беспроводная", 2000.0, 15)
    category_with_products.add_product(new_product)
    assert Category.product_count == initial_count + 1


def test_private_products_attribute(category_with_products):
    """Проверяет, что атрибут products приватный."""
    with pytest.raises(AttributeError):
        _ = category_with_products.__products
