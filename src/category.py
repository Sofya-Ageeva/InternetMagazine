from typing import List, Optional

from src.exceptions import ZeroQuantityError
from src.product import Product


class Category:
    name = str
    description = str
    products = Optional[List[Product]]

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:
        if products is None:
            products = []

        self.name: str = name
        self.description: str = description
        self.__products: List[Product] = products

        # Автоматическое увеличение счётчиков
        Category.category_count += 1
        if products:
            Category.product_count += len(products)

    def add_product(self, product) -> None:
        """Добавляет продукт в категорию, если он является экземпляром Product или его наследником."""
        try:
            if not isinstance(product, Product):
                raise TypeError("Можно добавлять только объекты класса Product или его наследников")
            self.__products.append(product)
            Category.product_count += 1
        except ZeroQuantityError as e:
            print(f"Ошибка добавления товара {e}")
        else:
            print("Товар успешно добавлен")
        finally:
            print("Обработка добавления товара завершена")

    @property
    def products(self) -> str:
        """Геттер для приватного атрибута __products."""

        result = []
        for product in self.__products:
            result.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n")
        return ''.join(result)

    def get_products_list(self) -> List[Product]:
        """Возвращает приватный список продуктов как обычный список для программной работы."""
        return self.__products

    def middle_price(self) -> float:
        """Осуществляет подсчет средней цены всех товаров в категории."""
        try:
            total_price = sum(product.price for product in self.__products)
            middle = total_price / len(self.__products)
            return middle
        except ZeroDivisionError:
            return 0.0

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
