def sum_of_even_numbers(start, end):
    total = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            total += num
    print(f"Sum of even numbers from {start} to {end} is: {total}")
start = 1
end = 10
sum_of_even_numbers(start, end)
