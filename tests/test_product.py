import pytest
from src.category import Category
from src.products import Product, Smartphone


def test_category_initialization():
    """Проверяем инициализацию категории."""
    category = Category("Electronics", "Category for electronic devices")
    assert category.name == "Electronics"
    assert category.description == "Category for electronic devices"
    assert category.products() == []  # Проверяем, что список продуктов пуст
    assert Category.total_categories == 1  # Проверяем, что количество категорий равно 1
    assert category.total_unique_products == 0  # Проверяем, что количество уникальных продуктов равно 0


def test_add_product_to_category():
    """Проверяем добавление продукта в категорию."""
    # Создаем категорию и продукт
    category = Category("Electronics", "Category for electronic devices",
                        allowed_types=(Product, Smartphone))
    product = Product("Smartphone", "Mobile phone", 999.99, 10, "black")

    # Добавляем продукт в категорию
    category.add_product(product)

    # Проверяем, что продукт был успешно добавлен
    assert len(category.products()) == 1
    assert category.total_unique_products == 1
    assert category.products()[0] == product


def test_addition_of_products():
    """Проверяем сложение продуктов."""
    # Создаем два продукта одного типа
    product1 = Product("Smartphone", "Mobile phone", 999.99, 10, "black")
    product2 = Product("Smartphone", "Mobile phone", 799.99, 5, "white")

    # Складываем их
    total_price = product1 + product2

    # Проверяем, что общая цена правильная
    assert total_price == (999.99 * 10) + (799.99 * 5)


def test_adding_different_types_of_products():
    """Проверяем добавление продуктов разных типов в категорию."""
    # Создаем категорию
    category = Category("Electronics", "Category for electronic devices")

    # Создаем продукт разного типа
    product1 = Product("Smartphone", "Mobile phone", 999.99, 10, "black")
    product2 = Smartphone("iPhone", "Apple smartphone", 1299.99, 8, "silver", "High", "iPhone 12", "256GB")

    # Пытаемся добавить их в категорию
    with pytest.raises(TypeError):
        category.add_product(product1)
        category.add_product(product2)


if __name__ == '__main__':
    pytest.main()
