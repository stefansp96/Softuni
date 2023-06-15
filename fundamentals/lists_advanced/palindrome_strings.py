list_of_words = input().split(' ')
palindrome = input()
list_of_palindromes = []

for word in list_of_words:
    if word == ''.join(reversed(word)):
        list_of_palindromes.append(word)

print(list_of_palindromes)
print(f"Found palindrome {list_of_palindromes.count(palindrome)} times")
