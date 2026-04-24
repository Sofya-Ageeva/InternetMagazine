from src.product import Product


class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: str, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self) -> str:
        return (f"{self.name} {self.model}, {self.price} руб. "
                f"Остаток: {self.quantity} шт. "
                f"(Эффективность: {self.efficiency}, Память: {self.memory} ГБ, Цвет: {self.color})")
