import pytest
from src.category import Category
from src.products import Product


def test_category_initialization():
    category = Category("Electronics", "Category for electronic devices")
    assert category.name == "Electronics"
    assert category.description == "Category for electronic devices"
    assert category.products() == []  # Проверяем, что список продуктов пуст
    assert Category.total_categories == 1  # Проверяем, что количество категорий равно 1
    assert category.total_unique_products == 0  # Проверяем, что количество уникальных продуктов равно 0


def test_add_product_to_category():
    category = Category("Electronics", "Category for electronic devices")
    product = Product("Smartphone", "Mobile phone", 999.99, 10)
    category.add_product(product)
    assert len(category.products()) == 1  # Проверяем, что после добавления продукта список содержит один элемент
    assert category.total_unique_products == 1  # Проверяем, что количество уникальных продуктов увеличилось на 1


if __name__ == '__main__':
    pytest.main()
