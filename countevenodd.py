def count_even_odd(numbers):
    even_count = 0
    odd_count = 0
    
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    print(f"Even numbers: {even_count}, Odd numbers: {odd_count}")
numbers = [1, 2, 3, 4, 5, 6]
count_even_odd(numbers)
