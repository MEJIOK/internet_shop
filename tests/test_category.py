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


if __name__ == '__main__':
    pytest.main()
