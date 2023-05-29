kilometers = int(input())
time_of_day = input()
price = 0

taxi_fare = 0.70
if time_of_day == 'day':
    taxi_fare += kilometers * 0.79
elif time_of_day == 'night':
    taxi_fare += kilometers * 0.90

bus_fare = kilometers * 0.09
train_fare = kilometers * 0.06

if kilometers < 20:
    price = taxi_fare
elif 20 <= kilometers < 100:
    price = bus_fare
else:
    price = train_fare

print(f'{price:.2f}')
