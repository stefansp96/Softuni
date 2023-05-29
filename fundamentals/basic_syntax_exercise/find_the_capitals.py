input_word = input()
index_list = []

for i in range(len(input_word)):
    if input_word[i].isupper():
        index_list.append(i)

print(index_list)