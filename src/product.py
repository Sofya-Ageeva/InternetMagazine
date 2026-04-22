from src.base_product import BaseProduct

class Product(BaseProduct):
    name = str
    description = str
    price = float
    quantity = int

    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)
        self.__price = price

    @property
    def price(self) -> float:
        """Геттер для приватной цены."""
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """Сеттер для цены с проверкой."""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = value

    @classmethod
    def new_product(cls, product_data: dict, product_list: list = None) -> 'Product':
        """
        Создаёт новый продукт из словаря.
        Если продукт с таким именем уже есть в product_list,
        объединяет количество и берёт максимальную цену.
        """
        if product_list:
            for existing_product in product_list:
                if existing_product.name == product_data['name']:
                    # Складываем количество
                    existing_product.quantity += product_data['quantity']
            # Берём максимальную цену
            if product_data['price'] > existing_product.__price:
                existing_product.__price = product_data['price']
            return existing_product

        # Если дубликата нет, создаём новый продукт
        return cls(
            name=product_data['name'],
            description=product_data['description'],
            price=product_data['price'],
            quantity=product_data['quantity']
        )

    def __str__(self) -> str:
        """Строковое представление продукта."""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: 'Product') -> float:
        """Возвращает сумму произведений цены на количество у двух объектов."""
        if type(self) is not type(other) :
            raise TypeError(f"Нельзя сложить {type(self).__name__} с {type(other).__name__}")
        return self.__price * self.quantity + other.__price * other.quantity
