from src.products import Product
from abc import ABC, abstractmethod


class AbstractCategory(ABC):
    """Abstract base class for categories."""

    @abstractmethod
    def add_product(self, product: Product) -> None:
        """Add a product to the category."""
        pass

    @abstractmethod
    def products(self):
        """Get the list of products in the category."""
        pass

    @abstractmethod
    def __len__(self):
        """Return the total number of products in the category."""
        pass


class Category(AbstractCategory):
    """Class representing a category of products."""
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name: str, description: str, products=None, allowed_types=None) -> None:
        """Initialize a Category object with name, description, and products."""
        super().__init__()
        self.allowed_types = allowed_types
        self.name = name
        self.description = description
        self.__products = products if products is not None else []  # Приватный атрибут для хранения товаров
        Category.total_categories += 1
        Category.total_unique_products += len(set(self.__products))

    @classmethod
    def from_dict(cls, data: dict):
        """Create a Category object from a dictionary."""
        _category = cls(data['name'], data['description'])
        for product_data in data.get('products', []):
            product = Product.create_product(**product_data)
            _category.add_product(product)  # Используем метод добавления продукта
        return _category

    def add_product(self, product: Product) -> None:
        """Add a product to the category."""
        try:
            if product.quantity == 0:
                raise ZeroQuantityError("Товар с нулевым количеством не может быть добавлен.")
            if not isinstance(product, self.allowed_types):
                raise TypeError(f"Можно добавлять только продукты следующих типов: {self.allowed_types}")
        except (ZeroQuantityError, TypeError) as e:
            print(f"Ошибка при добавлении товара: {e}")
        else:
            self.__products.append(product)
            self.total_unique_products += 1
            print("Товар успешно добавлен.")
        finally:
            print("Обработка добавления товара завершена.")

    def products(self):
        """Get the list of products in the category."""
        return self.__products

    @property
    def products_info(self) -> str:
        """Get the information about products in the category."""
        products_info = ""
        for product in self.__products:
            products_info += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_info

    def __len__(self):
        """Return the total number of products in the category."""
        total_quantity = 0
        for product in self.__products:
            total_quantity += product.quantity
        return total_quantity

    def __str__(self):
        """Return a string representation of the category."""
        return f"{self.name}, количество продуктов: {len(self.__products)} шт., общее количество: {len(self)} шт."

    def average_price(self):
        """Calculate the average price of all products in the category."""
        try:
            total_price = sum(product.price for product in self.__products)
            average_price = total_price / len(self.__products)
            return average_price
        except ZeroDivisionError:
            print("В категории нет товаров.")
            return 0


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


class ZeroQuantityError(Exception):
    """Exception raised when trying to add a product with zero quantity."""

    def __init__(self, message="Товар с нулевым количеством не может быть добавлен."):
        self.message = message
        super().__init__(self.message)
