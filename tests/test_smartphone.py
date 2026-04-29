
from src.smartphone import Smartphone


def test_smartphone_initialization():
    smartphone = Smartphone(
        "iPhone 15", "Смартфон Apple", 99999.99, 5,
        "высокая", "iPhone 15 Pro", 256, "серый"
    )
    assert smartphone.name == "iPhone 15"
    assert smartphone.efficiency == "высокая"
    assert smartphone.memory == 256


def test_smartphone_str_representation():
    smartphone = Smartphone(
        "iPhone 15", "Смартфон", 99999.99, 5,
        "высокая", "Pro", 256, "серый"
    )
    result = str(smartphone)
    expected = "iPhone 15 Pro, 99999.99 руб. Остаток: 5 шт. (Эффективность: высокая, Память: 256 ГБ, Цвет: серый)"
    assert result == expected
