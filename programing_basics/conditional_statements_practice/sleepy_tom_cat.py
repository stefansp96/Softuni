weekends = int(input())
days_in_year = 365
working_days = days_in_year - weekends
norm_play_for_year = 30000

playtime_for_year = weekends * 127 + working_days * 63
diff = abs(norm_play_for_year - playtime_for_year)
hours = diff // 60
minutes = diff % 60

if playtime_for_year > norm_play_for_year:
    print('Tom will run away')
    print(f'{hours} hours and {minutes} minutes more for play')
else:
    print('Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')
