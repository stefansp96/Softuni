word = input()
repeater = int(input())
repeat_string = lambda a, b: a * b
result = repeat_string(word, repeater)
print(result)