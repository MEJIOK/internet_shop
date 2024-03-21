from typing import Any


class Product:
    """Class representing a product."""

    def __init__(self, name: str, description: str, price: float, quantity: int, color: str):
        """Initialize a Product object with name, description, price, and quantity."""
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
        if isinstance(other, Product):
            total_price_self = self.price * self.quantity
            total_price_other = other.price * other.quantity
            total_price = total_price_self + total_price_other
            return total_price
        else:
            raise ValueError("Нельзя складывать продукты с объектами других классов.")


class CategoryIterator:
    """Iterator for iterating over products in a category."""

    def __init__(self, category):
        self._category = category
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._category.get_products()):
            product = self._category.get_products()[self._index]
            self._index += 1
            return product
        else:
            raise StopIteration


class Smartphone(Product):
    """Class representing a smartphone."""
    def __init__(self, name: str, description: str, price: float, quantity: int, color: str,
                 performance: str, model: str, memory: str):
        """Initialize a Smartphone object with additional attributes."""
        super().__init__(name, description, price, quantity, color)
        self.performance = performance
        self.model = model
        self.memory = memory


class Grass(Product):
    """Class representing lawn grass."""
    def __init__(self, name: str, description: str, price: float, quantity: int, color: str,
                 country_of_origin: str, germination_period: str):
        """Initialize a LawnGrass object with additional attributes."""
        super().__init__(name, description, price, quantity, color)
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
