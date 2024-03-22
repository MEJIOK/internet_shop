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
        if not isinstance(product, self.allowed_types):
            raise TypeError(f"Можно добавлять только продукты следующих типов: {self.allowed_types}")
        self.__products.append(product)
        self.total_unique_products += 1

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


class CategoryIterator:
    """Iterator for iterating over products in a category."""
# Может быть этот класс нужно убрать в файл с категориями?
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
