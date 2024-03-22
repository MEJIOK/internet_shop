from typing import Any
from abc import ABC, abstractmethod


class CreationInfoMixin:
    """Mixin for printing information about created objects."""
    def __repr__(self):
        """Return a string representation of the object."""
        class_name = self.__class__.__name__
        attributes = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{class_name}({attributes})"

    def __init__(self, *args, **kwargs):
        """Initialize the object and print its attributes."""
        print(f"Object of class {self.__class__.__name__} has been created:")
        for key, value in kwargs.items():
            print(f"{key}: {value}")
        super().__init__(*args, **kwargs)


class AbstractProduct(ABC):
    """Abstract base class for products."""
    def __init__(self, name: str, description: str, price: float, quantity: int, color: str):
        super().__init__()
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity
        self.color = color

    def __str__(self) -> str:
        """Return a string representation of the product."""
        return f"{self.name}, {self._price} руб. Остаток: {self.quantity} шт., Цвет: {self.color}"

    @property
    def price(self) -> float:
        """Getter for the price attribute."""
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        """Setter for the price attribute."""
        if value <= 0:
            print("Ошибка: цена введена некорректно.")
        elif value < self._price:
            confirmation = input("Цена товара понижается. Вы уверены? (y/n): ")
            if confirmation.lower() == 'y':
                self._price = value
                print("Цена товара успешно изменена.")
            else:
                print("Изменение цены отменено.")
        else:
            self._price = value

    @abstractmethod
    def additional_info(self) -> str:
        """Abstract method to return additional information about the product."""
        pass

    @classmethod
    def from_dict(cls, data: dict):
        """Create a Product object from a dictionary."""
        return cls(data['name'], data['description'], data['price'], data['quantity'], data['color'])

    @classmethod
    def create(cls, **kwargs: Any):
        """Create a new product using kwargs."""
        return cls(**kwargs)

    @classmethod
    def create_product(cls, name: str, description: str, price: float, quantity: int, color: str, products_list):
        """Create a new product or update existing one and return it."""
        for product in products_list:
            if product.name == name:
                # Если товар с таким именем уже существует, обновляем его данные
                product.price = max(product.price, price)  # Выбираем более высокую цену
                product.quantity += quantity  # Увеличиваем количество в наличии
                return product  # Возвращаем существующий товар

        # Если товар с таким именем не найден, создаем новый товар
        return cls(name, description, price, quantity, color)

    def __add__(self, other) -> float:
        """Return the total price of two products considering their quantities."""
        if isinstance(other, type(self)):
            total_price_self = self.price * self.quantity
            total_price_other = other.price * other.quantity
            total_price = total_price_self + total_price_other
            return total_price
        else:
            raise TypeError("Нельзя складывать продукты разных типов или объекты других классов.")


class Product(AbstractProduct):
    """Class representing a product."""
    def additional_info(self) -> str:
        return ""  # Получается, что нет особых аттрибутов (свойств) обычного продукта?


class Smartphone(AbstractProduct):
    """Class representing a smartphone."""

    def __init__(self, name: str, description: str, price: float, quantity: int, color: str,
                 performance: str, model: str, memory: str):
        super().__init__(name, description, price, quantity, color)  # Используем инициализатор родительского класса
        self.performance = performance
        self.model = model
        self.memory = memory

    def additional_info(self) -> str:
        return f"Performance: {self.performance}, Model: {self.model}, Memory: {self.memory}"


class Grass(AbstractProduct):
    """Class representing lawn grass."""
    def __init__(self, name: str, description: str, price: float, quantity: int, color: str,
                 country_of_origin: str, germination_period: str):
        super().__init__(name, description, price, quantity, color)
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period

    def additional_info(self) -> str:
        return f"Country of Origin: {self.country_of_origin}, Germination Period: {self.germination_period}"


if __name__ == "__main__":
    # Пример использования
    smartphone = Smartphone("iPhone", "Apple smartphone", 1299.99, 8,
                            "silver", "High", "iPhone 12", "256GB")
    print(smartphone.additional_info())

    grass = Grass("Green Grass", "Lawn grass for garden", 5.99, 100,
                  "green", "USA", "2 weeks")
    print(grass.additional_info())
