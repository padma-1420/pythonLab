def print_pyramid(n):
    for i in range(n):
        spaces = n - i - 1
        stars = 2 * i + 1
        print(' ' * spaces + '*' * stars)
n = int(input("Enter the number of rows: "))
print_pyramid(n)
