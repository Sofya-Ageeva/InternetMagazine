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
        self.products = products

        # Автоматическое увеличение счётчиков
        Category.category_count += 1
        Category.product_count += len(products)
