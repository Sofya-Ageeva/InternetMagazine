
from src.lawngrass import LawnGrass


def test_lawngrass_initialization():
    grass = LawnGrass(
        "Трава газонная", "Зелёная трава", 1500.0, 10,
        "Россия", "14–21 день", "зелёный"
    )
    assert grass.country == "Россия"
    assert grass.germination_period == "14–21 день"


def test_lawngrass_str_representation():
    grass = LawnGrass("Трава газонная", "Описание", 1500.0, 10, "Россия",
                      "14–21 день", "зелёный")
    result = str(grass)
    expected = ("Трава газонная, 1500.0 руб. Остаток: 10 шт. (Страна: Россия, Срок прорастания: 14–21 день, "
                "Цвет: зелёный)")
    assert result == expected
