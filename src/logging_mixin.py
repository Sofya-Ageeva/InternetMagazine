class LoggingMixin:
    """Миксин для логирования создания объектов. Печатает информацию о классе и параметрах при создании объекта."""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(repr(self))


    def __repr__(self) -> str:
        """Формирует строку вида ClassName с параметрами создания."""
        args_list = [
            repr(self.name),
            repr(self.description),
            repr(self.price),
            repr(self.quantity)
        ]
        return f"{self.__class__.__name__}({', '.join(args_list)})"
