numbers = [4, 7, 2, 4, 9, 2, 7, 1, 5, 9]
duplicates = []
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j] and numbers[i] not in duplicates:
            duplicates.append(numbers[i])
print("Duplicate values are:", duplicates)
