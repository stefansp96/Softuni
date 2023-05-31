companions = int(input())
days_of_adventure = int(input())
coins = 0

for day in range(1, days_of_adventure + 1):
    if day % 10 == 0:
        companions -= 2
    if day % 15 == 0:
        companions += 5
    if day % 3 == 0:
        coins -= companions * 3
    if day % 5 == 0:
        coins += 20 * companions
        if day % 3 == 0:
           coins -= companions * 2
    coins += 50
    coins -= companions * 2

coins_per_companion = coins // companions
print(f"{companions} companions received {coins_per_companion} coins each.")
