from typing import List, Optional
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
        Category.product_count += len(products)

    def add_product(self, product) -> None:
        """Добавляет продукт в категорию, если он является экземпляром Product или его наследником."""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")
        self.products.append(product)

    @property
    def products(self) -> str:
        """Геттер для приватного атрибута __products."""
        result = []
        for product in self.__products:
            result.append(f"{product}\n")
        return ''.join(result)

    def get_products_list(self) -> List[Product]:
        """Возвращает приватный список продуктов как обычный список для программной работы."""
        return self.__products

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
