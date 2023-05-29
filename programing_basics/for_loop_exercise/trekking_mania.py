groups_people = int(input())
musala = 0
monblan = 0
kilimandzharu = 0
k2 = 0
everest = 0

for people in range(groups_people):
    current_people = int(input())
    if current_people <= 5:
        musala += current_people
    elif 6 <= current_people <= 12:
        monblan += current_people
    elif 13 <= current_people <= 25:
        kilimandzharu += current_people
    elif 26 <= current_people <= 40:
        k2 += current_people
    else:
        everest += current_people

total_people = musala + monblan + kilimandzharu + k2 + everest
musala_percent = musala / total_people * 100
monblan_percent = monblan / total_people * 100
kilimandzharu_percent = kilimandzharu / total_people * 100
k2_percent = k2 / total_people * 100
everest_percent = everest / total_people * 100

print(f'{musala_percent:.2f}%')
print(f'{monblan_percent:.2f}%')
print(f'{kilimandzharu_percent:.2f}%')
print(f'{k2_percent:.2f}%')
print(f'{everest_percent:.2f}%')
