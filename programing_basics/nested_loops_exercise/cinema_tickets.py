movie = input()
total_tickets = 0
standard_counter = 0
student_counter = 0
kids_counter = 0

while movie != 'Finish':
    free_seats = int(input())
    tickets_for_movie = 0

    while free_seats > 0:
        ticket_type = input()

        if ticket_type == 'End':
            break

        free_seats -= 1
        tickets_for_movie += 1

        if ticket_type == 'standard':
            standard_counter += 1
            total_tickets += 1
        elif ticket_type == 'student':
            student_counter += 1
            total_tickets += 1
        elif ticket_type == 'kid':
            kids_counter += 1
            total_tickets += 1

    percent_tickets_movie = tickets_for_movie / (tickets_for_movie + free_seats)
    print(f'{movie} - {percent_tickets_movie * 100:.2f}% full.')

    movie = input()

print(f'Total tickets: {total_tickets}')
print(f'{(student_counter / total_tickets * 100):.2f}% student tickets.')
print(f'{(standard_counter / total_tickets * 100):.2f}% standard tickets.')
print(f'{(kids_counter / total_tickets * 100):.2f}% kids tickets.')
