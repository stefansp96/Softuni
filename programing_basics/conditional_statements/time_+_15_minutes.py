current_hours = int(input())
current_minutes = int(input())

total_time_in_minutes = current_hours * 60 + (current_minutes + 15)

hours = total_time_in_minutes // 60
minutes = total_time_in_minutes % 60

if hours > 23:
    hours = 0

if minutes < 10:
    print(f'{hours}:0{minutes}')
else:
    print(f'{hours}:{minutes}')
