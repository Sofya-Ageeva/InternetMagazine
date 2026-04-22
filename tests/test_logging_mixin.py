
import io
import sys
from src.logging_mixin import LoggingMixin
from src.product import Product

def test_logging_mixin_output():
    # Перехватываем вывод в консоль
    captured_output = io.StringIO()
    sys.stdout = captured_output

    product = Product("Смартфон", "Современный", 29999.99, 10)

    # Восстанавливаем стандартный вывод
    sys.stdout = sys.__stdout__

    output = captured_output.getvalue().strip()
    assert "Product('Смартфон', 'Современный', 29999.99, 10)" in output