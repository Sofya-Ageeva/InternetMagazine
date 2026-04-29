class LoggingMixin:
    """Миксин для логирования создания объектов. Печатает информацию о классе и параметрах при создании объекта."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        class_name = self.__class__.__name__
        params = ', '.join([repr(arg) for arg in args] + [f"{k}={v!r}" for k, v in kwargs.items()])
        print(f"{class_name}({params})")
