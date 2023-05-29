movie_type = input()
rows = int(input())
columns = int(input())
capacity = rows * columns
income = 0

if movie_type == 'Premiere':
    income = capacity * 12
elif movie_type == 'Normal':
    income = capacity * 7.50
elif movie_type == 'Discount':
    income = capacity * 5

print(f'{income:.2f} leva')
