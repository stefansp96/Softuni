money_as_string = input().split(', ')
beggar_count = int(input())
money_as_digits = []

for element in money_as_string:
    money_as_digits.append(int(element))

collected_money = []
start_index = 0

while start_index < beggar_count:
    money_for_current_beggar = 0
    for current_index in range(start_index, len(money_as_digits), beggar_count):
        money_for_current_beggar += money_as_digits[current_index]
    collected_money.append(money_for_current_beggar)
    start_index += 1

print(collected_money)
