word = input()
vowels_list = ['a', 'o', 'u', 'e', 'i']
remove_vowels = [char for char in word if char.lower() not in vowels_list]
filtered_word = ''.join(remove_vowels)
print(filtered_word)
