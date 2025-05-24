import json

try:
    with open('1.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
except FileNotFoundError:
    data = {"products": []}

print("\nДобавление нового продукта:")
data["products"].append({
    "name": input("Название: "),
    "price": int(input("Цена: ")),
    "available": input("В наличии (да/нет): ").lower() == "да",
    "weight": int(input("Вес: "))
})

with open('products_updated.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\nСписок продуктов:")
for product in data["products"]:
    print(f"Название: {product['name']}")
    print(f"Цена: {product['price']}")
    print(f"Вес: {product['weight']}")
    print("В наличии" if product['available'] else "Нет в наличии!")
    print()