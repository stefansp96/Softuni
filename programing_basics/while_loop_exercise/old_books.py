book_name = input()
book_count = 0
book_found = False

current_book = input()

while current_book != 'No More Books':
    if current_book == book_name:
        book_found = True
        print(f'You checked {book_count} books and found it.')
        break

    book_count += 1
    current_book = input()

if not book_found:
    print('The book you search is not here!')
    print(f'You checked {book_count} books.')
