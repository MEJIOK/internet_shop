class Category:
    """Class representing a category of products."""
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description):
        """Initialize a Category object with name and description."""
        self.name = name
        self.description = description
        self._products = []  # Приватный атрибут для хранения товаров
        Category.total_categories += 1

    @classmethod
    def from_dict(cls, data):
        """Create a Category object from a dictionary."""
        _category = cls(data['name'], data['description'])
        for product_data in data.get('products', []):
            product = Product.from_dict(product_data)
            _category.add_product(product)  # Используем метод добавления продукта
        return _category

    def add_product(self, product):
        """Add a product to the category."""
        self._products.append(product)  # Добавляем продукт в список товаров категории

    def get_products(self):
        """Get the list of products in the category."""
        return self._products

    @property
    def products_info(self):
        """Get the information about products in the category."""
        products_info = ""
        for product in self._products:
            products_info += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_info


class Product:
    """Class representing a product."""

    def __init__(self, name, description, price, quantity):
        """Initialize a Product object with name, description, price, and quantity."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        Category.total_unique_products += 1

    @classmethod
    def from_dict(cls, data):
        """Create a Product object from a dictionary."""
        return cls(data['name'], data['description'], data['price'], data['quantity'])
