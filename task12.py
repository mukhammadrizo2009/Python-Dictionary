inventory = {
    "apple": {"quantity: 5"},
    "banana": {"quantity: 8"},
    "peach": {"quantity: 11"}
}

produkt = input('Mahsulotni kiriting!: ')

if produkt not in inventory:
    inventory[produkt] = {"quantity" : 0}

print("Natija: ",inventory)