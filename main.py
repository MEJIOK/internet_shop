import json


class Category:
    """Class representing a category of products."""
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description):
        """Initialize a Category object with name and description."""
        self.name = name
        self.description = description
        self.products = []
        Category.total_categories += 1

    @classmethod
    def from_dict(cls, data):
        """Create a Category object from a dictionary."""
        _category = cls(data['name'], data['description'])
        for product_data in data.get('products', []):
            product = Product.from_dict(product_data)
            _category.products.append(product)
        return _category


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


def load_data_from_json(file_path):
    """Load data from a JSON file and create Category objects."""
    categories = []

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for category_data in data:
        category = Category.from_dict(category_data)
        categories.append(category)

    return categories


loaded_categories = load_data_from_json('products.json')
for category in loaded_categories:
    print(f"Category: {category.name}, Description: {category.description}")
    print("Products:")
    for product in category.products:
        print(f"- {product.name}: {product.description}, Price: {product.price}, Quantity: {product.quantity}")
