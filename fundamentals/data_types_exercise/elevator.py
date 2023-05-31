num_people = int(input())
capacity = int(input())
result = num_people // capacity
if num_people % capacity != 0:
    result += 1
print(result)
