people_in_circle = input().split(' ')
execution_step = int(input())
executed_order = []
counter = 0
index = 0

while people_in_circle:
    counter += 1
    if counter % execution_step == 0:
        executed_order.append(people_in_circle.pop(index))
    else:
        index += 1

    if index >= len(people_in_circle):
        index = 0

print(str(executed_order).replace(' ', '').replace("'", ""))