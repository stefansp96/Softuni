force_sides = {}

while True:
    command = input()

    if command == "Lumpawaroo":
        break

    if '|' in command:
        command = command.split(' | ')
        force_side = command[0]
        force_user = command[1]
        force_exists = False
        user_exists = False

        for key, val in force_sides.items():
            if key == force_side:
                force_exists = True
            if force_user in val:
                user_exists = True

        if not force_exists and not user_exists:
            force_sides[force_side] = [force_user]
        elif force_exists and not user_exists:
            force_sides[force_side].append(force_user)
        elif user_exists:
            continue

    if ' -> ' in command:
        command = command.split(' -> ')
        force_user = command[0]
        force_side = command[1]
        force_exists = False
        user_exists = False
        no_change_needed = False

        for key, val in force_sides.items():
            if key == force_side:
                force_exists = True
            if force_user in val:
                user_exists = True
            if key == force_side and force_user in val:
                no_change_needed = True

        if user_exists and not no_change_needed:
            for side, current_user in force_sides.items():
                for index in range(len(current_user)):
                    if current_user[index] == force_user:
                        current_user.pop(index)
            if force_side in force_sides.keys():
                force_sides[force_side].append(force_user)
                print(f"{force_user} joins the {force_side} side!")
        elif force_exists and not user_exists:
            force_sides[force_side].append(force_user)
            print(f"{force_user} joins the {force_side} side!")
        elif not user_exists and not force_exists:
            force_sides[force_side] = [force_user]
            print(f"{force_user} joins the {force_side} side!")

for key, val in force_sides.items():
    if len(val) > 0:
        print(f"Side: {key}, Members: {len(val)}")
        for current_val in val:
            print(f"! {current_val}")
