from src.product import Product
from src.category import Category


class CategoryIterator:
    """Итератор для перебора товаров в категории."""
    def __init__(self, category: 'Category'):
        self._products = category.get_products_list()
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self) -> 'Product':
        if self._index >= len(self._products):
            raise StopIteration
        product = self._products[self._index]
        self._index += 1
        return product
