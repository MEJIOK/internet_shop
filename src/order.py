from abc import ABC, abstractmethod

from src.category import ZeroQuantityError
from src.products import Product, CreationInfoMixin


class AbstractOrder(ABC):
    """Abstract base class for orders."""
    @abstractmethod
    def __init__(self, product: Product, quantity: int) -> None:
        """Initialize an Order object with a product and quantity."""
        self.quantity = quantity
        self.product = product

    @abstractmethod
    def total_cost(self) -> float:
        """Calculate the total cost of the order."""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Return a string representation of the order."""
        pass


class Order(AbstractOrder, CreationInfoMixin):
    """Class representing an order for a product."""
    total_orders = 0

    def __init__(self, product: Product, quantity: int) -> None:
        """Initialize an Order object with a product and quantity."""
        try:
            if quantity == 0:
                raise ZeroQuantityError()
            super().__init__(product, quantity)
            self.product = product
            self.quantity = quantity
            Order.total_orders += 1
            print("Товар успешно добавлен.")
        except ZeroQuantityError as e:
            print(e)
        finally:
            print("Обработка добавления товара завершена.")

    def total_cost(self) -> float:
        """Calculate the total cost of the order."""
        return self.product.price * self.quantity

    def __str__(self) -> str:
        """Return a string representation of the order."""
        return f"Order: {self.product.name}, Quantity: {self.quantity}, Total Cost: {self.total_cost()} руб."
