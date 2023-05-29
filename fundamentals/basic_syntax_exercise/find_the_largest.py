number = int(input())
string_number = str(number)
digits = [int(x) for x in string_number]
digits.sort(reverse=True)
for i in digits:
    print(i, end='')
