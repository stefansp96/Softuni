chicken_menu = int(input()) * 10.35
fish_menu = int(input()) * 12.40
vegan_menu = int(input()) * 8.15
menu_sum = chicken_menu + fish_menu + vegan_menu
desert_price = menu_sum * 0.20
delivery_price = 2.50
final_sum = (menu_sum + desert_price + delivery_price)
print (final_sum)
