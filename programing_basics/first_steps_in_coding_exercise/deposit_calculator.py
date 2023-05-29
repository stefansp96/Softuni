deposit_sum = float(input())
months = int(input())
year_interest_percent = float(input()) / 100
interest = deposit_sum * year_interest_percent
month_interest = interest / 12
final_sum = deposit_sum + months * month_interest
print(final_sum)
