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
        self._price = price
        self.quantity = quantity
        Category.total_unique_products += 1

    @property
    def price(self):
        """Getter for the price attribute."""
        return self._price

    @price.setter
    def price(self, value):
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
    def from_dict(cls, data):
        """Create a Product object from a dictionary."""
        return cls(data['name'], data['description'], data['price'], data['quantity'])

    @classmethod
    def create_product(cls, name, description, price, quantity, products_list):
        """Create a new product or update existing one and return it."""
        for product in products_list:
            if product.name == name:
                # Если товар с таким именем уже существует, обновляем его данные
                product.price = max(product.price, price)  # Выбираем более высокую цену
                product.quantity += quantity  # Увеличиваем количество в наличии
                return product  # Возвращаем существующий товар

        # Если товар с таким именем не найден, создаем новый товар
        return cls(name, description, price, quantity)
