year_tax = int(input())
sneakers = year_tax - (year_tax * 0.40)
jersey = sneakers - (sneakers * 0.20)
ball = jersey * 0.25
accessories = ball * 0.20
final_sum = year_tax + sneakers + jersey + ball + accessories
print(final_sum)
