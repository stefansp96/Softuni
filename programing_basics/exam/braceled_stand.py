allowance = float(input())
sales_income = float(input())
spent_money = float(input())
gift_cost = float(input())

allowance_saved = 5 * allowance
sales_saved = 5 * sales_income
total_money_saved = allowance_saved + sales_saved - spent_money
diff = abs(total_money_saved - gift_cost)

if total_money_saved >= gift_cost:
    print(f'Profit: {total_money_saved:.2f} BGN, the gift has been purchased.')
else:
    print(f'Insufficient money: {diff:.2f} BGN.')
