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


def test_price_getter(sample_product):
    """Проверяет, что геттер price возвращает корректное значение."""
    assert sample_product.price == 29999.99


def test_price_setter_positive(sample_product):
    """Проверяет установку положительной цены через сеттер."""
    sample_product.price = 35000.0
    assert sample_product.price == 35000.0


def test_price_setter_negative(capsys, sample_product):
    """Проверяет обработку отрицательной цены — сообщение и отсутствие изменений."""
    sample_product.price = -5000
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert sample_product.price == 29999.99


def test_price_setter_zero(capsys, sample_product):
    """Проверяет обработку нулевой цены — сообщение и отсутствие изменений."""
    sample_product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert sample_product.price == 29999.99  # цена не изменилась


def test_new_product_classmethod():
    """Проверяет создание продукта через класс-метод new_product."""
    product_data = {
        'name': 'Ноутбук',
        'description': 'Игровой ноутбук',
        'price': 59999.99,
        'quantity': 5
    }

    product = Product.new_product(product_data)
    assert product.name == 'Ноутбук'
    assert product.description == 'Игровой ноутбук'
    assert product.price == 59999.99
    assert product.quantity == 5


def test_price_setter_confirmation_required(monkeypatch, sample_product):
    """Проверяет запрос подтверждения при понижении цены."""
    def mock_input(_):
        return 'y'

    monkeypatch.setattr('builtins.input', mock_input)
    sample_product.price = 25000.0  # понижаем цену
    assert sample_product.price == 25000.0


def test_product_str_format(sample_product):
    """Проверяет формат строкового представления продукта."""
    result = str(sample_product)
    expected = "Смартфон, 29999.99 руб. Остаток: 10 шт."
    assert result == expected


def test_product_str_zero_quantity():
    """Проверяет __str__ при нулевом количестве."""
    product = Product("Распродан", "Товар закончился", 5000.0, 0)
    result = str(product)
    expected = "Распродан, 5000.0 руб. Остаток: 0 шт."
    assert result == expected


def test_product_addition_basic():
    """Базовый тест сложения двух продуктов."""
    product_a = Product("Товар A", "Описание", 100, 10)
    product_b = Product("Товар B", "Описание", 200, 2)
    result = product_a + product_b
    expected = 100 * 10 + 200 * 2  # 1400
    assert result == expected


def test_addition_zero_quantity():
    """Тест сложения с продуктом с нулевым количеством."""
    product_a = Product("Товар A", "Описание", 100, 0)
    product_b = Product("Товар B", "Описание", 50, 4)
    result = product_a + product_b
    expected = 0 + 50 * 4  # 200
    assert result == expected


def test_addition_with_non_product(sample_product):
    with pytest.raises(TypeError):
        sample_product + "не продукт"


def test_addition_same_product():
    """Тест сложения одного и того же продукта."""
    product = Product("Товар", "Описание", 75, 8)
    result = product + product
    expected = 75 * 8 + 75 * 8  # 1200
    assert result == expected
