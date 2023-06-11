numbers_as_string = input().split()
numbers_list = []
for num in numbers_as_string:
    num = float(num)
    numbers_list.append(abs(num))
print(numbers_list)
