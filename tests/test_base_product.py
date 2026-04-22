from abc import ABC
from src.base_product import BaseProduct
from src.product import Product


def test_base_product_is_abstract():
    assert issubclass(BaseProduct, ABC)


def test_product_inherits_from_base_product():
    product = Product("Тест", "Описание", 1000, 5)
    assert isinstance(product, BaseProduct)


def test_abstract_methods_implemented():
    product = Product("Тест", "Описание", 1000, 5)
    # Проверяем, что все абстрактные методы реализованы
    assert hasattr(product, 'price')
    assert callable(product.__str__)
    assert callable(product.__add__)
