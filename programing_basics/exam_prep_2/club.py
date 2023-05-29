desired_income = float(input())
income = 0
command = input()

while True:
    cocktail = command

    if command == 'Party!':
        print(f'We need {desired_income - income:.2f} leva more.')
        print(f'Club income - {income:.2f} leva.')
        break

    num_cocktails = int(input())
    cocktail_cost = len(cocktail)
    total_cost = cocktail_cost * num_cocktails

    if total_cost % 2 != 0:
        total_cost *= 0.75

    income += total_cost

    if income >= desired_income:
        print("Target acquired.")
        print(f'Club income - {income:.2f} leva.')
        break

    command = input()

