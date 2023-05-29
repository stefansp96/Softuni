num_messages = int(input())

for i in range(num_messages):
    number = int(input())
    message = ''
    if number < 88:
        message = 'GREAT!'
    if number == 86:
        message = 'How are you?'
    if number == 88:
        message = 'Hello'
    if number > 88:
        message = 'Bye.'
    print(message)
