def generate_invoice(customer_name, products):
    print("\n" + "="*40)
    print(" " * 10 + "INVOICE")
    print("="*40)
    print(f"Customer Name: {customer_name}")
    print("-" * 40)
    print(f"{'Product':20} {'Price':>10}")
    print("-" * 40)
    
    total = 0
    for product, price in products:
        print(f"{product:20} ${price:>9.2f}")
        total += price
    
    print("-" * 40)
    print(f"{'Total':20} ${total:>9.2f}")
    print("="*40)
    print("Thank you for your purchase!")
    print("="*40)
if __name__ == "__main__":
    customer = input("Enter customer name: ")
    products = []

    while True:
        product_name = input("Enter product name (or type 'done' to finish): ")
        if product_name.lower() == 'done':
            break
        try:
            price = float(input(f"Enter price for {product_name}: "))
            products.append((product_name, price))
        except ValueError:
            print("Invalid price. Please enter a numeric value.")

    if products:
        generate_invoice(customer, products)
    else:
        print("No products entered. Invoice not generated.")
