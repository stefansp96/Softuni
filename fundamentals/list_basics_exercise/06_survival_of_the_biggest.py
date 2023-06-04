numbers_string = input().split()
numbers_list = []

for num in numbers_string:
    numbers_list.append(int(num))

nums_remover = int(input())

for _ in range(nums_remover):
    numbers_list.remove(min(numbers_list))

list_as_string = ', '.join(map(str, numbers_list))
print(list_as_string)