cake_width = int(input())
cake_length = int(input())
cake_size = cake_length * cake_width
total_pieces = 0


while cake_size > 0:
    command = input()
    if command == 'STOP':
        print(f'{cake_size} pieces are left.')
        break
    else:
        cake_size -= int(command)
        total_pieces += int(command)

if cake_size < 0:
    print(f'No more cake left! You need {abs(cake_width * cake_length - total_pieces)} pieces more.')
