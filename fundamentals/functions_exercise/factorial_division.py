def factorial_number(some_number):
    result = 1
    for num in range(1, some_number + 1):
        result *= num
    return result


first_number = int(input())
second_number = int(input())
division_factorial = factorial_number(first_number) / factorial_number(second_number)
print(f'{division_factorial:.2f}')