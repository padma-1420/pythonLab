names = ["Alice", "Arnold", "Bob", "Brenda", "Charlie", "Clara", "David", "Diana"]
grouped_names = {}
for name in names:
    first_letter = name[0].upper()
    if first_letter not in grouped_names:
        grouped_names[first_letter] = []
    grouped_names[first_letter].append(name)
for letter, name_list in grouped_names.items():
    print(f"{letter}: {name_list}")
