number_of_electrons = int(input())
current_cell = 1
filled_cells = []

while number_of_electrons > 0:
    current_cell_value = 2*(current_cell**2)
    electrons_in_cell = 0
    while electrons_in_cell < current_cell_value:
        number_of_electrons -= 1
        electrons_in_cell += 1
        if number_of_electrons == 0:
            break
    filled_cells.append(electrons_in_cell)
    current_cell += 1

print(filled_cells)
