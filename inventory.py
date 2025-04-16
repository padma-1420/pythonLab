inventory = {
    "apple": 50,
    "banana": 30,
    "orange": 20,
    "mango": 15
}
print("Current Inventory:")
for item, quantity in inventory.items():
    print(f"{item.title()}: {quantity}")
item_to_sell = input("\nEnter the item you want to sell: ").lower()
quantity_to_sell = int(input("Enter the quantity to sell: "))
if item_to_sell in inventory:
    if inventory[item_to_sell] >= quantity_to_sell:
        inventory[item_to_sell] -= quantity_to_sell
        print(f"\nSold {quantity_to_sell} {item_to_sell}(s).")
        print(f"Remaining stock of {item_to_sell}: {inventory[item_to_sell]}")
    else:
        print(f"\nNot enough stock! Only {inventory[item_to_sell]} {item_to_sell}(s) available.")
else:
    print(f"\nItem '{item_to_sell}' not found in inventory.")
