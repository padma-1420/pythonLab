colors = ['red', 'green', 'white', 'black']
print("Original list:", colors)
print("Traverse the said list in reverse order with original indices:")
for i in range(len(colors) - 1, -1, -1):
    print(f"Index {i}: {colors[i]}")
