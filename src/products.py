class Product:
    """Class representing a product."""

    def __init__(self, name, description, price, quantity):
        """Initialize a Product object with name, description, price, and quantity."""
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    def __str__(self):
        """Return a string representation of the product."""
        return f"{self.name}, {self._price} руб. Остаток: {self.quantity} шт."

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
    def create(cls, **kwargs):
        """Create a new product using kwargs."""
        return cls(**kwargs)

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

    def __add__(self, other):
        """Return the total price of two products considering their quantities."""
        if isinstance(other, Product) and self.name == other.name and self.description == other.description:
            total_price_self = self.price * self.quantity
            total_price_other = other.price * other.quantity
            total_price = total_price_self + total_price_other
            return total_price
        else:
            raise ValueError("Нельзя складывать различные товары или товары с разными названиями/описаниями.")


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
