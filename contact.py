contacts = {
    "Alice": "123-456-7890",
    "Bob": "234-567-8901",
    "Charlie": "345-678-9012"
}
print("Current Contacts:")
for name, number in contacts.items():
    print(f"{name}: {number}")
name = input("\nEnter contact name: ").title()
phone = input("Enter phone number: ")
if name in contacts:
    print(f"\n{name} already exists with number {contacts[name]}. Updating number...")
else:
    print(f"\nAdding new contact: {name}")
contacts[name] = phone
print("\nUpdated Contacts:")
for name, number in contacts.items():
    print(f"{name}: {number}")
