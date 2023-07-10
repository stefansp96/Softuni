text = [char for char in input() if char != ' ']
letters = {}

for symbol in text:
    if symbol not in letters.keys():
        letters[symbol] = 1
    else:
        letters[symbol] += 1

for letter, occurrences in letters.items():
    print(f"{letter} -> {occurrences}")
