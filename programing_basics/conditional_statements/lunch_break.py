from math import ceil

name_of_series = str(input())
length_of_episode = int(input())
length_of_break = int(input())

lunch_time = (1 / 8) * length_of_break
relax_time = (1 / 4) * length_of_break

time_for_series = length_of_break - lunch_time - relax_time
difference = ceil(abs(length_of_break - (lunch_time + relax_time + length_of_episode)))

if time_for_series >= length_of_episode:
    print(f'You have enough time to watch {name_of_series} and left with {difference} minutes free time.')
else:
    print(f"You don't have enough time to watch {name_of_series}, you need {difference} more minutes.")
