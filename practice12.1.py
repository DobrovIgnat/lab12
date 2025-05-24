import json


def print_products_from_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for product in data['products']:
        print(f"Название: {product['name']}")
        print(f"Цена: {product['price']}")
        print(f"Вес: {product['weight']}")
        print("В наличии" if product['available'] else "Нет в наличии!")
        print()


print_products_from_json('1.json')