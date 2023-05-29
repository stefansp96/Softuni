text = input()
sum_vol = 0
for c in text:
    if c == 'a':
        sum_vol += 1
    elif c == 'e':
        sum_vol += 2
    elif c == 'i':
        sum_vol += 3
    elif c == 'o':
        sum_vol += 4
    elif c == 'u':
        sum_vol += 5

print(sum_vol)