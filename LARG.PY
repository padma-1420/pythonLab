def find_largest(numbers):
    if not numbers:
        return None  # Return None if the list is empty
    largest = numbers[0]  # Start by assuming the first number is the largest
    for num in numbers:
        if num > largest:
            largest = num  # Update largest if a larger number is found
    return largest
