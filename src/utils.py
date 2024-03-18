import json
from src.category import Category


def load_data_from_json(file_path):
    """Load data from a JSON file and create Category objects."""
    categories = []

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for category_data in data:
        category = Category.from_dict(category_data)
        categories.append(category)

    return categories


class Product:
    pass