years = int(input())
washing_machine = float(input())
price_toy = int(input())

num_toys = 0
money = 0

for i in range(1, years + 1):
    if i % 2 == 0:
        money += i * 5 - 1
    else:
        num_toys += 1

final_money = money + num_toys * price_toy
diff = abs(washing_machine - final_money)

if final_money >= washing_machine:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')
