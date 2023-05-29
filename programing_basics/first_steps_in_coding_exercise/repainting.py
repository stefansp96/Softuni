nylon_needed = int(input())
paint_needed = int(input())
thinner_needed = int(input())
hours_for_work = int(input())
sum_nylon = (nylon_needed + 2) * 1.50
sum_paint = (paint_needed * 0.10 + paint_needed) * 14.50
sum_thinner = thinner_needed * 5
sum_bags = 0.40
sum_materials = sum_nylon + sum_paint + sum_thinner + sum_bags
sum_workers = (sum_materials * 0.30) * hours_for_work
final_sum = sum_materials + sum_workers
print(final_sum)
