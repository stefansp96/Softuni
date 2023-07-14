some_text = input()
digits = ''
letters = ''
others = ''

for char in some_text:
    if char.isdigit():
        digits += char
    elif char.isalpha():
        letters += char
    else:
        others += char

print(digits)
print(letters)
print(others)
