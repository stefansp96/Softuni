month = input()
number_nights = int(input())
price_for_stay_studio = 0
price_for_stay_apartment = 0
price_for_studio = 0
price_for_apartment = 0

if month == 'May' or month == 'October':
    price_for_studio = 50
    price_for_stay_studio = number_nights * price_for_studio
    if 7 < number_nights <= 14:
        price_for_stay_studio *= 0.95
    elif number_nights > 14:
        price_for_stay_studio *= 0.70
    price_for_apartment = 65
    price_for_stay_apartment = price_for_apartment * number_nights
    if number_nights > 14:
        price_for_stay_apartment *= 0.90
    print(f'Apartment: {price_for_stay_apartment:.2f} lv.')
    print(f'Studio: {price_for_stay_studio:.2f} lv.')

if month == 'June' or month == 'September':
    price_for_studio = 75.20
    price_for_stay_studio = number_nights * price_for_studio
    if number_nights > 14:
        price_for_stay_studio *= 0.80
    price_for_apartment = 68.70
    price_for_stay_apartment = price_for_apartment * number_nights
    if number_nights > 14:
        price_for_stay_apartment *= 0.90
    print(f'Apartment: {price_for_stay_apartment:.2f} lv.')
    print(f'Studio: {price_for_stay_studio:.2f} lv.')

if month == 'July' or month == 'August':
    price_for_studio = 76
    price_for_stay_studio = number_nights * price_for_studio
    price_for_apartment = 77
    price_for_stay_apartment = price_for_apartment * number_nights
    if number_nights > 14:
        price_for_stay_apartment *= 0.90
    print(f'Apartment: {price_for_stay_apartment:.2f} lv.')
    print(f'Studio: {price_for_stay_studio:.2f} lv.')
