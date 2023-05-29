pool_volume = int(input())
p1_output = int(input())
p2_output = int(input())
hours_missing = float(input())

p1_total_output = p1_output * hours_missing
p2_total_output = p2_output * hours_missing
total_output = p1_total_output + p2_total_output
p1_percentage = (p1_total_output / total_output) * 100
p2_percentage = (p2_total_output / total_output) * 100
total_percentage = ((p1_total_output + p2_total_output) / pool_volume) * 100

if total_output <= pool_volume:
    print(f"The pool is {total_percentage:.2f}% full. Pipe 1: {p1_percentage:.2f}%. Pipe 2: {p2_percentage:.2f}%.")
else:
    print(f"For {hours_missing} hours the pool overflows with {total_output - pool_volume:.2f} liters.")
