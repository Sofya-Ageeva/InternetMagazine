import json
from typing import List

from src.category import Category
from src.product import Product


def read_json(filename: str) -> tuple[List[Product], List[Category]]:
    """
    Загружает данные из JSON-файла и создаёт объекты классов Product и Category.
    Возвращает кортеж (список продуктов, список категорий).
    """

    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    products = []
    categories = []

    for category_data in data:
        category_products = []
        for product_data in category_data.get('products', []):
            product = Product(
                name=product_data['name'],
                description=product_data['description'],
                price=product_data['price'],
                quantity=product_data['quantity']
            )
            products.append(product)
            category_products.append(product)

        category = Category(
            name=category_data['name'],
            description=category_data['description'],
            products=category_products
        )
        categories.append(category)

    return products, categories


# open_json = read_json('data/products.json')
# print(open_json)
