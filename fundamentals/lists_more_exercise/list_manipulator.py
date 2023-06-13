given_numbers = input().split()
given_numbers_list = []
for n in given_numbers:
    n = int(n)
    given_numbers_list.append(n)
final_list_of_numbers = []
command = input()

while command != 'end':
