numbers = [12, 45, 2, 99, 23, 7]
smallest = numbers[0]
largest = numbers[0]
for number in numbers:
    if number < smallest:
        smallest = number
    if number > largest:
        largest = number
print("Smallest number is:", smallest)
print("Largest number is:", largest)
