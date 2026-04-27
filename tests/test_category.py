import pytest
from src.category import Category
from src.product import Product
from src.smartphone import Smartphone
from src.lawngrass import LawnGrass


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


@pytest.fixture
def empty_category():
    return Category("Пустая категория", "Нет товаров", [])


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


def test_add_product(reset_category_counters):
    category = Category("Электроника", "Техника")
    product = Product("Наушники", "Беспроводные", 5000, 15)
    category.add_product(product)
    assert len(category.get_products_list()) == 1
    assert Category.product_count == 1


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


def test_product_count_increment():
    category1 = Category("Смартфоны", "Мобильные устройства")
    category2 = Category("Травы", "Газонная трава")

    phone = Smartphone("iPhone", "Смартфон", 10000, 2, "высокая", "Pro", 128, "чёрный")
    grass = LawnGrass("Трава", "Газонная", 1500, 10, "Россия", "14–21 день", "зелёный")

    category1.add_product(phone)
    category2.add_product(grass)

    assert Category.product_count == 2


def test_private_products_attribute(category_with_products):
    """Проверяет, что атрибут products приватный."""
    with pytest.raises(AttributeError):
        _ = category_with_products.__products


def test_add_valid_product():
    category = Category("Электроника", "Смартфоны и аксессуары")
    product = Product("Наушники", "Беспроводные", 5000, 15)
    category.add_product(product)
    assert len(category._Category__products) == 1


def test_add_smartphone_to_category():
    category = Category("Смартфоны", "Мобильные устройства")
    smartphone = Smartphone("iPhone", "Смартфон", 10000, 2, "высокая", "Pro", 128, "чёрный")
    category.add_product(smartphone)
    assert len(category._Category__products) == 1


def test_add_invalid_object_to_category():
    category = Category("Ошибки", "Тестовая категория")
    with pytest.raises(TypeError, match="Можно добавлять только объекты класса Product"):
        category.add_product("не продукт")


def test_average_price_empty_category(empty_category):
    """Средний ценник в пустой категории равен 0."""
    assert empty_category.middle_price() == 0.0


def test_average_price_with_products(category_with_products):
    """Расчёт среднего ценника для категории с товарами."""
    # (29 999,99 + 59 999,99) / 2 = 44 999,99
    expected = (29999.99 + 59999.99) / 2
    assert category_with_products.middle_price() == pytest.approx(expected, rel=1e-2)


def test_average_price_single_product():
    """Средний ценник для категории с одним товаром."""
    product = Product("Один товар", "Описание", 10000.0, 5)
    category = Category("Одиночный товар", "Один продукт", [product])
    assert category.middle_price() == 10000.0
