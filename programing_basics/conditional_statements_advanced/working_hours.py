hour = int(input())
day = input()

if 10 <= hour <= 18:
    if day != 'Sunday':
        print('open')
    else:
        print('closed')
else:
    print('closed')
