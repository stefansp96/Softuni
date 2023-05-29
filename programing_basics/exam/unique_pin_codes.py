first_num_limit = int(input())
second_num_limit = int(input())
third_num_limit = int(input())

for first_num in range(1, first_num_limit + 1):
    for second_num in range(2, second_num_limit + 1):
        for third_num in range(1, third_num_limit + 1):
            is_prime = True
            if second_num > 1:
                for i in range(2, second_num):
                    if second_num % i == 0:
                        is_prime = False
            if is_prime and first_num % 2 == 0 and third_num % 2 == 0:
                print(f'{first_num} {second_num} {third_num}')

