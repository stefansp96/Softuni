def find_divisors(some_number):
    proper_divisors = []
    for num in range(1, number):
        if number % num == 0:
            proper_divisors.append(num)
    return proper_divisors


number = int(input())
if sum(find_divisors(number)) == number:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")

"""def is_perfect(some_number: int) -> str:
    divisors_sum = 0
    for divisor in range(1, some_number):
        if some_number % divisor == 0:
            divisors_sum += divisor
    if some_number == divisors_sum:
        return "We have a perfect number!"
    return "It's not so perfect."
 
 
number = int(input())
print(is_perfect(number))"""
