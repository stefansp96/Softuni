banned_words = input().split(', ')
some_text = input()

for word in banned_words:
    while word in some_text:
        some_text = some_text.replace(word, '*' * len(word))

print(some_text)
