def odd_even_numbers(some_numbers):
    sum_of_even_numbers = 0
    sum_of_odd_numbers = 0
    for num in some_numbers:
        if int(num) % 2 == 0:
            sum_of_even_numbers += int(num)
        else:
            sum_of_odd_numbers += int(num)
    return sum_of_even_numbers, sum_of_odd_numbers


number = input()
even_numbers, odd_numbers = odd_even_numbers(number)
print(f'Odd sum = {odd_numbers}, Even sum = {even_numbers}')
