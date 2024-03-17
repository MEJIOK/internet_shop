import pytest
from utils import Category, Product


def test_category_initialization():
    category = Category("Electronics", "Category for electronic devices")
    assert category.name == "Electronics"
    assert category.description == "Category for electronic devices"
    assert category._products == []  # Проверяем приватный атрибут
    assert Category.total_categories == 1


def test_product_initialization():
    product = Product("Smartphone", "Mobile phone", 999.99, 10)
    assert product.name == "Smartphone"
    assert product.description == "Mobile phone"
    assert product.price == 999.99
    assert product.quantity == 10
    assert Category.total_unique_products == 1


def test_product_count():
    Category.total_categories = 0
    Category.total_unique_products = 0

    category1 = Category("Electronics", "Category for electronic devices")
    category2 = Category("Clothing", "Category for clothes")

    product1 = Product("Smartphone", "Mobile phone", 999.99, 10)
    product2 = Product("Laptop", "Portable computer", 1499.99, 5)

    category1.add_product(product1)  # Добавляем товары в категории
    category2.add_product(product2)

    assert Category.total_categories == 2
    assert Category.total_unique_products == 2


if __name__ == '__main__':
    pytest.main()

