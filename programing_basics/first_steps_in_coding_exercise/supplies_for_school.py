sum_pens = int(input()) * 5.80
sum_markers = int(input()) * 7.20
sum_cleaner = int(input()) * 1.20
discount_percent = int(input()) / 100
total_sum = sum_pens + sum_cleaner + sum_markers
final_sum = total_sum - (total_sum * discount_percent)
print(final_sum)
