number_of_pages = int(input())
pages_per_hour = int(input())
days_for_book = int(input())
hours_needed = number_of_pages // pages_per_hour
hours_per_day = hours_needed // days_for_book
print(hours_per_day)
