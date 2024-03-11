class Category:
    total_categories = 0  # Атрибут класса для хранения общего количества категорий
    total_unique_products = 0  # Атрибут класса для хранения общего количества уникальных продуктов

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.products = []  # Пустой список для хранения товаров в категории
        Category.total_categories += 1  # Увеличиваем общее количество категорий


class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        Category.total_unique_products += 1  # Увеличиваем общее количество уникальных продуктов
