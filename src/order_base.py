from abc import ABC, abstractmethod
from src.product import Product


class OrderBase(ABC):
    """Абстрактный класс для общих свойств заказа и категории."""

    @abstractmethod
    def get_total_cost(self) -> float:
        pass

    @abstractmethod
    def display_info(self) -> str:
        pass


class Order(OrderBase):
    def __init__(self, product: 'Product', quantity: int):
        self.product = product
        self.quantity = quantity
        self.total_cost = product.price * quantity

    def get_total_cost(self) -> float:
        return self.total_cost

    def display_info(self) -> str:
        return (f"Заказ: {self.product.name}, "
                f"количество: {self.quantity}, "
                f"итого: {self.total_cost} руб.")
