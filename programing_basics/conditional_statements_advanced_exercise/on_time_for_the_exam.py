exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_time_in_minutes = exam_hour * 60 + exam_minutes
arrival_time_in_minutes = arrival_hour * 60 + arrival_minutes
diff = abs(exam_time_in_minutes - arrival_time_in_minutes)
hours = diff // 60
minutes = diff % 60

if arrival_time_in_minutes == exam_time_in_minutes:
    print('On time')

elif exam_time_in_minutes > arrival_time_in_minutes:
    if diff <= 30:
        print('On time')
        print(f'{minutes} minutes before the start')
    elif 30 < diff < 60:
        print('Early')
        print(f'{minutes} minutes before the start')
    elif diff >= 60:
        print('Early')
        print(f'{hours}:{minutes:02d} hours before the start')

else:
    print('Late')
    if diff < 60:
        print(f'{minutes} minutes after the start')
    elif diff >= 60:
        print(f'{hours}:{minutes:02d} hours after the start')
