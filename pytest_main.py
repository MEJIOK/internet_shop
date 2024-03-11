import pytest
from main import Category, Product  # Подставьте имя вашего модуля, где определены классы


def test_category_initialization():
    category = Category("Electronics", "Category for electronic devices")
    assert category.name == "Electronics"
    assert category.description == "Category for electronic devices"
    assert category.products == []
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

    Category("Electronics", "Category for electronic devices")
    Category("Clothing", "Category for clothes")
    Product("Smartphone", "Mobile phone", 999.99, 10)
    Product("Laptop", "Portable computer", 1499.99, 5)

    assert Category.total_categories == 2
    assert Category.total_unique_products == 2


if __name__ == '__main__':
    pytest.main()
