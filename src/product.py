

class Product:
    name = str
    description = str
    price = float
    quantity = int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Геттер для приватной цены."""
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """Сеттер для цены с проверкой."""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            # Дополнительное задание: запрос подтверждения при понижении цены
            if value < self.__price:
                confirmation = input(
                    f"Цена понижается с {self.__price} до {value}. Подтвердить? (y/n): "
                )
                if confirmation.lower() == 'y':
                    self.__price = value
                else:
                    print("Изменение цены отменено")
            else:
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
