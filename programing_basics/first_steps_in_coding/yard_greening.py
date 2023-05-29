square_meters = float(input())
price_for_square_meter = 7.61
total_price = square_meters * price_for_square_meter
discount = total_price * 0.18
final_price = total_price - discount
print(f'The final price is: {final_price} lv.')
print(f'The discount is: {discount} lv.')
