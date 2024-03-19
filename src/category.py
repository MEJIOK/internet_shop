from src.products import Product


class Category:
    """Class representing a category of products."""
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description, products=None):
        """Initialize a Category object with name, description, and products."""
        self.name = name
        self.description = description
        self.__products = products if products is not None else []  # Приватный атрибут для хранения товаров
        Category.total_categories += 1
        Category.total_unique_products += len(self.__products)

    @classmethod
    def from_dict(cls, data):
        """Create a Category object from a dictionary."""
        _category = cls(data['name'], data['description'])
        for product_data in data.get('products', []):
            product = Product.create_product(**product_data)
            _category.add_product(product)  # Используем метод добавления продукта
        return _category

    def add_product(self, product):
        """Add a product to the category."""
        self.__products.append(product)  # Добавляем продукт в список товаров категории
        self.total_unique_products += 1

    def products(self):
        """Get the list of products in the category."""
        return self.__products

    @property
    def products_info(self):
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

