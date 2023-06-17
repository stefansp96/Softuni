word_list = input().split(' ')
even_word_list = [word for word in word_list if len(word) % 2 == 0]
for even_word in even_word_list:
    print(''.join(even_word))
