class Category:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.products = []  # Пустой список для хранения товаров в категории


class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
