from typing import List, Optional

from src.product import Product


class Category:
    name = str
    description = str
    products = Optional[List[Product]]

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name, description, products=None) -> None:
        if products is None:
            products = []

        self.name = name
        self.description = description
        self.__products = products

        # Автоматическое увеличение счётчиков
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: 'Product') -> None:
        """Добавляет продукт в категорию и увеличивает счётчик."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер для приватного атрибута __products."""
        result = []
        for product in self.__products:
            result.append(
                f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
            )
        return ''.join(result)

    def get_products_list(self) -> List[Product]:
        """Возвращает приватный список продуктов как обычный список для программной работы."""
        return self.__products
